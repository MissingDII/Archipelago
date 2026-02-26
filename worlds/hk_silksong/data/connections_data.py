from typing import List, Optional, Dict

from ..strings.item_names import ItemName, EventName
from ..strings.region_names import RegionName


class ConnectionData:
    origin: str
    destination: str
    entrance: str
    requirements: Optional[Dict[str, int]]

    def __init__(self, origin: str, destination: str, entrance: str = "", requirements: None | List[str] | str | Dict[str, int] = None):
        self.origin = origin
        self.destination = destination
        self.entrance = entrance if entrance else ""
        if isinstance(requirements, str):
            requirements = [requirements]
        if isinstance(requirements, list):
            requirements_dict = dict()
            for requirement in requirements:
                if requirement not in requirements_dict:
                    requirements_dict[requirement] = 0
                requirements_dict[requirement] += 1
            requirements = requirements_dict
        self.requirements = requirements


all_connections = [
    ConnectionData(RegionName.menu, RegionName.moss_grotto),
    ConnectionData(RegionName.moss_grotto, RegionName.bone_bottom),
    ConnectionData(RegionName.moss_grotto, RegionName.bonegrave, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.bonegrave, RegionName.chapel_of_the_wanderer),
    ConnectionData(RegionName.bone_bottom, RegionName.weavenest_atla, requirements=ItemName.needolin),
    ConnectionData(RegionName.bone_bottom, RegionName.craggler_cavern, requirements=ItemName.swift_step),
    ConnectionData(RegionName.bone_bottom, RegionName.marrow_west),

    ConnectionData(RegionName.craggler_cavern, RegionName.wormways_entrance), # Add Simple Key Requirement
    ConnectionData(RegionName.wormways_entrance, RegionName.wormways_bottom_left, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.wormways_entrance, RegionName.weavenest_karn, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.wormways_entrance, RegionName.wormways_plasmium),
    ConnectionData(RegionName.wormways_entrance, RegionName.bonegrave),

    ConnectionData(RegionName.marrow_west, RegionName.marrow_bellway, requirements=ItemName.silkspear),
    ConnectionData(RegionName.marrow_bellway, RegionName.marrow_east),
    ConnectionData(RegionName.marrow_bellway, RegionName.marrow_bellway_north_alcove, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.marrow_east, RegionName.deep_docks_entrance),
    ConnectionData(RegionName.marrow_east, RegionName.hunters_march, requirements=ItemName.swift_step),
    ConnectionData(RegionName.marrow_east, RegionName.bone_bottom_after_skull_tyrant, requirements=EventName.skull_tyrant_defeated),

    ConnectionData(RegionName.hunters_march, RegionName.chapel_of_the_beast, requirements=ItemName.drifters_cloak),
    ConnectionData(RegionName.deep_docks_entrance, RegionName.deep_docks_swift_step),
    ConnectionData(RegionName.deep_docks_entrance, RegionName.deep_docks_forge_daughter),
    ConnectionData(RegionName.deep_docks_entrance, RegionName.deep_docks_lace, requirements=ItemName.swift_step),
    ConnectionData(RegionName.deep_docks_lace, RegionName.deep_docks_bell),
    ConnectionData(RegionName.deep_docks_bell, RegionName.far_fields_entrance),
    ConnectionData(RegionName.deep_docks_forge_daughter, RegionName.deep_docks_diving_bell, requirements=[ItemName.swift_step, ItemName.clawline]),
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
    ConnectionData(RegionName.greymoor_spires, RegionName.sinners_road, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.greymoor_spires, RegionName.wisp_thicket),
    ConnectionData(RegionName.greymoor_spires, RegionName.chapel_of_the_reaper),
    ConnectionData(RegionName.greymoor_spires, RegionName.yarnaby),
    ConnectionData(RegionName.yarnaby, RegionName.yarnaby_with_steel_spines),  # Add requirement to get cursed
    ConnectionData(RegionName.greymoor_craw_lake, RegionName.verdania),
    ConnectionData(RegionName.halfway_home, RegionName.halfway_home_alcove, requirements=ItemName.faydown_cloak),

    ConnectionData(RegionName.sinners_road, RegionName.bilewater),

    ConnectionData(RegionName.bilewater, RegionName.bilewater_bellway),
    ConnectionData(RegionName.bilewater_bellway, RegionName.mist),
    ConnectionData(RegionName.bilewater, RegionName.bilewater_upper, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.mist, RegionName.exhaust_organ, requirements=ItemName.needolin),

    ConnectionData(RegionName.bellhart, RegionName.shellwood),
    ConnectionData(RegionName.shellwood, RegionName.bellhart_upper, requirements=ItemName.cling_grip),

    ConnectionData(RegionName.shellwood, RegionName.greyroot),
    ConnectionData(RegionName.greyroot, RegionName.greyroot_rite_of_pollip, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.greyroot_rite_of_pollip, RegionName.greyroot_with_twisted_bud, requirements=ItemName.twisted_bud),

    ConnectionData(RegionName.bellhart_upper, RegionName.bellhart_saved),
    ConnectionData(RegionName.bellhart_saved, RegionName.pinmaster_home),
    ConnectionData(RegionName.bellhart_saved, RegionName.bellhart_wishwall),
    ConnectionData(RegionName.bellhart_wishwall, RegionName.wish_shellwood_missing_courrier, requirements=[ItemName.cling_grip]),
    ConnectionData(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_after_tipp, requirements={ItemName.tipp_and_pill: 1}),
    ConnectionData(RegionName.bellhart_wishwall_after_tipp, RegionName.wish_sinners_road_missing_brother, requirements={ItemName.tipp_and_pill: 1}),
    ConnectionData(RegionName.bellhart_wishwall_after_tipp, RegionName.bellhart_delivery_wishes, requirements={ItemName.tipp_and_pill: 2}),
    ConnectionData(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_after_needle),  # TODO: Write logic for this
    ConnectionData(RegionName.bellhart_wishwall_after_needle, RegionName.bellhart_wishwall_after_needle_and_relic),  # TODO: Write logic for this
    ConnectionData(RegionName.bellhart_wishwall_after_needle, RegionName.wish_pinmaster_oil, requirements=ItemName.pale_oil),  # TODO: Write logic for this
    ConnectionData(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_all_maps_faydown_and_two_melodies),  # TODO: Write logic for this
    ConnectionData(RegionName.bellhart_wishwall_all_maps_faydown_and_two_melodies, RegionName.trail_end, requirements=[ItemName.cling_grip, ItemName.faydown_cloak]),
    ConnectionData(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_after_beastfy, requirements=[EventName.beastfly_defeated, EventName.fourth_chorus_defeat, EventName.songclave_discovered]), # Not sure if beast crest, or just killing first beastfly here
    ConnectionData(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_bellhart_restored, requirements=[ItemName.bellhart_restoration, ItemName.clawline]), # TODO: Add one needle upgrade to this

    ConnectionData(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_act_3, requirements=[ItemName.act_3]),
    ConnectionData(RegionName.bellhart_wishwall_act_3, RegionName.bellhart_wishwall_with_strike, requirements=[ItemName.needle_strike]),
    ConnectionData(RegionName.bellhart_wishwall_act_3, RegionName.wish_heros_call),
    ConnectionData(RegionName.bellhart_wishwall_act_3, RegionName.bellhart_wishwall_after_awaiting_end),
    ConnectionData(RegionName.bellhart_wishwall_after_awaiting_end, RegionName.wish_dark_hearts),
    ConnectionData(RegionName.bellhart_wishwall_after_awaiting_end, RegionName.bellhart_wishwall_with_silk_soar, requirements=ItemName.silk_soar),
    ConnectionData(RegionName.bellhart_wishwall_with_silk_soar, RegionName.bellhart_wishwall_after_karmelita),
    ConnectionData(RegionName.bellhart_wishwall_after_karmelita, RegionName.wish_hidden_hunter),

    ConnectionData(RegionName.shellwood, RegionName.blasted_steps, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.blasted_steps, RegionName.sands_of_karak, requirements=ItemName.clawline),
    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_pinstress, requirements=[ItemName.swift_step, ItemName.cling_grip, ItemName.drifters_cloak]),
    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_grand_gate, requirements={ItemName.swift_step: 1, ItemName.cling_grip: 1, ItemName.drifters_cloak: 1, ItemName.grand_gate_bell: 5}),
    ConnectionData(RegionName.blasted_steps_grand_gate, RegionName.grand_gate, requirements=[EventName.last_judge_defeated]),
    ConnectionData(RegionName.grand_gate, RegionName.underworks_act_2),
    ConnectionData(RegionName.exhaust_organ, RegionName.underworks_act_2, requirements=[EventName.phantom_defeated]),
    ConnectionData(RegionName.underworks_act_2, RegionName.underworks, requirements=[EventName.act_2_reached]),
    ConnectionData(RegionName.underworks, RegionName.underworks_confessional),
    ConnectionData(RegionName.underworks, RegionName.choral_chambers_above_bellway),
    ConnectionData(RegionName.underworks_cauldron, RegionName.underworks),
    ConnectionData(RegionName.underworks_cauldron, RegionName.twelfth_architect),
    ConnectionData(RegionName.twelfth_architect, RegionName.chapel_of_the_architect, requirements=ItemName.architect_key),
    ConnectionData(RegionName.choral_chambers_above_bellway, RegionName.choral_chambers_bellway),
    ConnectionData(RegionName.choral_chambers_bellway, RegionName.choral_chambers),
    ConnectionData(RegionName.choral_chambers, RegionName.whiteward),
    ConnectionData(RegionName.whiteward, RegionName.underworks_cauldron),
    ConnectionData(RegionName.choral_chambers, RegionName.cogwork_core),
    ConnectionData(RegionName.choral_chambers, RegionName.memorium, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.choral_chambers, RegionName.cradle, requirements=[ItemName.architect_melody, ItemName.vaultkeeper_melody, ItemName.conductor_melody]),
    ConnectionData(RegionName.choral_chambers, RegionName.high_halls),
    ConnectionData(RegionName.choral_chambers, RegionName.the_slab),
    ConnectionData(RegionName.choral_chambers, RegionName.songclave),
    ConnectionData(RegionName.memorium, RegionName.putrified_ducts),
    ConnectionData(RegionName.putrified_ducts, RegionName.fleatopia),
    ConnectionData(RegionName.cogwork_core, RegionName.whispering_vaults),
    ConnectionData(RegionName.whispering_vaults, RegionName.whispering_vaults_east),
    ConnectionData(RegionName.whispering_vaults_east, RegionName.choral_chambers_outside),

    ConnectionData(RegionName.the_slab, RegionName.mount_fay, requirements=ItemName.clawline),
    ConnectionData(RegionName.the_slab, RegionName.the_slab_shortcut_cave, requirements=[ItemName.faydown_cloak, ItemName.key_of_apostate]),
    ConnectionData(RegionName.the_slab_shortcut_cave, RegionName.the_slab_first_sinner_cave, requirements=ItemName.key_of_heretic),
    ConnectionData(RegionName.deep_docks_diving_bell, RegionName.abyss, requirements=ItemName.act_3),
    ConnectionData(RegionName.abyss, RegionName.weavenest_absolom),

    ConnectionData(RegionName.choral_chambers, RegionName.citadel),
    ConnectionData(RegionName.grand_gate, RegionName.citadel),
    ConnectionData(RegionName.whispering_vaults, RegionName.citadel),
    ConnectionData(RegionName.high_halls, RegionName.citadel),
    ConnectionData(RegionName.memorium, RegionName.citadel),
    ConnectionData(RegionName.cogwork_core, RegionName.citadel),
    ConnectionData(RegionName.whiteward, RegionName.citadel),

    ConnectionData(RegionName.cradle, RegionName.cradle_with_soul_snare, requirements=[ItemName.soul_snare, ItemName.needolin]),
    ConnectionData(RegionName.cradle_with_soul_snare, RegionName.cradle_act_3, requirements=ItemName.act_3),
    ConnectionData(RegionName.cradle_act_3, RegionName.escaped_cradle_act_3),
    ConnectionData(RegionName.escaped_cradle_act_3, RegionName.choral_chambers_act_3),
    ConnectionData(RegionName.choral_chambers_act_3, RegionName.mount_fay_act_3, requirements=[ItemName.clawline, ItemName.faydown_cloak]),
    ConnectionData(RegionName.choral_chambers_act_3, RegionName.blasted_steps_act_3),
    ConnectionData(RegionName.choral_chambers_act_3, RegionName.craw_lake_act_3),
    ConnectionData(RegionName.craw_lake_act_3, RegionName.court_of_craws, requirements=ItemName.craw_summons),
    ConnectionData(RegionName.blasted_steps_act_3, RegionName.moss_grotto_act_3),
    ConnectionData(RegionName.moss_grotto_act_3, RegionName.ruined_chapel),

    ConnectionData(RegionName.weavenest_atla, RegionName.eva_0),
    ConnectionData(RegionName.eva_0, RegionName.eva_1, requirements={ItemName.crest_slots: 1}),
    ConnectionData(RegionName.eva_1, RegionName.eva_2, requirements={ItemName.crest_slots: 2}),
    ConnectionData(RegionName.eva_2, RegionName.eva_3, requirements={ItemName.crest_slots: 3}),
    ConnectionData(RegionName.eva_3, RegionName.eva_4, requirements={ItemName.crest_slots: 4}),
    ConnectionData(RegionName.eva_4, RegionName.eva_5, requirements={ItemName.crest_slots: 5}),
    ConnectionData(RegionName.eva_5, RegionName.eva_6, requirements={ItemName.crest_slots: 6}),
    ConnectionData(RegionName.eva_6, RegionName.eva_7, requirements={ItemName.crest_slots: 7}),
    ConnectionData(RegionName.eva_7, RegionName.eva_8, requirements={ItemName.crest_slots: 8}),
    ConnectionData(RegionName.eva_8, RegionName.eva_9, requirements={ItemName.crest_slots: 9}),
    ConnectionData(RegionName.eva_9, RegionName.eva_10, requirements={ItemName.crest_slots: 10}),
    ConnectionData(RegionName.eva_10, RegionName.eva_11, requirements={ItemName.crest_slots: 11}),
    ConnectionData(RegionName.eva_11, RegionName.eva_12, requirements={ItemName.crest_slots: 12}),
    ConnectionData(RegionName.eva_12, RegionName.eva_13, requirements={ItemName.crest_slots: 13}),
    ConnectionData(RegionName.eva_13, RegionName.eva_14, requirements={ItemName.crest_slots: 14}),
    ConnectionData(RegionName.eva_14, RegionName.eva_15, requirements={ItemName.crest_slots: 15}),
    ConnectionData(RegionName.eva_15, RegionName.eva_16, requirements={ItemName.crest_slots: 16}),
    ConnectionData(RegionName.eva_16, RegionName.eva_17, requirements={ItemName.crest_slots: 17}),
    ConnectionData(RegionName.eva_17, RegionName.eva_18, requirements={ItemName.crest_slots: 18}),
    ConnectionData(RegionName.eva_18, RegionName.eva_19, requirements={ItemName.crest_slots: 19}),
    ConnectionData(RegionName.eva_19, RegionName.eva_20, requirements={ItemName.crest_slots: 20}),
    ConnectionData(RegionName.eva_20, RegionName.eva_21, requirements={ItemName.crest_slots: 21}),
    ConnectionData(RegionName.eva_21, RegionName.eva_22, requirements={ItemName.crest_slots: 22}),
    ConnectionData(RegionName.eva_22, RegionName.eva_23, requirements={ItemName.crest_slots: 23}),
    ConnectionData(RegionName.eva_23, RegionName.eva_24, requirements={ItemName.crest_slots: 24}),
    ConnectionData(RegionName.eva_24, RegionName.eva_25, requirements={ItemName.crest_slots: 25}),
    ConnectionData(RegionName.eva_25, RegionName.eva_26, requirements={ItemName.crest_slots: 26}),
    ConnectionData(RegionName.eva_26, RegionName.eva_27, requirements={ItemName.crest_slots: 27}),
    ConnectionData(RegionName.eva_27, RegionName.eva_28, requirements={ItemName.crest_slots: 28}),
    ConnectionData(RegionName.eva_28, RegionName.eva_29, requirements={ItemName.crest_slots: 29}),
    ConnectionData(RegionName.eva_29, RegionName.eva_30, requirements={ItemName.crest_slots: 30}),
    ConnectionData(RegionName.eva_30, RegionName.eva_31, requirements={ItemName.crest_slots: 31}),
    ConnectionData(RegionName.eva_31, RegionName.eva_32, requirements={ItemName.crest_slots: 32}),
    ConnectionData(RegionName.eva_32, RegionName.eva_33, requirements={ItemName.crest_slots: 33}),
    ConnectionData(RegionName.eva_33, RegionName.eva_34, requirements={ItemName.crest_slots: 34}),
    ConnectionData(RegionName.eva_34, RegionName.eva_35, requirements={ItemName.crest_slots: 35}),
    ConnectionData(RegionName.eva_35, RegionName.eva_36, requirements={ItemName.crest_slots: 36}),
    ConnectionData(RegionName.eva_36, RegionName.eva_37, requirements={ItemName.crest_slots: 37}),
    ConnectionData(RegionName.eva_37, RegionName.eva_38, requirements={ItemName.crest_slots: 38}),
    ConnectionData(RegionName.eva_38, RegionName.eva_39, requirements={ItemName.crest_slots: 39}),
    ConnectionData(RegionName.eva_39, RegionName.eva_40, requirements={ItemName.crest_slots: 40}),
]

connections_by_name: Dict[str, ConnectionData] = {(connection.entrance if connection.entrance else f"{connection.origin} -> {connection.destination}"): connection for connection in all_connections}