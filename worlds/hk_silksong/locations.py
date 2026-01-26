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
    PICKUP = enum.auto()
    CREST_UPGRADE = enum.auto
    EVA = enum.auto()
    EVA_EXTRA_LOCATIONS = enum.auto()
    MEMORY_LOCKET = enum.auto()
    SHOP = enum.auto()
    WISH = enum.auto()
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


all_locations = [
    LocationData("Escape Moss Grotto", RegionName.bone_bottom, [LocationGroup.ALWAYS_ACTIVE, LocationGroup.ACT_1]),

    LocationData("Save: The Threadspun Town", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    LocationData("Seek: The Great Citadel", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    LocationData("Ring The Bell In The Marrow", RegionName.marrow_bellway, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    LocationData("Ring The Bell In Deep Docks", RegionName.deep_docks_bell, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    LocationData("Ring The Bell In Greymoor", RegionName.greymoor_craw_lake, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    LocationData("Ring The Bell In Bellhart", RegionName.bellhart, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    LocationData("Ring The Bell In Shellwood", RegionName.shellwood, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),

    LocationData("Ring The Bell In The Marrow", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    LocationData("Search: Silent Halls", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    LocationData("Ascend: Pharloom's Crown", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    LocationData("Learn: Conductor's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2]),
    LocationData("Learn: Architect's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2]),
    LocationData("Learn: Vaultkeeper's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2]),

    LocationData("Seek: After The Fall", RegionName.choral_chambers, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Seek: Awaiting The End", RegionName.moss_grotto, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Seek: The Dark Below", RegionName.abyss, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Ascend: Return To Pharloom", RegionName.abyss, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Seek: Spell Seeker", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Seek: The Old Hearts", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),

    LocationData("Weaver Spire: Silkspear", RegionName.bone_bottom, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_1]),
    LocationData("Weaver Spire: Thread Storm", RegionName.greymoor_craw_lake, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_1]),
    LocationData("Weaver Spire: Sharpdart", RegionName.weavenest_karn, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_2]),
    LocationData("Acquire Pale Nails", RegionName.cradle, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_3]),

    LocationData("Grant Flexile Spines", RegionName.far_fields_seamstress, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_1]),
    LocationData("Weaver Spire: Cling Grip", RegionName.shellwood, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_1]),
    LocationData("Weaver Spire: Swift Step", RegionName.deep_docks_swift_step, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_1]),
    LocationData("Acquire Faydown Cloak", RegionName.mount_fay, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_2]),
    LocationData("Weaver Spire: Clawline", RegionName.underworks, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_2]),
    LocationData("Weaver Spire: Silk Soar", RegionName.abyss, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_3]),

    LocationData("Learn Needle Strike", RegionName.blasted_steps, [LocationGroup.COMBAT_ABILITY, LocationGroup.ACT_1]),

    LocationData("Seek: The Old Hearts", RegionName.bone_bottom, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Pickup Farsight", RegionName.weavenest_atla, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.PICKUP, LocationGroup.ACT_3]),

    LocationData("Defeat Moss Mother", RegionName.moss_grotto, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Bell Beast", RegionName.marrow_bellway, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Lace", RegionName.deep_docks_lace, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Fourth Chorus", RegionName.far_fields_fourth_chorus, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Moorwing", RegionName.greymoor_spires, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Sister Splinter", RegionName.shellwood, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Widow", RegionName.bellhart_upper, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Great Conchflies", RegionName.blasted_steps, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Last Judge", RegionName.blasted_steps_grand_gate, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Cogwork Dancers", RegionName.cogwork_core, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Trobbio", RegionName.choral_chambers, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Tormented Trobbio", RegionName.choral_chambers_act_3, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Groal the Great", RegionName.bilewater_upper, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat The Unraveled", RegionName.whiteward, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Disgraced Chef Lugoli", RegionName.sinners_road, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Craggler", RegionName.craggler_cavern, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Father of the Flame", RegionName.wisp_thicket, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Voltvyrm", RegionName.sands_of_karak, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Second Sentinel", RegionName.high_halls, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Broodmother", RegionName.the_slab, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Plasmified Zango", RegionName.wormways_plasmium, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Shrine Guardian Seth", RegionName.grand_gate, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Palestag", RegionName.verdania, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Lost Garmond", RegionName.blasted_steps_act_3, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Pinstress", RegionName.mount_fay_act_3, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Gurr the Outcast", RegionName.far_fields_fields, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Watcher at the Edge", RegionName.sands_of_karak, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Crawfather", RegionName.greymoor_craw_lake, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    # LocationData("Defeat Summoned Savior", RegionName., [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Shakra", RegionName.greymoor_spires, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Garmond and Zaza", RegionName.choral_chambers_outside, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),

    LocationData("Defeat Savage Beastfly (Beast)", RegionName.chapel_of_beast, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Savage Beastfly (Wish)", RegionName.far_fields_beastfly, [LocationGroup.WISH, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),

    LocationData("Defeat Skull Tyrant (Wish)", RegionName.marrow_east, [LocationGroup.WISH, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat Skull Tyrant (Bone Bottom)", RegionName.bone_bottom, [LocationGroup.WISH, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),

    LocationData("Defeat Phantom", RegionName.exhaust_organ, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),

    LocationData("Defeat Raging Conchfly", RegionName.sands_of_karak, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat First Sinner", RegionName.the_slab, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat The Unravelled", RegionName.whiteward, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Lace (Cradle)", RegionName.cradle, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Grand Mother Silk", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),

    LocationData("Defeat Bell Eater", RegionName.choral_chambers, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Crust King Khann", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Nyleth", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Skarrsinger Karmelita", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Clover Dancers", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Lost Lace", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),

    LocationData("Eva: 0 Slots", RegionName.weavenest_atla, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 1 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 2 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 3 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 4 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 5 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 6 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 7 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 8 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 9 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 10 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 11 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 12 Slots", RegionName.weavenest_atla, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 13 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 14 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 15 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 16 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 17 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 18 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 19 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 20 Slots", RegionName.weavenest_atla, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA, LocationGroup.ACT_1]),
    LocationData("Eva: 21 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 22 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 23 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 24 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 25 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 26 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 27 Slots", RegionName.weavenest_atla, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 28 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 29 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 30 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 31 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 32 Slots", RegionName.weavenest_atla, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 33 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 34 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 35 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Eva: 36 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    LocationData("Eva: 37 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    LocationData("Eva: 38 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    LocationData("Eva: 39 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    LocationData("Eva: 40 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),

    LocationData("Memory locket - Chapel of the Beast", RegionName.chapel_of_beast, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1]),
    LocationData("Memory locket - Mort", RegionName.far_fields_pilgrims_rest, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_1]),
    # LocationData("Memory locket - Grindle", RegionName.blasted_steps_grindle_shop_act_3, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_3]),
    LocationData("Memory locket - Greymoor", RegionName.greymoor_bellway, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_1]),
    LocationData("Memory locket - Volatiles FlintBeetles", RegionName.marrow_west, [LocationGroup.MEMORY_LOCKET, LocationGroup.WISH, LocationGroup.ACT_1]),
    # LocationData("Memory locket - Survivor's Camp", RegionName.marrow_west, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_3]),
    LocationData("Memory locket - The Marrow", RegionName.marrow_bellway_north_alcove, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1]),
    LocationData("Memory locket - Wormways", RegionName.wormways_bottom_left, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1]),
    LocationData("Memory locket - Frey", RegionName.bellhart_saved, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_1]),
    LocationData("Memory locket - Blasted Steps", RegionName.blasted_steps, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1]),
    LocationData("Memory locket - Bilewater", RegionName.bilewater_bellway, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1]),
    LocationData("Memory locket - Choral Chambers", RegionName.choral_chambers_above_bellway, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    LocationData("Memory locket - Underworks", RegionName.underworks_confessional, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    LocationData("Memory locket - Deep Docks", RegionName.deep_docks_diving_bell, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    LocationData("Memory locket - Whispering Vaults", RegionName.whispering_vaults_east, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    LocationData("Memory locket - Sands of Karak", RegionName.sands_of_karak, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    LocationData("Memory locket - Greymoor", RegionName.halfway_home_alcove, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    LocationData("Memory locket - Memorium", RegionName.memorium, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    LocationData("Memory locket - The Slab", RegionName.the_slab_shortcut_cave, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    LocationData("Memory locket - Bilewater Upper", RegionName.bilewater_upper, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    LocationData("Memory locket - Bellhart Ceiling", RegionName.bellhart, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_3]),
    LocationData("Memory locket - Far Fields East", RegionName.far_fields_fields, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_3]),

]


events_locations = [
    LocationData(GoalName.fanatic, RegionName.bellhart_saved, [LocationGroup.GOAL], True),
    LocationData(GoalName.act_1, RegionName.grand_gate, [LocationGroup.GOAL], True),
    LocationData(GoalName.weaver_queen, RegionName.cradle, [LocationGroup.GOAL], True),
    LocationData(GoalName.snared_silk, RegionName.cradle, [LocationGroup.GOAL], True),
    LocationData(GoalName.flea_friend, RegionName.fleatopia, [LocationGroup.GOAL], True),
    LocationData(GoalName.sister_of_the_void, RegionName.abyss, [LocationGroup.GOAL], True),
    LocationData(GoalName.completion, RegionName.abyss, [LocationGroup.GOAL], True),
]

location_data_by_name = {location.name: location for location in all_locations + events_locations}


def create_locations(location_collector: SilksongLocationCollector,
                     options: SilksongOptions,
                     random: Random):
    randomized_location_names = []

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
    enabled_groups.append(LocationGroup.EVA_EXTRA_LOCATIONS)
    enabled_groups.append(LocationGroup.MEMORY_LOCKET)

    for group in enabled_groups:
        randomized_location_names.extend(location_names_by_groups[group])

    randomized_location_names = sorted(list(set(randomized_location_names)))

    for location_name in randomized_location_names:
        location_data = location_data_by_name[location_name]
        location_collector(location_data.name, location_data.id, location_data.region)