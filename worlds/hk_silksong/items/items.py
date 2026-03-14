from random import Random
from typing import Dict, List, Protocol, Union

from BaseClasses import Item, ItemClassification
from ..options.options import SilksongOptions
from ..strings.generic_strings import GAME_NAME


class SilksongItem(Item):
    game: str = GAME_NAME


offset = 1_757_008_800


items_by_id: Dict[int, str] = dict()
items_by_name: Dict[str, int] = dict()


def generate_id(name: str) -> int:
    id = 0
    for char in name:
        id = id * 26
        id += (ord(char.lower()) - 96)
    id = id % 1125899906842624
    return id


class ItemData:
    id: int
    name: str
    classification: ItemClassification

    def __init__(self, name: str, classification: ItemClassification = ItemClassification.progression, event_only: bool = False):
        if event_only:
            self.id = -1
        else:
            if name in items_by_name:
                self.id = items_by_name[name]
            else:
                self.id = generate_id(name)
        self.name = name
        self.classification = classification
        if not event_only:
            items_by_name[self.name] = self.id
            items_by_id[self.id] = self.name
        item_data_by_name[self.name] = self


item_data_by_name: Dict[str, ItemData] = dict()


class SilksongItemFactory(Protocol):
    def __call__(self, name: Union[str, ItemData], override_classification: ItemClassification = None) -> Item:
        raise NotImplementedError


filler_items = [
    ItemData("10 Rosaries", ItemClassification.filler),
    ItemData("10 Shell Shards", ItemClassification.filler),
    ItemData("25 Rosaries", ItemClassification.filler),
    ItemData("25 Shell Shards", ItemClassification.filler),
    ItemData("50 Rosaries", ItemClassification.filler),
    ItemData("50 Shell Shards", ItemClassification.filler),
    ItemData("100 Rosaries", ItemClassification.filler),
    ItemData("100 Shell Shards", ItemClassification.filler),
    ItemData("150 Shell Shards", ItemClassification.filler),
    ItemData("200 Shell Shards", ItemClassification.filler),
]


def create_items(item_factory: SilksongItemFactory, world_options: SilksongOptions, locations_items_pairs, enabled_locations: list[str],
                 excluded_items: list[str], random: Random) -> List[Item]:
    items_to_create = []
    items_to_create.extend(choose_items_based_on_enabled_locations(world_options, locations_items_pairs, enabled_locations))

    for excluded_item in excluded_items:
        if excluded_item in items_to_create:
            items_to_create.remove(excluded_item)

    number_items = len(items_to_create)
    locations_count = len(enabled_locations)
    number_filler = locations_count - number_items

    items_to_create.extend(choose_fillers_and_traps(world_options, number_filler, random))

    return [item_factory(item) for item in items_to_create]


def choose_items_based_on_enabled_locations(world_options: SilksongOptions, locations_items_pairs, enabled_locations) -> List[str]:
    items = []
    for enabled_location in enabled_locations:
        loc_item_pair = locations_items_pairs[enabled_location]
        if loc_item_pair.item_data is None:
            continue
        items.append(loc_item_pair.item_data.name)
    return items


def choose_fillers_and_traps(world_options: SilksongOptions, number_filler: int, random: Random) -> List[str]:
    valid_filler_names = []
    valid_filler_names.extend([item.name for item in filler_items])
    # valid_filler_names.extend(item_names_by_groups[ItemGroup.TRAP])

    chosen_filler = random.choices(valid_filler_names, k=number_filler)

    return chosen_filler
