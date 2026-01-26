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
    ConnectionData(RegionName.bone_bottom, RegionName.weavenest_atla, requirements=ItemName.needolin),
    ConnectionData(RegionName.bone_bottom, RegionName.craggler_cavern, requirements=ItemName.swift_step),
    ConnectionData(RegionName.bone_bottom, RegionName.marrow_west),

    ConnectionData(RegionName.craggler_cavern, RegionName.wormways_entrance), # Add Simple Key Requirement
    ConnectionData(RegionName.wormways_entrance, RegionName.wormways_bottom_left, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.wormways_entrance, RegionName.weavenest_karn, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.wormways_entrance, RegionName.wormways_plasmium),

    ConnectionData(RegionName.marrow_west, RegionName.marrow_bellway, requirements=ItemName.silkspear),
    ConnectionData(RegionName.marrow_bellway, RegionName.marrow_east),
    ConnectionData(RegionName.marrow_bellway, RegionName.marrow_bellway_north_alcove, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.marrow_east, RegionName.deep_docks_entrance),
    ConnectionData(RegionName.marrow_east, RegionName.hunters_march),
    ConnectionData(RegionName.hunters_march, RegionName.chapel_of_beast),
    ConnectionData(RegionName.deep_docks_entrance, RegionName.deep_docks_swift_step),
    ConnectionData(RegionName.deep_docks_entrance, RegionName.deep_docks_forge_daughter),
    ConnectionData(RegionName.deep_docks_entrance, RegionName.deep_docks_lace, requirements=ItemName.swift_step),
    ConnectionData(RegionName.deep_docks_lace, RegionName.deep_docks_bell),
    ConnectionData(RegionName.deep_docks_bell, RegionName.far_fields_entrance),
    ConnectionData(RegionName.deep_docks_forge_daughter, RegionName.deep_docks_diving_bell, requirements=ItemName.clawline),
    ConnectionData(RegionName.far_fields_entrance, RegionName.far_fields_pilgrims_rest),
    ConnectionData(RegionName.far_fields_entrance, RegionName.far_fields_seamstress),
    ConnectionData(RegionName.far_fields_seamstress, RegionName.far_fields_east),
    ConnectionData(RegionName.far_fields_pilgrims_rest, RegionName.far_fields_climb, requirements=ItemName.drifters_cloak),
    ConnectionData(RegionName.far_fields_seamstress, RegionName.far_fields_fourth_chorus, requirements=ItemName.drifters_cloak),
    ConnectionData(RegionName.far_fields_fourth_chorus, RegionName.far_fields_beastfly),
    ConnectionData(RegionName.far_fields_climb, RegionName.greymoor_above_far_fields),
    ConnectionData(RegionName.hunters_march, RegionName.far_fields_fields, requirements=ItemName.silk_soar),
    ConnectionData(RegionName.greymoor_above_far_fields, RegionName.greymoor_craw_lake),
    ConnectionData(RegionName.greymoor_above_far_fields, RegionName.greymoor_spires),
    ConnectionData(RegionName.greymoor_spires, RegionName.halfway_home),
    ConnectionData(RegionName.greymoor_spires, RegionName.greymoor_bellway),
    ConnectionData(RegionName.greymoor_spires, RegionName.bellhart),
    ConnectionData(RegionName.greymoor_spires, RegionName.sinners_road),
    ConnectionData(RegionName.greymoor_spires, RegionName.wisp_thicket),
    ConnectionData(RegionName.greymoor_craw_lake, RegionName.verdania),
    ConnectionData(RegionName.halfway_home, RegionName.halfway_home_alcove, requirements=ItemName.faydown_cloak),

    ConnectionData(RegionName.sinners_road, RegionName.bilewater),

    ConnectionData(RegionName.bilewater, RegionName.bilewater_bellway),
    ConnectionData(RegionName.bilewater_bellway, RegionName.mist),
    ConnectionData(RegionName.bilewater, RegionName.bilewater_upper, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.mist, RegionName.exhaust_organ, requirements=ItemName.needolin),

    ConnectionData(RegionName.bellhart, RegionName.shellwood),
    ConnectionData(RegionName.shellwood, RegionName.bellhart_upper, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.bellhart_upper, RegionName.bellhart_saved),
    ConnectionData(RegionName.shellwood, RegionName.blasted_steps, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.blasted_steps, RegionName.sands_of_karak, requirements=ItemName.clawline),
    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_grand_gate, requirements=[ItemName.swift_step, ItemName.cling_grip, ItemName.drifters_cloak]),
    ConnectionData(RegionName.blasted_steps_grand_gate, RegionName.grand_gate),
    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_act_3),
    ConnectionData(RegionName.grand_gate, RegionName.underworks),
    ConnectionData(RegionName.exhaust_organ, RegionName.underworks),
    ConnectionData(RegionName.underworks, RegionName.underworks_confessional),
    ConnectionData(RegionName.underworks, RegionName.choral_chambers_above_bellway),
    ConnectionData(RegionName.choral_chambers_above_bellway, RegionName.choral_chambers_bellway),
    ConnectionData(RegionName.choral_chambers_bellway, RegionName.choral_chambers),
    ConnectionData(RegionName.choral_chambers, RegionName.whiteward),
    ConnectionData(RegionName.choral_chambers, RegionName.cogwork_core),
    ConnectionData(RegionName.choral_chambers, RegionName.memorium, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.choral_chambers, RegionName.cradle, requirements=[ItemName.architect_melody, ItemName.vaultkeeper_melody, ItemName.conductor_melody]),
    ConnectionData(RegionName.choral_chambers, RegionName.high_halls),
    ConnectionData(RegionName.choral_chambers, RegionName.the_slab),
    ConnectionData(RegionName.choral_chambers, RegionName.choral_chambers_act_3),
    ConnectionData(RegionName.memorium, RegionName.putrified_ducts),
    ConnectionData(RegionName.putrified_ducts, RegionName.fleatopia),
    ConnectionData(RegionName.cogwork_core, RegionName.whispering_vaults),
    ConnectionData(RegionName.whispering_vaults, RegionName.whispering_vaults_east),
    ConnectionData(RegionName.whispering_vaults_east, RegionName.choral_chambers_outside),

    ConnectionData(RegionName.the_slab, RegionName.mount_fay, requirements=ItemName.clawline),
    ConnectionData(RegionName.the_slab, RegionName.the_slab_shortcut_cave, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.mount_fay, RegionName.mount_fay_act_3),
    ConnectionData(RegionName.deep_docks_forge_daughter, RegionName.abyss),

    ConnectionData(RegionName.choral_chambers, RegionName.citadel),
    ConnectionData(RegionName.grand_gate, RegionName.citadel),
    ConnectionData(RegionName.whispering_vaults, RegionName.citadel),
    ConnectionData(RegionName.high_halls, RegionName.citadel),
    ConnectionData(RegionName.memorium, RegionName.citadel),
    ConnectionData(RegionName.cogwork_core, RegionName.citadel),
    ConnectionData(RegionName.whiteward, RegionName.citadel),
]

connections_by_name: Dict[str, ConnectionData] = {(connection.entrance if connection.entrance else f"{connection.origin} -> {connection.destination}"): connection for connection in all_connections}