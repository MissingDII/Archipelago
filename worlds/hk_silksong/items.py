import enum
from random import Random
from typing import Dict, List, Protocol, Union

from BaseClasses import Item, ItemClassification
from .options.options import ShuffleMovementAbilities, SilksongOptions
from .strings.generic_strings import GAME_NAME
from .strings.item_names import ItemName


class SilksongItem(Item):
    game: str = GAME_NAME


offset = 1_757_008_800


class ItemGroup(enum.Enum):
    SLASH = enum.auto()
    ACT_1 = enum.auto()
    ACT_2 = enum.auto()
    ACT_3 = enum.auto()
    SONG = enum.auto()
    BIND = enum.auto()
    MOVEMENT_ABILITY = enum.auto()
    SILK_COMBAT_ABILITY = enum.auto()
    SILK_OTHER_ABILITY = enum.auto()
    COMBAT_ABILITY = enum.auto()
    SHARDS = enum.auto()
    ROSARIES = enum.auto()

    FILLER = enum.auto()
    TRAP = enum.auto()


items_by_id: Dict[int, str] = dict()
items_by_name: Dict[str, int] = dict()
item_names_by_groups: Dict[ItemGroup, List[str]] = dict()


class ItemData:
    id: int
    name: str
    classification: ItemClassification
    groups: List[ItemGroup]

    def __init__(self, name: str, classification: ItemClassification, groups: List[ItemGroup]):
        if name in items_by_name:
            self.id = items_by_name[name]
        else:
            self.id = len(items_by_name) + 1
        self.name = name
        self.classification = classification
        self.groups = groups
        items_by_name[self.name] = self.id
        items_by_id[self.id] = self.name
        for group in self.groups:
            if group not in item_names_by_groups:
                item_names_by_groups[group] = []
            item_names_by_groups[group].append(self.name)

    def has_any_group(self, *group: ItemGroup) -> bool:
        groups = set(group)
        return bool(groups.intersection(self.groups))


class SilksongItemFactory(Protocol):
    def __call__(self, name: Union[str, ItemData], override_classification: ItemClassification = None) -> Item:
        raise NotImplementedError


all_items = [
    ItemData(ItemName.needolin, ItemClassification.progression, [ItemGroup.SONG, ItemGroup.ACT_1]),
    ItemData(ItemName.beastling_call, ItemClassification.useful, [ItemGroup.SONG, ItemGroup.ACT_3]),
    ItemData(ItemName.elegy_of_the_deep, ItemClassification.progression, [ItemGroup.SONG, ItemGroup.ACT_3]),

    ItemData(ItemName.bind, ItemClassification.progression, [ItemGroup.BIND, ItemGroup.ACT_1]),

    ItemData(ItemName.silkspear, ItemClassification.progression, [ItemGroup.SILK_COMBAT_ABILITY, ItemGroup.ACT_1]),
    ItemData(ItemName.cross_stitch, ItemClassification.useful, [ItemGroup.SILK_COMBAT_ABILITY, ItemGroup.ACT_1]),
    ItemData(ItemName.thread_storm, ItemClassification.useful, [ItemGroup.SILK_COMBAT_ABILITY, ItemGroup.ACT_1]),
    ItemData(ItemName.sharpdart, ItemClassification.useful, [ItemGroup.SILK_COMBAT_ABILITY, ItemGroup.ACT_2]),
    ItemData(ItemName.rune_rage, ItemClassification.useful, [ItemGroup.SILK_COMBAT_ABILITY, ItemGroup.ACT_2]),
    ItemData(ItemName.pale_nails, ItemClassification.useful, [ItemGroup.SILK_COMBAT_ABILITY, ItemGroup.ACT_3]),

    ItemData(ItemName.drifters_cloak, ItemClassification.progression, [ItemGroup.MOVEMENT_ABILITY, ItemGroup.ACT_1]),
    ItemData(ItemName.cling_grip, ItemClassification.progression, [ItemGroup.MOVEMENT_ABILITY, ItemGroup.ACT_1]),
    ItemData(ItemName.swift_step, ItemClassification.progression, [ItemGroup.MOVEMENT_ABILITY, ItemGroup.ACT_1]),
    ItemData(ItemName.faydown_cloak, ItemClassification.progression, [ItemGroup.MOVEMENT_ABILITY, ItemGroup.ACT_2]),
    ItemData(ItemName.clawline, ItemClassification.progression, [ItemGroup.MOVEMENT_ABILITY, ItemGroup.ACT_2]),
    ItemData(ItemName.silk_soar, ItemClassification.progression, [ItemGroup.MOVEMENT_ABILITY, ItemGroup.ACT_3]),

    ItemData(ItemName.needle_strike, ItemClassification.progression, [ItemGroup.COMBAT_ABILITY, ItemGroup.ACT_1]),

    ItemData(ItemName.silk_heart, ItemClassification.progression, [ItemGroup.SILK_OTHER_ABILITY, ItemGroup.ACT_1]),
    ItemData(ItemName.sylphsong, ItemClassification.useful, [ItemGroup.SILK_OTHER_ABILITY, ItemGroup.ACT_2]),
    ItemData(ItemName.farsight, ItemClassification.useful, [ItemGroup.SILK_OTHER_ABILITY, ItemGroup.ACT_3]),
    ItemData(ItemName.everbloom, ItemClassification.progression, [ItemGroup.SILK_OTHER_ABILITY, ItemGroup.ACT_3]),

    ItemData("50 Rosaries", ItemClassification.filler, [ItemGroup.FILLER]),
    ItemData("50 Shell Shards", ItemClassification.filler, [ItemGroup.FILLER]),
]

item_data_by_name = {item.name: item for item in all_items}
item_data_by_group = {item.name: item for item in all_items}


def create_items(item_factory: SilksongItemFactory, world_options: SilksongOptions, locations_count: int, excluded_items: list[str], random: Random) -> List[Item]:
    items_to_create = []
    items_to_create.extend(choose_abilities_items(item_factory, world_options))

    for excluded_item in excluded_items:
        if excluded_item in items_to_create:
            items_to_create.remove(excluded_item)

    number_items = len(items_to_create)
    number_filler = locations_count - number_items

    items_to_create.extend(choose_fillers_and_traps(item_factory, world_options, number_filler, random))

    return [item_factory(item) for item in items_to_create]


def choose_abilities_items(item_factory: SilksongItemFactory, world_options: SilksongOptions) -> List[str]:
    abilities_items = []
    abilities_items.extend(item_names_by_groups[ItemGroup.SONG])
    abilities_items.extend(item_names_by_groups[ItemGroup.BIND])
    if world_options.shuffle_movement_abilities == ShuffleMovementAbilities.option_true:
        abilities_items.extend(item_names_by_groups[ItemGroup.MOVEMENT_ABILITY])
    abilities_items.extend(item_names_by_groups[ItemGroup.SILK_COMBAT_ABILITY])
    abilities_items.extend(item_names_by_groups[ItemGroup.COMBAT_ABILITY])
    abilities_items.extend(choose_other_abilities_items())
    return abilities_items


def choose_other_abilities_items():
    other_abilities_items = []
    other_abilities_items.append("Silk Heart")
    other_abilities_items.append("Silk Heart")
    other_abilities_items.append("Silk Heart")
    other_abilities_items.append("Sylphsong")
    other_abilities_items.append("Farsight")
    other_abilities_items.append("Everbloom")
    return other_abilities_items


def choose_fillers_and_traps(item_factory: SilksongItemFactory, world_options: SilksongOptions, number_filler: int, random: Random) -> List[str]:
    valid_filler_names = []
    valid_filler_names.extend(item_names_by_groups[ItemGroup.FILLER])
    # valid_filler_names.extend(item_names_by_groups[ItemGroup.TRAP])

    chosen_filler = random.choices(valid_filler_names, k=number_filler)

    return chosen_filler
