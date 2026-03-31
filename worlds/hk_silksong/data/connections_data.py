from typing import List, Optional, Dict

from ..strings.item_names import ItemName, EventName
from ..strings.region_names import RegionName


class ConnectionData:
    origin: str
    destination: str
    entrance: str
    requirements: Optional[Dict[str | tuple[str], int]]
    include_reverse: bool

    def __init__(self, origin: str, destination: str, entrance: str = "", requirements: None | List[str | tuple[str, ...]] | str | Dict[str, int] = None, include_reverse: bool = True):
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
        self.include_reverse = include_reverse


def one_way_connection(origin: str, destination: str, entrance: str = "", requirements: None | List[str | tuple[str, ...]] | str | Dict[str, int] = None) -> ConnectionData:
    return ConnectionData(origin, destination, entrance, requirements, False)


all_connections = [
    ConnectionData(RegionName.menu, RegionName.moss_grotto),
    ConnectionData(RegionName.moss_grotto, RegionName.bone_bottom),
    ConnectionData(RegionName.moss_grotto, RegionName.bonegrave, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.moss_grotto, RegionName.weavenest_atla, requirements=ItemName.needolin),
    ConnectionData(RegionName.bonegrave, RegionName.chapel_of_the_wanderer),
    ConnectionData(RegionName.bone_bottom, RegionName.craggler_cavern, requirements=[(ItemName.swift_step, ItemName.faydown_cloak, ItemName.clawline)]),
    ConnectionData(RegionName.bone_bottom, RegionName.marrow_west),
    ConnectionData(RegionName.bone_bottom, RegionName.bone_bottom_bellway, requirements=[ItemName.the_marrow_bell_beast]),
    ConnectionData(RegionName.bone_bottom, RegionName.bone_bottom_wishwall, requirements=ItemName.bone_bottom_wishwall),

    ConnectionData(RegionName.craggler_cavern, RegionName.wormways_entrance), # Add Simple Key Requirement
    ConnectionData(RegionName.wormways_entrance, RegionName.wormways_bottom_left, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.wormways_entrance, RegionName.wormways_upper, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.wormways_entrance, RegionName.weavenest_karn, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.wormways_entrance, RegionName.bonegrave),

    ConnectionData(RegionName.marrow_west, RegionName.marrow_bell_beast_fight, requirements=ItemName.silkspear),
    ConnectionData(RegionName.marrow_bell_beast_fight, RegionName.marrow_bellway, requirements=ItemName.silkspear),
    ConnectionData(RegionName.marrow_bellway, RegionName.marrow_east),
    ConnectionData(RegionName.marrow_bellway, RegionName.marrow_bellway_north),
    ConnectionData(RegionName.marrow_bellway_north, RegionName.marrow_bellway_north_alcove, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.marrow_east, RegionName.deep_docks_entrance),
    ConnectionData(RegionName.marrow_east, RegionName.hunters_march, requirements=ItemName.swift_step),
    ConnectionData(RegionName.marrow_east, RegionName.marrow_east_bone_bottom_wishes, requirements=ItemName.bone_bottom_wishwall),
    ConnectionData(RegionName.marrow_east, RegionName.flea_caravan_marrow),
    ConnectionData(RegionName.flea_caravan_marrow, RegionName.lost_flea_wish),
    ConnectionData(RegionName.lost_flea_wish, RegionName.flea_caravan_marrow_with_5_fleas, requirements={ItemName.lost_flea: 5}),
    ConnectionData(RegionName.marrow_east_bone_bottom_wishes, RegionName.marrow_east_skull_tyrant, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.marrow_east_bone_bottom_wishes, RegionName.marrow_east_flintbeetles, requirements=[(EventName.visited_shellwood, EventName.visited_greymoor,)]),
    ConnectionData(RegionName.marrow_east_skull_tyrant, RegionName.bone_bottom_after_skull_tyrant, requirements=[EventName.skull_tyrant_defeated, (EventName.visited_blasted_steps, EventName.visited_sinners_road, EventName.visited_citadel)]),

    ConnectionData(RegionName.hunters_march, RegionName.chapel_of_the_beast, requirements=ItemName.drifters_cloak),
    ConnectionData(RegionName.deep_docks_entrance, RegionName.deep_docks_swift_step),
    ConnectionData(RegionName.deep_docks_swift_step, RegionName.deep_docks_swift_step_upper, requirements=ItemName.swift_step),
    ConnectionData(RegionName.deep_docks_entrance, RegionName.deep_docks_bellway),
    ConnectionData(RegionName.deep_docks_bellway, RegionName.deep_docks_bellway_flea_room),
    ConnectionData(RegionName.deep_docks_entrance, RegionName.deep_docks_forge_daughter),
    ConnectionData(RegionName.deep_docks_entrance, RegionName.deep_docks_lace, requirements=ItemName.swift_step),
    ConnectionData(RegionName.deep_docks_lace, RegionName.deep_docks_bell),
    ConnectionData(RegionName.deep_docks_bell, RegionName.far_fields_entrance),
    ConnectionData(RegionName.deep_docks_forge_daughter, RegionName.deep_docks_diving_bell, requirements=[ItemName.swift_step, ItemName.clawline]),
    ConnectionData(RegionName.far_fields_entrance, RegionName.far_fields_pilgrims_rest),
    ConnectionData(RegionName.far_fields_entrance, RegionName.far_fields_bellway),
    ConnectionData(RegionName.far_fields_bellway, RegionName.far_fields_pilgrims_rest_rhinogrund, requirements=[ItemName.drifters_cloak, ItemName.cling_grip]),
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
    ConnectionData(RegionName.greymoor_spires, RegionName.greymoor_spires_above_halfway_home, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.greymoor_spires_above_halfway_home, RegionName.sinners_road),
    ConnectionData(RegionName.greymoor_spires, RegionName.greymoor_spires_upper, requirements=ItemName.drifters_cloak),
    ConnectionData(RegionName.greymoor_spires_upper, RegionName.wisp_thicket, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.wisp_thicket, RegionName.underworks_from_wisp_thicket),
    ConnectionData(RegionName.greymoor_spires, RegionName.chapel_of_the_reaper),
    ConnectionData(RegionName.greymoor_spires, RegionName.yarnaby),
    ConnectionData(RegionName.yarnaby, RegionName.yarnaby_with_steel_spines),  # Add requirement to get cursed
    ConnectionData(RegionName.greymoor_craw_lake, RegionName.verdania),
    ConnectionData(RegionName.halfway_home, RegionName.halfway_home_alcove, requirements=ItemName.faydown_cloak),

    ConnectionData(RegionName.sinners_road, RegionName.bilewater),
    ConnectionData(RegionName.sinners_road, RegionName.sinners_road_chef_lugoli, requirements=ItemName.faydown_cloak),

    one_way_connection(RegionName.bilewater, RegionName.bilewater_bellway),
    one_way_connection(RegionName.bilewater_bellway, RegionName.bilewater, requirements=[(ItemName.faydown_cloak, ItemName.silk_soar)]),
    ConnectionData(RegionName.bilewater_bellway, RegionName.mist),
    ConnectionData(RegionName.bilewater, RegionName.bilewater_upper, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.mist, RegionName.exhaust_organ, requirements=ItemName.needolin),

    ConnectionData(RegionName.bellhart, RegionName.shellwood_entrance),

    ConnectionData(RegionName.shellwood_entrance, RegionName.shellwood, requirements=[(ItemName.swift_step, ItemName.clawline)]),
    ConnectionData(RegionName.shellwood, RegionName.bellhart_upper, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.shellwood, RegionName.greyroot),
    one_way_connection(RegionName.shellwood, RegionName.shellwood_bellway, requirements=ItemName.cling_grip),
    one_way_connection(RegionName.shellwood_bellway, RegionName.shellwood),
    ConnectionData(RegionName.shellwood_bellway, RegionName.blasted_steps),

    one_way_connection(RegionName.greyroot, RegionName.greyroot_rite_of_pollip, requirements=ItemName.cling_grip),
    one_way_connection(RegionName.greyroot_rite_of_pollip, RegionName.greyroot_with_twisted_bud, requirements=ItemName.twisted_bud),

    ConnectionData(RegionName.bellhart_upper, RegionName.bellhart_saved),
    ConnectionData(RegionName.bellhart_saved, RegionName.pinmaster_home),
    ConnectionData(RegionName.bellhart_saved, RegionName.bellhart_wishwall),
    ConnectionData(RegionName.bellhart_saved, RegionName.bellhart_bellway),
    ConnectionData(RegionName.bellhart_bellway, RegionName.bellhart_lower),
    one_way_connection(RegionName.bellhart_lower, RegionName.marrow_east),
    one_way_connection(RegionName.bellhart_wishwall, RegionName.wish_shellwood_missing_courrier, requirements=[ItemName.cling_grip]),
    one_way_connection(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_after_tipp, requirements={ItemName.tipp_and_pill: 1}),
    one_way_connection(RegionName.bellhart_wishwall_after_tipp, RegionName.wish_sinners_road_missing_brother, requirements={ItemName.tipp_and_pill: 1}),
    one_way_connection(RegionName.bellhart_wishwall_after_tipp, RegionName.bellhart_delivery_wishes, requirements={ItemName.tipp_and_pill: 2}),
    one_way_connection(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_after_needle),  # TODO: Write logic for this
    one_way_connection(RegionName.bellhart_wishwall_after_needle, RegionName.bellhart_wishwall_after_needle_and_relic),  # TODO: Write logic for this
    one_way_connection(RegionName.bellhart_wishwall_after_needle, RegionName.wish_pinmaster_oil, requirements=ItemName.pale_oil),  # TODO: Write logic for this
    one_way_connection(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_all_maps_faydown_and_two_melodies),  # TODO: Write logic for this
    one_way_connection(RegionName.bellhart_wishwall_all_maps_faydown_and_two_melodies, RegionName.trail_end, requirements=[ItemName.cling_grip, ItemName.faydown_cloak]),
    one_way_connection(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_after_beastfy, requirements=[EventName.beastfly_defeated, EventName.fourth_chorus_defeat, EventName.visited_songclave]), # Not sure if beast crest, or just killing first beastfly here
    one_way_connection(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_bellhart_restored, requirements=[ItemName.bellhart_restoration, ItemName.clawline]), # TODO: Add one needle upgrade to this

    one_way_connection(RegionName.bellhart_wishwall, RegionName.bellhart_wishwall_act_3, requirements=[ItemName.act_3]),
    one_way_connection(RegionName.bellhart_wishwall_act_3, RegionName.bellhart_wishwall_with_strike, requirements=[ItemName.needle_strike]),
    one_way_connection(RegionName.bellhart_wishwall_act_3, RegionName.wish_heros_call),
    one_way_connection(RegionName.bellhart_wishwall_act_3, RegionName.bellhart_wishwall_after_awaiting_end),
    one_way_connection(RegionName.bellhart_wishwall_after_awaiting_end, RegionName.wish_dark_hearts),
    one_way_connection(RegionName.bellhart_wishwall_after_awaiting_end, RegionName.bellhart_wishwall_with_silk_soar, requirements=ItemName.silk_soar),
    one_way_connection(RegionName.bellhart_wishwall_with_silk_soar, RegionName.bellhart_wishwall_after_karmelita),
    one_way_connection(RegionName.bellhart_wishwall_after_karmelita, RegionName.wish_hidden_hunter),


    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_shaft),
    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_bellway),
    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_grindle, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_dice_pilgrim),
    ConnectionData(RegionName.blasted_steps, RegionName.sands_of_karak, requirements=ItemName.clawline),
    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_pinstress, requirements=[ItemName.swift_step, ItemName.cling_grip, ItemName.drifters_cloak]),
    ConnectionData(RegionName.blasted_steps, RegionName.blasted_steps_grand_gate, requirements={ItemName.swift_step: 1, ItemName.cling_grip: 1, ItemName.drifters_cloak: 1, ItemName.needolin: 1, ItemName.grand_gate_bell_marrow: 1, ItemName.grand_gate_bell_deep_docks: 1, ItemName.grand_gate_bell_greymoor: 1, ItemName.grand_gate_bell_bellhart: 1, ItemName.grand_gate_bell_shellwood: 1}),
    ConnectionData(RegionName.blasted_steps_grand_gate, RegionName.grand_gate, requirements=[EventName.last_judge_defeated]),
    ConnectionData(RegionName.grand_gate, RegionName.underworks_act_2),
    ConnectionData(RegionName.exhaust_organ, RegionName.underworks_act_2, requirements=[EventName.phantom_defeated]),
    ConnectionData(RegionName.underworks_act_2, RegionName.underworks, requirements=[EventName.act_2_reached]),
    ConnectionData(RegionName.underworks, RegionName.underworks_confessional),
    ConnectionData(RegionName.underworks, RegionName.choral_chambers_above_bellway),
    ConnectionData(RegionName.underworks, RegionName.underworks_ventrica),
    ConnectionData(RegionName.underworks_cauldron, RegionName.underworks),
    ConnectionData(RegionName.underworks_cauldron, RegionName.twelfth_architect),
    ConnectionData(RegionName.twelfth_architect, RegionName.chapel_of_the_architect, requirements=ItemName.architect_key),

    one_way_connection(RegionName.choral_chambers_above_bellway, RegionName.choral_chambers_bellway),
    ConnectionData(RegionName.choral_chambers_bellway, RegionName.choral_chambers),
    ConnectionData(RegionName.choral_chambers_bellway, RegionName.grand_bellway_ventrica),
    ConnectionData(RegionName.choral_chambers, RegionName.whiteward),
    ConnectionData(RegionName.whiteward, RegionName.whiteward_ceiling, requirements=[ItemName.cling_grip, ItemName.clawline]),
    ConnectionData(RegionName.whiteward, RegionName.underworks_cauldron),
    ConnectionData(RegionName.choral_chambers, RegionName.choral_chambers_ventrica),
    ConnectionData(RegionName.choral_chambers, RegionName.cogwork_core),
    ConnectionData(RegionName.choral_chambers, RegionName.memorium, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.choral_chambers, RegionName.cradle, requirements=[ItemName.needolin, ItemName.architect_melody, ItemName.vaultkeeper_melody, ItemName.conductor_melody]),
    ConnectionData(RegionName.choral_chambers, RegionName.high_halls),
    ConnectionData(RegionName.choral_chambers, RegionName.the_slab),
    ConnectionData(RegionName.choral_chambers, RegionName.songclave),
    ConnectionData(RegionName.choral_chambers, RegionName.choral_chambers_vent, requirements=ItemName.drifters_cloak),
    ConnectionData(RegionName.memorium, RegionName.memorium_ventrica),
    ConnectionData(RegionName.memorium, RegionName.memorium_giant_flea),
    ConnectionData(RegionName.memorium, RegionName.memorium_outside, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.memorium_outside, RegionName.putrified_ducts, requirements=ItemName.cling_grip),
    ConnectionData(RegionName.high_halls, RegionName.high_halls_ventrica),
    ConnectionData(RegionName.songclave, RegionName.first_shrine_ventrica),

    ConnectionData(RegionName.putrified_ducts, RegionName.putrified_ducts_bellway),
    ConnectionData(RegionName.putrified_ducts, RegionName.putrified_ducts_vog_passage),
    ConnectionData(RegionName.putrified_ducts, RegionName.fleatopia, requirements={ItemName.needolin: 1, ItemName.lost_flea: 27, ItemName.kratt: 1, ItemName.vog: 1, ItemName.giant_lost_flea: 1}),
    ConnectionData(RegionName.cogwork_core, RegionName.whispering_vaults),
    ConnectionData(RegionName.whispering_vaults, RegionName.whispering_vaults_east),
    ConnectionData(RegionName.whispering_vaults_east, RegionName.choral_chambers_outside),
    ConnectionData(RegionName.choral_chambers_outside, RegionName.choral_chambers_outside_alcove, requirements=ItemName.clawline),

    ConnectionData(RegionName.sands_of_karak, RegionName.sands_of_karak_shaft, requirements=[ItemName.cling_grip, ItemName.faydown_cloak, ItemName.clawline, ItemName.swift_step, ItemName.drifters_cloak]),
    ConnectionData(RegionName.sands_of_karak_shaft, RegionName.sands_of_karak_lower_right),
    ConnectionData(RegionName.sands_of_karak_lower_right, RegionName.sands_of_karak_upper_right),
    ConnectionData(RegionName.sands_of_karak_upper_right, RegionName.sands_of_karak_upper_left),
    ConnectionData(RegionName.sands_of_karak_upper_right, RegionName.sands_of_karak_voltnest, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.sands_of_karak_upper_left, RegionName.sands_of_karak_coral_tower),
    ConnectionData(RegionName.sands_of_karak_coral_tower, RegionName.sands_of_karak_coral_tower_dream, requirements=ItemName.elegy_of_the_deep),

    ConnectionData(RegionName.the_slab, RegionName.the_slab_bellway),
    ConnectionData(RegionName.the_slab_bellway, RegionName.mount_fay, requirements=ItemName.clawline),
    ConnectionData(RegionName.the_slab_bellway, RegionName.the_slab_above_bench, requirements=ItemName.faydown_cloak),
    ConnectionData(RegionName.the_slab, RegionName.the_slab_shortcut_cave, requirements=[ItemName.faydown_cloak, ItemName.key_of_apostate]),
    ConnectionData(RegionName.the_slab_shortcut_cave, RegionName.the_slab_first_sinner_cave, requirements=ItemName.key_of_heretic),
    ConnectionData(RegionName.the_slab, RegionName.the_slab_indolent, requirements=ItemName.key_of_indolent),
    ConnectionData(RegionName.deep_docks_diving_bell, RegionName.abyss, requirements=ItemName.act_3),
    ConnectionData(RegionName.abyss, RegionName.weavenest_absolom),
    one_way_connection(RegionName.abyss, RegionName.abyss_with_everbloom, requirements=ItemName.everbloom),

    ConnectionData(RegionName.mount_fay, RegionName.mount_fay_ceiling_cave, requirements=ItemName.cling_grip),

    one_way_connection(RegionName.choral_chambers, RegionName.citadel),
    one_way_connection(RegionName.grand_gate, RegionName.citadel),
    one_way_connection(RegionName.whispering_vaults, RegionName.citadel),
    one_way_connection(RegionName.high_halls, RegionName.citadel),
    one_way_connection(RegionName.memorium, RegionName.citadel),
    one_way_connection(RegionName.cogwork_core, RegionName.citadel),
    one_way_connection(RegionName.whiteward, RegionName.citadel),

    one_way_connection(RegionName.cradle, RegionName.terminus_ventrica),
    one_way_connection(RegionName.cradle, RegionName.cradle_with_soul_snare, requirements=[ItemName.soul_snare, ItemName.needolin]),
    one_way_connection(RegionName.cradle_with_soul_snare, RegionName.cradle_act_3, requirements=ItemName.act_3),
    one_way_connection(RegionName.cradle_act_3, RegionName.escaped_cradle_act_3),
    one_way_connection(RegionName.escaped_cradle_act_3, RegionName.choral_chambers_act_3),
    ConnectionData(RegionName.choral_chambers_act_3, RegionName.mount_fay_act_3, requirements=[ItemName.clawline, ItemName.faydown_cloak]),
    ConnectionData(RegionName.choral_chambers_act_3, RegionName.blasted_steps_act_3),
    ConnectionData(RegionName.choral_chambers_act_3, RegionName.craw_lake_act_3),
    ConnectionData(RegionName.craw_lake_act_3, RegionName.court_of_craws, requirements=ItemName.craw_summons),
    ConnectionData(RegionName.blasted_steps_act_3, RegionName.moss_grotto_act_3),
    ConnectionData(RegionName.blasted_steps_act_3, RegionName.wormways_plasmium),
    ConnectionData(RegionName.moss_grotto_act_3, RegionName.ruined_chapel),

    ConnectionData(RegionName.weavenest_atla, RegionName.weavenest_atla_moss_mothers, requirements=[ItemName.swift_step]),
    one_way_connection(RegionName.weavenest_atla, RegionName.eva_0),
    one_way_connection(RegionName.eva_0, RegionName.eva_1, requirements={ItemName.crest_slots: 1}),
    one_way_connection(RegionName.eva_1, RegionName.eva_2, requirements={ItemName.crest_slots: 2}),
    one_way_connection(RegionName.eva_2, RegionName.eva_3, requirements={ItemName.crest_slots: 3}),
    one_way_connection(RegionName.eva_3, RegionName.eva_4, requirements={ItemName.crest_slots: 4}),
    one_way_connection(RegionName.eva_4, RegionName.eva_5, requirements={ItemName.crest_slots: 5}),
    one_way_connection(RegionName.eva_5, RegionName.eva_6, requirements={ItemName.crest_slots: 6}),
    one_way_connection(RegionName.eva_6, RegionName.eva_7, requirements={ItemName.crest_slots: 7}),
    one_way_connection(RegionName.eva_7, RegionName.eva_8, requirements={ItemName.crest_slots: 8}),
    one_way_connection(RegionName.eva_8, RegionName.eva_9, requirements={ItemName.crest_slots: 9}),
    one_way_connection(RegionName.eva_9, RegionName.eva_10, requirements={ItemName.crest_slots: 10}),
    one_way_connection(RegionName.eva_10, RegionName.eva_11, requirements={ItemName.crest_slots: 11}),
    one_way_connection(RegionName.eva_11, RegionName.eva_12, requirements={ItemName.crest_slots: 12}),
    one_way_connection(RegionName.eva_12, RegionName.eva_13, requirements={ItemName.crest_slots: 13}),
    one_way_connection(RegionName.eva_13, RegionName.eva_14, requirements={ItemName.crest_slots: 14}),
    one_way_connection(RegionName.eva_14, RegionName.eva_15, requirements={ItemName.crest_slots: 15}),
    one_way_connection(RegionName.eva_15, RegionName.eva_16, requirements={ItemName.crest_slots: 16}),
    one_way_connection(RegionName.eva_16, RegionName.eva_17, requirements={ItemName.crest_slots: 17}),
    one_way_connection(RegionName.eva_17, RegionName.eva_18, requirements={ItemName.crest_slots: 18}),
    one_way_connection(RegionName.eva_18, RegionName.eva_19, requirements={ItemName.crest_slots: 19}),
    one_way_connection(RegionName.eva_19, RegionName.eva_20, requirements={ItemName.crest_slots: 20}),
    one_way_connection(RegionName.eva_20, RegionName.eva_21, requirements={ItemName.crest_slots: 21}),
    one_way_connection(RegionName.eva_21, RegionName.eva_22, requirements={ItemName.crest_slots: 22}),
    one_way_connection(RegionName.eva_22, RegionName.eva_23, requirements={ItemName.crest_slots: 23}),
    one_way_connection(RegionName.eva_23, RegionName.eva_24, requirements={ItemName.crest_slots: 24}),
    one_way_connection(RegionName.eva_24, RegionName.eva_25, requirements={ItemName.crest_slots: 25}),
    one_way_connection(RegionName.eva_25, RegionName.eva_26, requirements={ItemName.crest_slots: 26}),
    one_way_connection(RegionName.eva_26, RegionName.eva_27, requirements={ItemName.crest_slots: 27}),
    one_way_connection(RegionName.eva_27, RegionName.eva_28, requirements={ItemName.crest_slots: 28}),
    one_way_connection(RegionName.eva_28, RegionName.eva_29, requirements={ItemName.crest_slots: 29}),
    one_way_connection(RegionName.eva_29, RegionName.eva_30, requirements={ItemName.crest_slots: 30}),
    one_way_connection(RegionName.eva_30, RegionName.eva_31, requirements={ItemName.crest_slots: 31}),
    one_way_connection(RegionName.eva_31, RegionName.eva_32, requirements={ItemName.crest_slots: 32}),
    one_way_connection(RegionName.eva_32, RegionName.eva_33, requirements={ItemName.crest_slots: 33}),
    one_way_connection(RegionName.eva_33, RegionName.eva_34, requirements={ItemName.crest_slots: 34}),
    one_way_connection(RegionName.eva_34, RegionName.eva_35, requirements={ItemName.crest_slots: 35}),
    one_way_connection(RegionName.eva_35, RegionName.eva_36, requirements={ItemName.crest_slots: 36}),
    one_way_connection(RegionName.eva_36, RegionName.eva_37, requirements={ItemName.crest_slots: 37}),
    one_way_connection(RegionName.eva_37, RegionName.eva_38, requirements={ItemName.crest_slots: 38}),
    one_way_connection(RegionName.eva_38, RegionName.eva_39, requirements={ItemName.crest_slots: 39}),
    one_way_connection(RegionName.eva_39, RegionName.eva_40, requirements={ItemName.crest_slots: 40}),

    ConnectionData(RegionName.bellhart_bellway, RegionName.bellway_travel, requirements=ItemName.bellhart_bell_beast),
    ConnectionData(RegionName.bilewater_bellway, RegionName.bellway_travel, requirements=ItemName.bilewater_bell_beast),
    ConnectionData(RegionName.blasted_steps_bellway, RegionName.bellway_travel, requirements=ItemName.blasted_steps_bell_beast),
    ConnectionData(RegionName.bone_bottom_bellway, RegionName.bellway_travel, requirements=[ItemName.bone_bottom_bell_beast, ItemName.the_marrow_bell_beast]),
    ConnectionData(RegionName.deep_docks_bellway, RegionName.bellway_travel, requirements=ItemName.deep_docks_bell_beast),
    ConnectionData(RegionName.far_fields_bellway, RegionName.bellway_travel, requirements=ItemName.far_fields_bell_beast),
    ConnectionData(RegionName.choral_chambers_bellway, RegionName.bellway_travel, requirements=ItemName.choral_chambers_bell_beast),
    ConnectionData(RegionName.greymoor_bellway, RegionName.bellway_travel, requirements=ItemName.greymoor_bell_beast),
    ConnectionData(RegionName.putrified_ducts_bellway, RegionName.bellway_travel, requirements=ItemName.putrified_ducts_bell_beast),
    ConnectionData(RegionName.shellwood_bellway, RegionName.bellway_travel, requirements=ItemName.shellwood_bell_beast),
    ConnectionData(RegionName.marrow_bellway, RegionName.bellway_travel, requirements=ItemName.the_marrow_bell_beast),
    ConnectionData(RegionName.the_slab_bellway, RegionName.bellway_travel, requirements=ItemName.the_slab_bell_beast),

    ConnectionData(RegionName.terminus_ventrica, RegionName.ventrica_travel, requirements=ItemName.terminus_ventrica),
    ConnectionData(RegionName.memorium_ventrica, RegionName.ventrica_travel, requirements=ItemName.memorium_ventrica),
    ConnectionData(RegionName.high_halls_ventrica, RegionName.ventrica_travel, requirements=ItemName.high_halls_ventrica),
    ConnectionData(RegionName.first_shrine_ventrica, RegionName.ventrica_travel, requirements=ItemName.first_shrine_ventrica),
    ConnectionData(RegionName.choral_chambers_ventrica, RegionName.ventrica_travel, requirements=ItemName.choral_chambers_ventrica),
    ConnectionData(RegionName.grand_bellway_ventrica, RegionName.ventrica_travel, requirements=ItemName.grand_bellway_ventrica),
    ConnectionData(RegionName.underworks_ventrica, RegionName.ventrica_travel, requirements=ItemName.underworks_ventrica),
]

# Create all the inverse connections
for connection_data in all_connections:
    if not connection_data.include_reverse:
        continue
    all_connections.append(ConnectionData(connection_data.destination, connection_data.origin, "", connection_data.requirements, False))

connections_by_name: Dict[str, ConnectionData] = {(connection.entrance if connection.entrance else f"{connection.origin} -> {connection.destination}"): connection for connection in all_connections}