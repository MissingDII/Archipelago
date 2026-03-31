from typing import List

from BaseClasses import MultiWorld
from .data.items_locations_data import all_locations_items_pairs
from .items.items import SilksongItem
from .locations import SilksongLocation, LocationGroup
from .options.options import Goal, SilksongOptions


def get_event_location_name(location_name: str) -> str:
    if location_name.startswith("[Event] "):
        return location_name
    return f"[Event] {location_name}"


def create_events(multiworld: MultiWorld, player: int, enabled_locations: List[str], options: SilksongOptions):

    allowed_acts = [LocationGroup.ACT_1]
    if options.goal >= Goal.option_weaver_queen:
        allowed_acts.append(LocationGroup.ACT_2)
        if options.goal >= Goal.option_sister_of_the_void:
            allowed_acts.append(LocationGroup.ACT_3)

    for loc_item_pair in all_locations_items_pairs:
        if loc_item_pair.location_name in enabled_locations:
            continue
        if loc_item_pair.item_data is None:
            continue
        if not any([act in loc_item_pair.location_data.groups for act in allowed_acts]):
            continue

        region = multiworld.get_region(loc_item_pair.location_data.region, player)
        region.add_event(get_event_location_name(loc_item_pair.location_name), loc_item_pair.item_data.name, None, SilksongLocation, SilksongItem, show_in_spoiler=True)