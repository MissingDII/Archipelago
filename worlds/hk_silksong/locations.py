import enum
from random import Random
from typing import List, Dict, Optional, Protocol

from BaseClasses import Location
from .options.options import ShuffleMovementAbilities, SilksongOptions
from .strings.generic_strings import GAME_NAME
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
    EVA = enum.auto()
    SHARDS = enum.auto()
    ROSARIES = enum.auto()


locations_by_id: Dict[int, str] = dict()
locations_by_name: Dict[str, int] = dict()
location_names_by_groups: Dict[LocationGroup, List[str]] = dict()


class LocationData:
    id: int
    name: str
    region: str
    groups: List[LocationGroup]

    def __init__(self, name: str, region: str, groups: List[LocationGroup]):
        if name in locations_by_name:
            self.id = locations_by_name[name]
        else:
            self.id = len(locations_by_name) + 1
        self.name = name
        self.region = region
        self.groups = groups
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
    LocationData("Ring The Bell In The Marrow", RegionName.marrow, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    LocationData("Ring The Bell In Far Fields", RegionName.far_fields, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    LocationData("Ring The Bell In Greymoor", RegionName.greymoor, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    LocationData("Ring The Bell In Bellhart", RegionName.bellhart, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    LocationData("Ring The Bell In Shellwood", RegionName.shellwood, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),

    LocationData("Ring The Bell In The Marrow", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    LocationData("Search: Silent Halls", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    LocationData("Ascend: Pharloom's Crown", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    LocationData("Learn: Conductor's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2]),
    LocationData("Learn: Architect's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2]),
    LocationData("Learn: Vaultkeeper's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2]),
    LocationData("Defeat Grand Mother Silk", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),

    LocationData("Seek: After The Fall", RegionName.choral_chambers, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Seek: Awaiting The End", RegionName.moss_grotto, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Defeat Bell Eater", RegionName.choral_chambers, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Seek: The Dark Below", RegionName.abyss, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Ascend: Return To Pharloom", RegionName.abyss, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Seek: Spell Seeker", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Seek: The Old Hearts", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Defeat Crust King Khann", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Nyleth", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Skarrsinger Karmelita", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Clover Dancers", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    LocationData("Defeat Lost Lace", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),

    LocationData("Weaver Spire: Silkspear", RegionName.bone_bottom, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_1]),
    LocationData("Defeat Phantom", RegionName.mist, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Weaver Spire: Thread Storm", RegionName.greymoor, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_1]),
    LocationData("Weaver Spire: Sharpdart", RegionName.wormways, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_2]),
    LocationData("Defeat First Sinner", RegionName.the_slab, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Acquire Pale Nails", RegionName.cradle, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_3]),

    LocationData("Grant Flexile Spines", RegionName.far_fields, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_1]),
    LocationData("Weaver Spire: Cling Grip", RegionName.shellwood, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_1]),
    LocationData("Weaver Spire: Swift Step", RegionName.deep_docks, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_1]),
    LocationData("Acquire Faydown Cloak", RegionName.mount_fay, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_2]),
    LocationData("Weaver Spire: Clawline", RegionName.underworks, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_2]),
    LocationData("Weaver Spire: Silk Soar", RegionName.abyss, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_3]),

    LocationData("Learn Needle Strike", RegionName.blasted_steps, [LocationGroup.COMBAT_ABILITY, LocationGroup.ACT_1]),

    LocationData("Defeat Bell Beast", RegionName.bone_bottom, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    LocationData("Defeat The Unravelled", RegionName.whiteward, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Defeat Lace (Cradle)", RegionName.cradle, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    LocationData("Eva: 32 Slots", RegionName.weavenest_atla, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.EVA, LocationGroup.ACT_2]),
    LocationData("Seek: The Old Hearts", RegionName.bone_bottom, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    LocationData("Pickup Farsight", RegionName.weavenest_atla, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.PICKUP, LocationGroup.ACT_3]),
]

location_data_by_name = {location.name: location for location in all_locations}


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

    for group in enabled_groups:
        randomized_location_names.extend(location_names_by_groups[group])

    randomized_location_names = sorted(list(set(randomized_location_names)))

    for location_name in randomized_location_names:
        location_data = location_data_by_name[location_name]
        location_collector(location_data.name, location_data.id, location_data.region)