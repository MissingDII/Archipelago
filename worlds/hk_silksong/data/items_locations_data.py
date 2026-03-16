from typing import Optional, List

from BaseClasses import ItemClassification
from ..items.items import ItemData
from ..locations import LocationGroup, LocationData
from ..strings.item_names import ItemName, EventName
from ..strings.region_names import RegionName


class LocationItemData:
    location_name: str
    location_data: LocationData
    item_data: Optional[ItemData]

    def __init__(self, location_data: LocationData, item_data: None | ItemData | str = None):
        self.location_name = location_data.name
        self.location_data = location_data
        if isinstance(item_data, str):
            item_data = ItemData(item_data)
        self.item_data = item_data


def item_location(location: str, region: str, groups: List[LocationGroup], item: None | str = None, classification: ItemClassification = ItemClassification.progression):
    event_only = LocationGroup.EVENT_ONLY in groups
    return LocationItemData(LocationData(location, region, groups, event_only), None if item is None else ItemData(item, classification, event_only))


all_locations_items_pairs: List[LocationItemData] = [
    item_location("Bound the Needle", RegionName.moss_grotto, [LocationGroup.RANDOMIZED_BIND, LocationGroup.ACT_1], ItemName.bind, ItemClassification.useful),
    item_location("Tutorial: Breakable Walls 1", RegionName.moss_grotto, [LocationGroup.RANDOMIZED_STARTING_CREST, LocationGroup.ACT_1], ItemName.crest_hunter_progressive),
    item_location("Tutorial: Breakable Walls 2", RegionName.moss_grotto, [LocationGroup.RANDOMIZED_SLASH, LocationGroup.ACT_1], ItemName.upslash, ItemClassification.useful),
    item_location("Tutorial: Breakable Walls 3", RegionName.moss_grotto, [LocationGroup.RANDOMIZED_SLASH, LocationGroup.ACT_1], ItemName.downslash, ItemClassification.useful),
    item_location("Tutorial: Mossgrub", RegionName.moss_grotto, [LocationGroup.RANDOMIZED_SLASH, LocationGroup.ACT_1], ItemName.leftslash, ItemClassification.useful),
    item_location("Tutorial: Mossmir", RegionName.moss_grotto, [LocationGroup.RANDOMIZED_SLASH, LocationGroup.ACT_1], ItemName.rightslash, ItemClassification.useful),
    item_location("Enter Deep Docks", RegionName.deep_docks_entrance, [LocationGroup.EVENT_ONLY, LocationGroup.ACT_1], ItemName.bone_bottom_wishwall),

    item_location("Save: The Threadspun Town", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    item_location("Seek: The Great Citadel", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    item_location("Ring The Bell In The Marrow", RegionName.marrow_bellway, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1], ItemName.grand_gate_bell_marrow),
    item_location("Ring The Bell In Deep Docks", RegionName.deep_docks_bell, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1], ItemName.grand_gate_bell_deep_docks),
    item_location("Ring The Bell In Greymoor", RegionName.greymoor_craw_lake, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1], ItemName.grand_gate_bell_greymoor),
    item_location("Ring The Bell In Bellhart", RegionName.bellhart, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1], ItemName.grand_gate_bell_bellhart),
    item_location("Ring The Bell In Shellwood", RegionName.shellwood, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1], ItemName.grand_gate_bell_shellwood),

    item_location("Search: Silent Halls", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    item_location("Ascend: Pharloom's Crown", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    item_location("Learn: Conductor's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2], ItemName.conductor_melody),
    item_location("Learn: Architect's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2], ItemName.architect_melody),
    item_location("Learn: Vaultkeeper's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2], ItemName.vaultkeeper_melody),

    item_location("Seek: After The Fall", RegionName.choral_chambers, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    item_location("Seek: Awaiting The End", RegionName.ruined_chapel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    item_location("Seek: The Dark Below", RegionName.abyss, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    item_location("Ascend: Return To Pharloom", RegionName.abyss, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    item_location("Seek: Spell Seeker", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3], ItemName.elegy_of_the_deep),

    item_location("Weaver Spire: Silkspear", RegionName.bone_bottom, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_1], ItemName.silkspear),
    item_location("Weaver Spire: Thread Storm", RegionName.greymoor_craw_lake, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_1], ItemName.thread_storm, ItemClassification.useful),
    item_location("Weaver Spire: Sharpdart", RegionName.weavenest_karn, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_2], ItemName.sharpdart, ItemClassification.useful),
    item_location("Acquire Pale Nails", RegionName.cradle, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.ACT_3], ItemName.pale_nails, ItemClassification.useful),

    item_location("Hunt Wish: Flexile Spines", RegionName.far_fields_seamstress, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_1], ItemName.drifters_cloak),
    item_location("Weaver Spire: Cling Grip", RegionName.shellwood, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_1], ItemName.cling_grip),
    item_location("Weaver Spire: Swift Step", RegionName.deep_docks_swift_step, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_1], ItemName.swift_step),
    item_location("Acquire Faydown Cloak", RegionName.mount_fay, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_2], ItemName.faydown_cloak),
    item_location("Weaver Spire: Clawline", RegionName.underworks, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_2], ItemName.clawline),
    item_location("Weaver Spire: Silk Soar", RegionName.abyss, [LocationGroup.MOVEMENT_ABILITY, LocationGroup.ACT_3], ItemName.silk_soar),

    item_location("Learn Needle Strike", RegionName.blasted_steps_pinstress, [LocationGroup.COMBAT_ABILITY, LocationGroup.ACT_1], ItemName.needle_strike),

    # item_location("Seek: The Old Hearts", RegionName.ruined_chapel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    # item_location("Complete Red Memory", RegionName.ruined_chapel, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.OBJECTIVE, LocationGroup.ACT_3], ItemName.everbloom, ItemClassification.progression),

    # item_location("Pickup Farsight", RegionName.weavenest_absolom, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.UNIQUE_PICKUPS, LocationGroup.ACT_3], ItemName.farsight, ItemClassification.useful),

    item_location("Defeat Moss Mother", RegionName.moss_grotto, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Bell Beast", RegionName.marrow_bellway, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1], ItemName.silk_heart),
    item_location("Defeat Lace", RegionName.deep_docks_lace, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Fourth Chorus", RegionName.far_fields_fourth_chorus, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Moorwing", RegionName.greymoor_spires, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Sister Splinter", RegionName.shellwood, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Widow", RegionName.bellhart_upper, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1], ItemName.needolin),
    item_location("Defeat Great Conchflies", RegionName.blasted_steps, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Last Judge", RegionName.blasted_steps_grand_gate, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Last Judge Defeated", RegionName.blasted_steps_grand_gate, [LocationGroup.EVENT_ONLY, LocationGroup.ACT_1], EventName.last_judge_defeated),
    item_location("Defeat Cogwork Dancers", RegionName.cogwork_core, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat Trobbio", RegionName.choral_chambers, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat Tormented Trobbio", RegionName.choral_chambers_act_3, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Groal the Great", RegionName.bilewater_upper, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat The Unraveled", RegionName.whiteward, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2], ItemName.silk_heart),
    item_location("Defeat Disgraced Chef Lugoli", RegionName.sinners_road_chef_lugoli, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat Craggler", RegionName.craggler_cavern, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Father of the Flame", RegionName.wisp_thicket, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat Voltvyrm", RegionName.sands_of_karak, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat Second Sentinel", RegionName.high_halls, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat Broodmother", RegionName.the_slab, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat Plasmified Zango", RegionName.wormways_plasmium, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Shrine Guardian Seth", RegionName.grand_gate, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Palestag", RegionName.verdania, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Lost Garmond", RegionName.blasted_steps_act_3, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Pinstress", RegionName.mount_fay_act_3, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Gurr the Outcast", RegionName.far_fields_fields, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Watcher at the Edge", RegionName.sands_of_karak, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Crawfather", RegionName.greymoor_craw_lake, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    # item_location("Defeat Summoned Savior", RegionName., [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Shakra", RegionName.greymoor_spires, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat Garmond and Zaza", RegionName.choral_chambers_outside, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),

    item_location("Defeat Savage Beastfly (Beast)", RegionName.chapel_of_the_beast, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Savage Beastfly Defeated (Beast)", RegionName.chapel_of_the_beast, [LocationGroup.EVENT_ONLY, LocationGroup.ACT_1], EventName.beastfly_defeated),
    item_location("Defeat Savage Beastfly (Wish)", RegionName.far_fields_beastfly, [LocationGroup.WISH, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),

    item_location("Defeat Skull Tyrant (Wish)", RegionName.marrow_east_skull_tyrant, [LocationGroup.WISH, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Skull Tyrant Defeated (Wish)", RegionName.marrow_east_skull_tyrant, [LocationGroup.EVENT_ONLY, LocationGroup.ACT_1], EventName.skull_tyrant_defeated),
    item_location("Defeat Skull Tyrant (Bone Bottom)", RegionName.bone_bottom_after_skull_tyrant, [LocationGroup.WISH, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),

    item_location("Defeat Phantom", RegionName.exhaust_organ, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1], ItemName.cross_stitch, ItemClassification.progression),
    item_location("Phantom Defeated", RegionName.exhaust_organ, [LocationGroup.EVENT_ONLY, LocationGroup.ACT_1], EventName.phantom_defeated),

    item_location("Enter Act 2", RegionName.underworks_act_2, [LocationGroup.EVENT_ONLY, LocationGroup.ACT_2], EventName.act_2_reached),

    item_location("Defeat Raging Conchfly", RegionName.sands_of_karak, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat First Sinner", RegionName.the_slab_first_sinner_cave, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2], ItemName.rune_rage, ItemClassification.useful),
    item_location("Defeat Lace (Cradle)", RegionName.cradle, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2], ItemName.silk_heart),
    item_location("Defeat Grand Mother Silk", RegionName.cradle, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Snare Grand Mother Silk", RegionName.cradle_with_soul_snare, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Unleash The Void On Pharloom", RegionName.cradle_with_soul_snare, [LocationGroup.EVENT_ONLY, LocationGroup.ACT_3], ItemName.act_3),

    item_location("Defeat Bell Eater", RegionName.choral_chambers, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3], ItemName.beastling_call, ItemClassification.useful),
    item_location("Defeat Crust King Khann", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Nyleth", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Skarrsinger Karmelita", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Clover Dancers", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Lost Lace", RegionName.abyss_with_everbloom, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),

    item_location("Eva: 0 Slots", RegionName.eva_0, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA_REWARD, LocationGroup.EVA, LocationGroup.ACT_1], ItemName.crest_hunter_progressive, ItemClassification.useful),
    item_location("Eva: 1 Slots", RegionName.eva_1, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 2 Slots", RegionName.eva_2, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 3 Slots", RegionName.eva_3, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 4 Slots", RegionName.eva_4, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 5 Slots", RegionName.eva_5, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 6 Slots", RegionName.eva_6, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 7 Slots", RegionName.eva_7, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 8 Slots", RegionName.eva_8, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 9 Slots", RegionName.eva_9, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 10 Slots", RegionName.eva_10, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 11 Slots", RegionName.eva_11, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 12 Slots", RegionName.eva_12, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA_REWARD, LocationGroup.EVA, LocationGroup.ACT_1], ItemName.vesticrest_yellow, ItemClassification.useful),
    item_location("Eva: 13 Slots", RegionName.eva_13, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 14 Slots", RegionName.eva_14, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 15 Slots", RegionName.eva_15, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 16 Slots", RegionName.eva_16, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 17 Slots", RegionName.eva_17, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 18 Slots", RegionName.eva_18, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 19 Slots", RegionName.eva_19, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 20 Slots", RegionName.eva_20, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA_REWARD, LocationGroup.EVA, LocationGroup.ACT_1], ItemName.vesticrest_blue, ItemClassification.useful),
    item_location("Eva: 21 Slots", RegionName.eva_21, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 22 Slots", RegionName.eva_22, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 23 Slots", RegionName.eva_23, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 24 Slots", RegionName.eva_24, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 25 Slots", RegionName.eva_25, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 26 Slots", RegionName.eva_26, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 27 Slots", RegionName.eva_27, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA_REWARD, LocationGroup.EVA, LocationGroup.ACT_2], ItemName.crest_hunter_progressive, ItemClassification.useful),
    item_location("Eva: 28 Slots", RegionName.eva_28, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 29 Slots", RegionName.eva_29, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 30 Slots", RegionName.eva_30, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 31 Slots", RegionName.eva_31, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 32 Slots", RegionName.eva_32, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.EVA_REWARD, LocationGroup.EVA, LocationGroup.ACT_2], ItemName.sylphsong, ItemClassification.useful),
    item_location("Eva: 33 Slots", RegionName.eva_33, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    item_location("Eva: 34 Slots", RegionName.eva_34, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    item_location("Eva: 35 Slots", RegionName.eva_35, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    item_location("Eva: 36 Slots", RegionName.eva_36, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    item_location("Eva: 37 Slots", RegionName.eva_37, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),

    item_location("Bound the Crest of Reaper", RegionName.chapel_of_the_reaper, [LocationGroup.CREST, LocationGroup.ACT_1], ItemName.crest_reaper),
    item_location("Bound the Crest of Wanderer", RegionName.chapel_of_the_wanderer, [LocationGroup.CREST, LocationGroup.ACT_1], ItemName.crest_wanderer),
    item_location("Bound the Crest of Beast", RegionName.chapel_of_the_beast, [LocationGroup.CREST, LocationGroup.ACT_1], ItemName.crest_beast),
    item_location("Bound the Crest of Architect", RegionName.chapel_of_the_architect, [LocationGroup.CREST, LocationGroup.ACT_2], ItemName.crest_architect),
    item_location("Bound the Crest of Shaman", RegionName.ruined_chapel, [LocationGroup.CREST, LocationGroup.ACT_3], ItemName.crest_shaman),

    item_location("Memory locket - Chapel of the Beast", RegionName.chapel_of_the_beast, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1], ItemName.memory_locket),
    item_location("Memory locket - Mort", RegionName.far_fields_pilgrims_rest, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_1], ItemName.memory_locket),
    # item_location("Memory locket - Grindle", RegionName.blasted_steps_grindle_shop_act_3, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_3], ItemName.memory_locket),
    item_location("Memory locket - Greymoor Bellway", RegionName.greymoor_bellway, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_1], ItemName.memory_locket),
    item_location("Memory locket - Volatiles FlintBeetles", RegionName.marrow_east_flintbeetles, [LocationGroup.MEMORY_LOCKET, LocationGroup.WISH, LocationGroup.ACT_1], ItemName.memory_locket),
    # item_location("Memory locket - Survivor's Camp", RegionName.marrow_west, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_3], ItemName.memory_locket),
    item_location("Memory locket - The Marrow", RegionName.marrow_bellway_north_alcove, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1], ItemName.memory_locket),
    item_location("Memory locket - Wormways", RegionName.wormways_bottom_left, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1], ItemName.memory_locket),
    item_location("Memory locket - Frey", RegionName.bellhart_saved, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_1], ItemName.memory_locket),
    item_location("Memory locket - Blasted Steps", RegionName.blasted_steps, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1], ItemName.memory_locket),
    item_location("Memory locket - Bilewater", RegionName.bilewater_bellway, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1], ItemName.memory_locket),
    item_location("Memory locket - Choral Chambers", RegionName.choral_chambers_above_bellway, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2], ItemName.memory_locket),
    item_location("Memory locket - Underworks", RegionName.underworks_confessional, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2], ItemName.memory_locket),
    item_location("Memory locket - Deep Docks", RegionName.deep_docks_diving_bell, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2], ItemName.memory_locket),
    item_location("Memory locket - Whispering Vaults", RegionName.whispering_vaults_east, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2], ItemName.memory_locket),
    item_location("Memory locket - Sands of Karak", RegionName.sands_of_karak, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2], ItemName.memory_locket),
    item_location("Memory locket - Halfway Home", RegionName.halfway_home_alcove, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2], ItemName.memory_locket),
    item_location("Memory locket - Memorium", RegionName.memorium, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2], ItemName.memory_locket),
    item_location("Memory locket - The Slab", RegionName.the_slab_shortcut_cave, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2], ItemName.memory_locket),
    item_location("Memory locket - Bilewater Upper", RegionName.bilewater_upper, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2], ItemName.memory_locket),
    item_location("Memory locket - Bellhart Ceiling", RegionName.bellhart, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_3], ItemName.memory_locket),
    item_location("Memory locket - Far Fields East", RegionName.far_fields_fields, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_3], ItemName.memory_locket),

    # item_location("Wayfarer Wish: The Lost Fleas", RegionName.wish_lost_fleas, [LocationGroup.RED_TOOL, LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: Pinmaster's Oil", RegionName.wish_pinmaster_oil, [LocationGroup.WISH, LocationGroup.ACT_2], ItemName.needle_upgrade),
    item_location("Wayfarer Wish: My Missing Courier", RegionName.wish_shellwood_missing_courrier, [LocationGroup.WISH, LocationGroup.SHOP, LocationGroup.ACT_1], ItemName.tipp_and_pill),
    item_location("Wayfarer Wish: My Missing Brother", RegionName.wish_sinners_road_missing_brother, [LocationGroup.WISH, LocationGroup.ACT_2], ItemName.tipp_and_pill),
    # item_location("Wayfarer Wish: Balm For The Wounded", RegionName.wish_whiteward, [LocationGroup.WISH, LocationGroup.SPOOL_FRAGMENT, LocationGroup.ACT_2]),
    # item_location("Wayfarer Wish: The Wandering Merchant", RegionName.wish_choral_chambers, [LocationGroup.WISH, LocationGroup.SHOP, LocationGroup.ACT_2], ItemName.jubilana),
    # item_location("Wayfarer Wish: The Lost Merchant", RegionName.wish_memorium_outside, [LocationGroup.WISH, LocationGroup.SHOP, LocationGroup.ACT_2], ItemName.jubilana),
    item_location("Wayfarer Wish: Rite Of Rebirth", RegionName.greyroot_with_twisted_bud, [LocationGroup.EVENT_ONLY, LocationGroup.ACT_2], ItemName.crest_cursed),
    item_location("Wayfarer Wish: Infestation Operation", RegionName.yarnaby_with_steel_spines, [LocationGroup.CREST, LocationGroup.WISH, LocationGroup.ACT_2], ItemName.crest_witch),
    # item_location("Wayfarer Wish: Trail's End", RegionName.trail_end, [LocationGroup.RED_TOOL, LocationGroup.WISH, LocationGroup.ACT_2], ItemName.throwing_ring),
    # item_location("Wayfarer Wish: Final Audience", RegionName.wish_final_audience, [LocationGroup.WISH, LocationGroup.ACT_2]),
    item_location("Wayfarer Wish: Silk and Soul", RegionName.choral_chambers, [LocationGroup.WISH, LocationGroup.ACT_2], ItemName.soul_snare),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),

    item_location("Twelfth Architect: Architect Key", RegionName.twelfth_architect, [LocationGroup.SHOP, LocationGroup.ACT_2], ItemName.architect_key),
    # item_location("Receive the Craw Summons", RegionName.craw_lake_act_3, [LocationGroup.UNIQUE_PICKUPS, LocationGroup.ACT_3], ItemName.craw_summons),
    item_location("Pickup White Key", RegionName.songclave, [LocationGroup.UNIQUE_PICKUPS, LocationGroup.ACT_2], ItemName.white_key),
    item_location("Pickup Key of Indolent", RegionName.the_slab, [LocationGroup.UNIQUE_PICKUPS, LocationGroup.ACT_1], ItemName.key_of_indolent),
    item_location("Pickup Key of Heretic", RegionName.the_slab, [LocationGroup.UNIQUE_PICKUPS, LocationGroup.ACT_1], ItemName.key_of_heretic),
    item_location("Pickup Key of Apostate", RegionName.putrified_ducts, [LocationGroup.UNIQUE_PICKUPS, LocationGroup.ACT_2], ItemName.key_of_apostate),
    item_location("Pickup Surgeon's Key", RegionName.whiteward_ceiling, [LocationGroup.UNIQUE_PICKUPS, LocationGroup.ACT_3], ItemName.surgeon_key),
    item_location("Pickup Twisted Bud", RegionName.bilewater_upper, [LocationGroup.UNIQUE_PICKUPS, LocationGroup.ACT_2], ItemName.twisted_bud),


]

locations_items_pairs_by_name = {pair.location_name: pair for pair in all_locations_items_pairs}