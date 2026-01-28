import enum
from random import Random
from typing import List, Dict, Optional, Protocol

from BaseClasses import Location
from .options.options import ShuffleMovementAbilities, SilksongOptions
from .strings.generic_strings import GAME_NAME
from .strings.goal_names import GoalName
from .strings.region_names import RegionName


class SilksongLocationCollector(Protocol):
    def __call__(self, name: str, code: Optional[int], region: str) -> None:
        raise NotImplementedError


class LocationGroup(enum.Enum):
    ACT_1 = enum.auto()
    ACT_2 = enum.auto()
    ACT_3 = enum.auto()
    ALWAYS_ACTIVE = enum.auto()
    SONG = enum.auto()
    OBJECTIVE = enum.auto()
    MOVEMENT_ABILITY = enum.auto()
    SILK_COMBAT_ABILITY = enum.auto()
    SILK_OTHER_ABILITY = enum.auto()
    COMBAT_ABILITY = enum.auto()
    BOSS_FIGHT = enum.auto()
    CREST_UPGRADE = enum.auto
    EVA = enum.auto()
    EVA_EXTRA_LOCATIONS = enum.auto()
    MEMORY_LOCKET = enum.auto()
    SHOP = enum.auto()
    WISH = enum.auto()
    RED_TOOL = enum.auto()
    YELLOW_TOOL = enum.auto()
    BLUE_TOOL = enum.auto()
    PALE_OIL = enum.auto()
    CREST = enum.auto()
    RANDOMIZED_STARTING_CREST = enum.auto()

    RANDOMIZED_SLASH = enum.auto()
    RANDOMIZED_BIND = enum.auto()

    UNIQUE_PICKUPS = enum.auto()
    PICKUP = enum.auto()

    SHARDS = enum.auto()
    ROSARIES = enum.auto()
    GOAL = enum.auto()


locations_by_id: Dict[int, str] = dict()
locations_by_name: Dict[str, int] = dict()
location_names_by_groups: Dict[LocationGroup, List[str]] = dict()


class LocationData:
    id: Optional[int]
    name: str
    region: str
    groups: List[LocationGroup]

    def __init__(self, name: str, region: str, groups: List[LocationGroup], is_event: bool = False):
        if is_event:
            self.id = None
        elif name in locations_by_name:
            self.id = locations_by_name[name]
        else:
            self.id = len(locations_by_name) + 1
        self.name = name
        self.region = region
        self.groups = groups
        if not is_event:
            locations_by_name[self.name] = self.id
            locations_by_id[self.id] = self.name
        for group in self.groups:
            if group not in location_names_by_groups:
                location_names_by_groups[group] = []
            location_names_by_groups[group].append(self.name)


class SilksongLocation(Location):
    game: str = GAME_NAME


goal_events_locations = [
    LocationData(GoalName.fanatic, RegionName.bellhart_saved, [LocationGroup.GOAL], True),
    LocationData(GoalName.act_1, RegionName.grand_gate, [LocationGroup.GOAL], True),
    LocationData(GoalName.weaver_queen, RegionName.cradle, [LocationGroup.GOAL], True),
    LocationData(GoalName.snared_silk, RegionName.cradle_with_soul_snare, [LocationGroup.GOAL], True),
    LocationData(GoalName.flea_friend, RegionName.fleatopia, [LocationGroup.GOAL], True),
    LocationData(GoalName.sister_of_the_void, RegionName.abyss, [LocationGroup.GOAL], True),
    LocationData(GoalName.completion, RegionName.abyss, [LocationGroup.GOAL], True),
]


def create_locations(location_collector: SilksongLocationCollector,
                     options: SilksongOptions, all_locations_items_pairs,
                     random: Random):
    randomized_locations = []

    enabled_groups = []
    enabled_groups.append(LocationGroup.ALWAYS_ACTIVE)
    enabled_groups.append(LocationGroup.OBJECTIVE)
    if options.shuffle_movement_abilities == ShuffleMovementAbilities.option_true:
        enabled_groups.append(LocationGroup.MOVEMENT_ABILITY)
    enabled_groups.append(LocationGroup.COMBAT_ABILITY)
    enabled_groups.append(LocationGroup.SILK_COMBAT_ABILITY)
    enabled_groups.append(LocationGroup.SILK_OTHER_ABILITY)
    enabled_groups.append(LocationGroup.BOSS_FIGHT)
    enabled_groups.append(LocationGroup.SONG)
    enabled_groups.append(LocationGroup.EVA)
    # enabled_groups.append(LocationGroup.EVA_EXTRA_LOCATIONS)
    enabled_groups.append(LocationGroup.MEMORY_LOCKET)
    enabled_groups.append(LocationGroup.WISH)
    enabled_groups.append(LocationGroup.CREST)

    for loc_item_pair in all_locations_items_pairs:
        for group in enabled_groups:
            if group in loc_item_pair.location_data.groups:
                randomized_locations.append(loc_item_pair.location_data)
                break

    # randomized_locations = sorted(list(set(randomized_locations)))

    for location_data in randomized_locations:
        location_collector(location_data.name, location_data.id, location_data.region)