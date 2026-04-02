import enum
from random import Random
from typing import List, Dict, Optional, Protocol

from BaseClasses import Location, MultiWorld
from .options.options import SilksongOptions, Goal, RandomizeMovementAbilities, RandomizeCombatAbilities, RandomizeOtherAbilities, RandomizeBossRewards, \
    RandomizeEvaRewards, RandomizeMemoryLockets, RandomizeWishRewards, RandomizeCrests, RandomStartingCrest, RandomizeShopItems, RandomizePickups, \
    RandomizeLostFleas, RandomizeStations, RandomizeNeedleUpgrades, StartingBind, StartingSlashes
from .strings.generic_strings import GAME_NAME
from .strings.goal_names import GoalName
from .strings.item_names import ItemName
from .strings.region_names import RegionName
from ..generic.Rules import forbid_item


class SilksongLocationCollector(Protocol):
    def __call__(self, name: str, code: Optional[int], region: str) -> None:
        raise NotImplementedError


class LocationGroup(enum.Enum):
    EVENT_ONLY = enum.auto()
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
    CREST_UPGRADE = enum.auto()
    EVA = enum.auto()
    EVA_REWARD = enum.auto()
    EVA_EXTRA_LOCATIONS = enum.auto()
    MEMORY_LOCKET = enum.auto()
    SHOP = enum.auto()
    WISH = enum.auto()
    RED_TOOL = enum.auto()
    YELLOW_TOOL = enum.auto()
    BLUE_TOOL = enum.auto()
    PALE_OIL = enum.auto()
    CREST = enum.auto()
    SPOOL_FRAGMENT = enum.auto()
    LOST_FLEA = enum.auto()
    BELLWAY = enum.auto()
    VENTRICA = enum.auto()
    NEEDLE_UPGRADE = enum.auto()

    UNIQUE_PICKUPS = enum.auto()
    PICKUP = enum.auto()

    RANDOMIZED_STARTING_CREST = enum.auto()
    RANDOMIZED_SLASH = enum.auto()
    RANDOMIZED_BIND = enum.auto()

    SHARDS = enum.auto()
    ROSARIES = enum.auto()
    GOAL = enum.auto()


locations_by_id: Dict[int, str] = dict()
locations_by_name: Dict[str, int] = dict()
location_names_by_groups: Dict[LocationGroup, List[str]] = dict()


def generate_id(name: str) -> int:
    id = 0
    for char in name:
        id = id * 26
        id += (ord(char.lower()) - 96)
    id = id % 1125899906842624
    return id


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
            self.id = generate_id(name)
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
    enabled_groups.append(LocationGroup.SONG)

    if options.randomize_movement_abilities == RandomizeMovementAbilities.option_true:
        enabled_groups.append(LocationGroup.MOVEMENT_ABILITY)

    if options.randomize_combat_abilities == RandomizeCombatAbilities.option_true:
        enabled_groups.append(LocationGroup.COMBAT_ABILITY)
        enabled_groups.append(LocationGroup.SILK_COMBAT_ABILITY)

    if options.randomize_other_abilities == RandomizeOtherAbilities.option_true:
        enabled_groups.append(LocationGroup.SILK_OTHER_ABILITY)

    if options.randomize_needle_upgrades == RandomizeNeedleUpgrades.option_true:
        enabled_groups.append(LocationGroup.NEEDLE_UPGRADE)

    if options.starting_bind == StartingBind.option_false:
        enabled_groups.append(LocationGroup.RANDOMIZED_BIND)

    if options.starting_slashes != StartingSlashes.option_all:
        enabled_groups.append(LocationGroup.RANDOMIZED_SLASH)

    if options.randomize_boss_rewards == RandomizeBossRewards.option_true:
        enabled_groups.append(LocationGroup.BOSS_FIGHT)

    if options.randomize_eva_rewards != RandomizeEvaRewards.option_none:
        enabled_groups.append(LocationGroup.EVA_REWARD)
        if options.randomize_eva_rewards == RandomizeEvaRewards.option_evasanity:
            enabled_groups.append(LocationGroup.EVA_EXTRA_LOCATIONS)

    if options.randomize_memory_lockets == RandomizeMemoryLockets.option_true:
        enabled_groups.append(LocationGroup.MEMORY_LOCKET)

    if options.randomize_wish_rewards == RandomizeWishRewards.option_true:
        enabled_groups.append(LocationGroup.WISH)

    if options.randomize_crests == RandomizeCrests.option_true:
        enabled_groups.append(LocationGroup.CREST)
        enabled_groups.append(LocationGroup.CREST_UPGRADE)

    if options.random_starting_crests == RandomStartingCrest.option_true:
        enabled_groups.append(LocationGroup.RANDOMIZED_STARTING_CREST)

    if options.randomize_shop_items == RandomizeShopItems.option_true:
        enabled_groups.append(LocationGroup.SHOP)

    if options.randomize_pickups != RandomizePickups.option_none:
        enabled_groups.append(LocationGroup.UNIQUE_PICKUPS)
        if options.randomize_pickups == RandomizePickups.option_all:
            enabled_groups.append(LocationGroup.PICKUP)

    if options.randomize_lost_fleas == RandomizeLostFleas.option_true:
        enabled_groups.append(LocationGroup.LOST_FLEA)

    if options.randomize_stations == RandomizeStations.option_true:
        enabled_groups.append(LocationGroup.BELLWAY)
        enabled_groups.append(LocationGroup.VENTRICA)

    allowed_acts = [LocationGroup.ACT_1]
    if options.goal >= Goal.option_weaver_queen:
        allowed_acts.append(LocationGroup.ACT_2)
        if options.goal >= Goal.option_sister_of_the_void:
            allowed_acts.append(LocationGroup.ACT_3)

    for loc_item_pair in all_locations_items_pairs:
        if not any([act in loc_item_pair.location_data.groups for act in allowed_acts]):
            continue
        for group in enabled_groups:
            if group in loc_item_pair.location_data.groups:
                randomized_locations.append(loc_item_pair.location_data)
                break

    # randomized_locations = sorted(list(set(randomized_locations)))

    for location_data in randomized_locations:
        location_collector(location_data.name, location_data.id, location_data.region)


def set_item_rules(multiworld: MultiWorld, player: int, enabled_locations: List[str]) -> None:
    # These can end a chain of lockets, so they can self-lock if placed there
    set_item_rule(multiworld, player, enabled_locations, "Eva: 17 Slots", ItemName.memory_locket)
    set_item_rule(multiworld, player, enabled_locations, "Eva: 32 Slots", ItemName.memory_locket)
    set_item_rule(multiworld, player, enabled_locations, "Eva: 37 Slots", ItemName.memory_locket)


def set_item_rule(multiworld: MultiWorld, player: int, enabled_locations: List[str], location_name: str, forbidden_item: str = None):
    if location_name not in enabled_locations:
        return
    location = multiworld.get_location(location_name, player)
    if forbidden_item:
        forbid_item(location, forbidden_item, player)