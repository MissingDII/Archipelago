from typing import List, Optional, Dict

from ..strings.entrance_names import EntranceName
from ..strings.item_names import ItemName
from ..strings.region_names import RegionName


class ConnectionData:
    origin: str
    destination: str
    entrance: str
    requirements: Optional[List[str]]

    def __init__(self, origin: str, destination: str, entrance: str = "", requirements: Optional[List[str]] | str = None):
        self.origin = origin
        self.destination = destination
        self.entrance = entrance if entrance else ""
        if isinstance(requirements, str):
            requirements = [requirements]
        self.requirements = requirements


all_connections = [
    ConnectionData(RegionName.menu, RegionName.moss_grotto, EntranceName.spawn_moss_grotto),
    ConnectionData(RegionName.moss_grotto, RegionName.bone_bottom),
    ConnectionData(RegionName.bone_bottom, RegionName.weavenest_atla),
    ConnectionData(RegionName.bone_bottom, RegionName.wormways),
    ConnectionData(RegionName.bone_bottom, RegionName.marrow_west),
    ConnectionData(RegionName.wormways, RegionName.wormways_plasmium),
    ConnectionData(RegionName.marrow_west, RegionName.marrow_bellway, requirements=ItemName.silkspear),
    ConnectionData(RegionName.marrow_bellway, RegionName.marrow_east),
    ConnectionData(RegionName.marrow_east, RegionName.deep_docks),
    ConnectionData(RegionName.marrow_east, RegionName.hunters_march),
    ConnectionData(RegionName.hunters_march, RegionName.chapel_of_beast),
    ConnectionData(RegionName.deep_docks, RegionName.far_fields),
    ConnectionData(RegionName.far_fields, RegionName.greymoor),
    ConnectionData(RegionName.greymoor, RegionName.bellhart),
    ConnectionData(RegionName.greymoor, RegionName.sinners_road),
    ConnectionData(RegionName.greymoor, RegionName.wisp_thicket),
    ConnectionData(RegionName.greymoor, RegionName.verdania),
    ConnectionData(RegionName.sinners_road, RegionName.bilewater),
    ConnectionData(RegionName.bilewater, RegionName.mist),
    ConnectionData(RegionName.bilewater, RegionName.bilewater_upper),
    ConnectionData(RegionName.bellhart, RegionName.shellwood),
    ConnectionData(RegionName.shellwood, RegionName.bellhart_upper),
    ConnectionData(RegionName.shellwood, RegionName.blasted_steps),
    ConnectionData(RegionName.blasted_steps, RegionName.sands_of_karak),
    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_grand_gate),
    ConnectionData(RegionName.blasted_steps_grand_gate, RegionName.grand_gate),
    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_act_3),
    ConnectionData(RegionName.grand_gate, RegionName.underworks),
    ConnectionData(RegionName.mist, RegionName.underworks),
    ConnectionData(RegionName.underworks, RegionName.choral_chambers),
    ConnectionData(RegionName.choral_chambers, RegionName.whiteward),
    ConnectionData(RegionName.choral_chambers, RegionName.cogwork_core),
    ConnectionData(RegionName.choral_chambers, RegionName.memorium),
    ConnectionData(RegionName.choral_chambers, RegionName.cradle),
    ConnectionData(RegionName.choral_chambers, RegionName.high_halls),
    ConnectionData(RegionName.choral_chambers, RegionName.the_slab),
    ConnectionData(RegionName.choral_chambers, RegionName.choral_chambers_act_3),
    ConnectionData(RegionName.cogwork_core, RegionName.whispering_vaults),
    ConnectionData(RegionName.the_slab, RegionName.mount_fay),
    ConnectionData(RegionName.mount_fay, RegionName.mount_fay_act_3),
    ConnectionData(RegionName.deep_docks, RegionName.abyss),

    ConnectionData(RegionName.choral_chambers, RegionName.citadel),
    ConnectionData(RegionName.grand_gate, RegionName.citadel),
    ConnectionData(RegionName.whispering_vaults, RegionName.citadel),
    ConnectionData(RegionName.high_halls, RegionName.citadel),
    ConnectionData(RegionName.memorium, RegionName.citadel),
    ConnectionData(RegionName.cogwork_core, RegionName.citadel),
    ConnectionData(RegionName.whiteward, RegionName.citadel),
]

connections_by_name: Dict[str, ConnectionData] = {(connection.entrance if connection.entrance else f"{connection.origin} -> {connection.destination}"): connection for connection in all_connections}