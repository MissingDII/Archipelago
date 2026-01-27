from typing import List

from BaseClasses import MultiWorld
from . import locations_items_pairs_by_name, SilksongItem
from .locations import SilksongLocation


def get_event_location_name(location_name: str) -> str:
    return f"Event: {location_name}"


def create_events(multiworld: MultiWorld, player: int, enabled_locations: List[str]):

    for loc_item_pair in locations_items_pairs_by_name:
        if loc_item_pair.location_name in enabled_locations:
            continue
        if loc_item_pair.item is None:
            continue
        region = multiworld.get_region(loc_item_pair.region, player)
        region.add_event(get_event_location_name(loc_item_pair.location_name), loc_item_pair.item.name, None, SilksongLocation, SilksongItem, show_in_spoiler=True)