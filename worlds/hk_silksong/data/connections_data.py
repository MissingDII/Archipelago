from ..strings.entrance_names import EntranceName
from ..strings.region_names import RegionName


class ConnectionData:
    origin: str
    destination: str
    entrance: str

    def __init__(self, origin: str, destination: str, entrance: str = ""):
        self.origin = origin
        self.destination = destination
        self.entrance = entrance if entrance else ""


all_connections = [
    ConnectionData(RegionName.menu, RegionName.moss_grotto, EntranceName.spawn_moss_grotto),
    ConnectionData(RegionName.moss_grotto, RegionName.bone_bottom),
    ConnectionData(RegionName.bone_bottom, RegionName.weavenest_atla),
    ConnectionData(RegionName.bone_bottom, RegionName.wormways),
    ConnectionData(RegionName.bone_bottom, RegionName.marrow),
    ConnectionData(RegionName.marrow, RegionName.deep_docks),
    ConnectionData(RegionName.deep_docks, RegionName.far_fields),
    ConnectionData(RegionName.far_fields, RegionName.greymoor),
    ConnectionData(RegionName.greymoor, RegionName.bellhart),
    ConnectionData(RegionName.greymoor, RegionName.sinners_road),
    ConnectionData(RegionName.sinners_road, RegionName.bilewater),
    ConnectionData(RegionName.bilewater, RegionName.mist),
    ConnectionData(RegionName.bellhart, RegionName.shellwood),
    ConnectionData(RegionName.shellwood, RegionName.blasted_steps),
    ConnectionData(RegionName.blasted_steps, RegionName.sands_of_karak),
    ConnectionData(RegionName.blasted_steps, RegionName.grand_gate),
    ConnectionData(RegionName.grand_gate, RegionName.underworks),
    ConnectionData(RegionName.mist, RegionName.underworks),
    ConnectionData(RegionName.underworks, RegionName.choral_chambers),
    ConnectionData(RegionName.choral_chambers, RegionName.whiteward),
    ConnectionData(RegionName.choral_chambers, RegionName.cogwork_core),
    ConnectionData(RegionName.choral_chambers, RegionName.memorium),
    ConnectionData(RegionName.choral_chambers, RegionName.cradle),
    ConnectionData(RegionName.choral_chambers, RegionName.high_halls),
    ConnectionData(RegionName.choral_chambers, RegionName.the_slab),
    ConnectionData(RegionName.cogwork_core, RegionName.whispering_vaults),
    ConnectionData(RegionName.the_slab, RegionName.mount_fay),
    ConnectionData(RegionName.deep_docks, RegionName.abyss),

    ConnectionData(RegionName.choral_chambers, RegionName.citadel),
    ConnectionData(RegionName.grand_gate, RegionName.citadel),
    ConnectionData(RegionName.whispering_vaults, RegionName.citadel),
    ConnectionData(RegionName.high_halls, RegionName.citadel),
    ConnectionData(RegionName.memorium, RegionName.citadel),
    ConnectionData(RegionName.cogwork_core, RegionName.citadel),
    ConnectionData(RegionName.whiteward, RegionName.citadel),
]