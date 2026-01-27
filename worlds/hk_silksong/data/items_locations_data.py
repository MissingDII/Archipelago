from typing import Optional, List

from BaseClasses import ItemClassification
from ..items.items import ItemData
from ..locations import LocationGroup, LocationData
from ..strings.item_names import ItemName
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
    return LocationItemData(LocationData(location, region, groups), None if item is None else ItemData(item, classification))


all_locations_items_pairs: List[LocationItemData] = [
    item_location("Escape Moss Grotto", RegionName.bone_bottom, [LocationGroup.ALWAYS_ACTIVE, LocationGroup.ACT_1], ItemName.bind),

    item_location("Save: The Threadspun Town", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    item_location("Seek: The Great Citadel", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    item_location("Ring The Bell In The Marrow", RegionName.marrow_bellway, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    item_location("Ring The Bell In Deep Docks", RegionName.deep_docks_bell, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    item_location("Ring The Bell In Greymoor", RegionName.greymoor_craw_lake, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    item_location("Ring The Bell In Bellhart", RegionName.bellhart, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),
    item_location("Ring The Bell In Shellwood", RegionName.shellwood, [LocationGroup.OBJECTIVE, LocationGroup.ACT_1]),

    item_location("Search: Silent Halls", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    item_location("Ascend: Pharloom's Crown", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.ACT_2]),
    item_location("Learn: Conductor's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2], ItemName.conductor_melody),
    item_location("Learn: Architect's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2], ItemName.architect_melody),
    item_location("Learn: Vaultkeeper's Melody", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.SONG, LocationGroup.ACT_2], ItemName.vaultkeeper_melody),

    item_location("Seek: After The Fall", RegionName.choral_chambers, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    item_location("Seek: Awaiting The End", RegionName.moss_grotto, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
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

    item_location("Seek: The Old Hearts", RegionName.bone_bottom, [LocationGroup.OBJECTIVE, LocationGroup.ACT_3]),
    item_location("Complete Red Memory", RegionName.bone_bottom, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.OBJECTIVE, LocationGroup.ACT_3], ItemName.everbloom, ItemClassification.progression),

    item_location("Pickup Farsight", RegionName.weavenest_atla, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.UNIQUE_PICKUPS, LocationGroup.ACT_3], ItemName.farsight, ItemClassification.useful),

    item_location("Defeat Moss Mother", RegionName.moss_grotto, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Bell Beast", RegionName.marrow_bellway, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1], ItemName.silk_heart),
    item_location("Defeat Lace", RegionName.deep_docks_lace, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Fourth Chorus", RegionName.far_fields_fourth_chorus, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Moorwing", RegionName.greymoor_spires, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Sister Splinter", RegionName.shellwood, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Widow", RegionName.bellhart_upper, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1], ItemName.needolin),
    item_location("Defeat Great Conchflies", RegionName.blasted_steps, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Last Judge", RegionName.blasted_steps_grand_gate, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Cogwork Dancers", RegionName.cogwork_core, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat Trobbio", RegionName.choral_chambers, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat Tormented Trobbio", RegionName.choral_chambers_act_3, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Groal the Great", RegionName.bilewater_upper, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat The Unraveled", RegionName.whiteward, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2], ItemName.silk_heart),
    item_location("Defeat Disgraced Chef Lugoli", RegionName.sinners_road, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
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

    item_location("Defeat Savage Beastfly (Beast)", RegionName.chapel_of_beast, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Savage Beastfly (Wish)", RegionName.far_fields_beastfly, [LocationGroup.WISH, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),

    item_location("Defeat Skull Tyrant (Wish)", RegionName.marrow_east, [LocationGroup.WISH, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),
    item_location("Defeat Skull Tyrant (Bone Bottom)", RegionName.bone_bottom, [LocationGroup.WISH, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1]),

    item_location("Defeat Phantom", RegionName.exhaust_organ, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_1], ItemName.cross_stitch, ItemClassification.useful),

    item_location("Defeat Raging Conchfly", RegionName.sands_of_karak, [LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat First Sinner", RegionName.the_slab, [LocationGroup.SILK_COMBAT_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2], ItemName.rune_rage, ItemClassification.useful),
    item_location("Defeat The Unravelled", RegionName.whiteward, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),
    item_location("Defeat Lace (Cradle)", RegionName.cradle, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2], ItemName.silk_heart),
    item_location("Defeat Grand Mother Silk", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_2]),

    item_location("Defeat Bell Eater", RegionName.choral_chambers, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3], ItemName.beastling_call, ItemClassification.useful),
    item_location("Defeat Crust King Khann", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Nyleth", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Skarrsinger Karmelita", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Clover Dancers", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),
    item_location("Defeat Lost Lace", RegionName.citadel, [LocationGroup.OBJECTIVE, LocationGroup.BOSS_FIGHT, LocationGroup.ACT_3]),

    item_location("Eva: 0 Slots", RegionName.weavenest_atla, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 1 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 2 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 3 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 4 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 5 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 6 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 7 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 8 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 9 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 10 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 11 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 12 Slots", RegionName.weavenest_atla, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 13 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 14 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 15 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 16 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 17 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 18 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 19 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 20 Slots", RegionName.weavenest_atla, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA, LocationGroup.ACT_1]),
    item_location("Eva: 21 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 22 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 23 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 24 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 25 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 26 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 27 Slots", RegionName.weavenest_atla, [LocationGroup.CREST_UPGRADE, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 28 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 29 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 30 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 31 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 32 Slots", RegionName.weavenest_atla, [LocationGroup.SILK_OTHER_ABILITY, LocationGroup.EVA, LocationGroup.ACT_2], ItemName.sylphsong, ItemClassification.useful),
    item_location("Eva: 33 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 34 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 35 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_2]),
    item_location("Eva: 36 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    item_location("Eva: 37 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    item_location("Eva: 38 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    item_location("Eva: 39 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),
    item_location("Eva: 40 Slots", RegionName.weavenest_atla, [LocationGroup.EVA_EXTRA_LOCATIONS, LocationGroup.EVA, LocationGroup.ACT_3]),

    item_location("Memory locket - Chapel of the Beast", RegionName.chapel_of_beast, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1]),
    item_location("Memory locket - Mort", RegionName.far_fields_pilgrims_rest, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_1]),
    # item_location("Memory locket - Grindle", RegionName.blasted_steps_grindle_shop_act_3, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_3]),
    item_location("Memory locket - Greymoor Bellway", RegionName.greymoor_bellway, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_1]),
    item_location("Memory locket - Volatiles FlintBeetles", RegionName.marrow_west, [LocationGroup.MEMORY_LOCKET, LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Memory locket - Survivor's Camp", RegionName.marrow_west, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_3]),
    item_location("Memory locket - The Marrow", RegionName.marrow_bellway_north_alcove, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1]),
    item_location("Memory locket - Wormways", RegionName.wormways_bottom_left, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1]),
    item_location("Memory locket - Frey", RegionName.bellhart_saved, [LocationGroup.MEMORY_LOCKET, LocationGroup.SHOP, LocationGroup.ACT_1]),
    item_location("Memory locket - Blasted Steps", RegionName.blasted_steps, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1]),
    item_location("Memory locket - Bilewater", RegionName.bilewater_bellway, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_1]),
    item_location("Memory locket - Choral Chambers", RegionName.choral_chambers_above_bellway, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    item_location("Memory locket - Underworks", RegionName.underworks_confessional, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    item_location("Memory locket - Deep Docks", RegionName.deep_docks_diving_bell, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    item_location("Memory locket - Whispering Vaults", RegionName.whispering_vaults_east, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    item_location("Memory locket - Sands of Karak", RegionName.sands_of_karak, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    item_location("Memory locket - Halfway Home", RegionName.halfway_home_alcove, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    item_location("Memory locket - Memorium", RegionName.memorium, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    item_location("Memory locket - The Slab", RegionName.the_slab_shortcut_cave, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    item_location("Memory locket - Bilewater Upper", RegionName.bilewater_upper, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_2]),
    item_location("Memory locket - Bellhart Ceiling", RegionName.bellhart, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_3]),
    item_location("Memory locket - Far Fields East", RegionName.far_fields_fields, [LocationGroup.MEMORY_LOCKET, LocationGroup.ACT_3]),

    item_location("Wayfarer Wish: The Lost Fleas", RegionName.marrow_west, [LocationGroup.RED_TOOL, LocationGroup.WISH, LocationGroup.ACT_1]),
    item_location("Wayfarer Wish: Pinmaster's Oil", RegionName.whispering_vaults, [LocationGroup.PALE_OIL, LocationGroup.WISH, LocationGroup.ACT_2]),
    item_location("Wayfarer Wish: My Missing Courier", RegionName.shellwood, [LocationGroup.WISH, LocationGroup.ACT_1]),
    item_location("Wayfarer Wish: My Missing Brother", RegionName.sinners_road, [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    item_location("Wayfarer Wish: Silk and Soul", RegionName.choral_chambers, [LocationGroup.WISH, LocationGroup.ACT_1], ItemName.soul_snare),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),
    # item_location("Wayfarer Wish: ", RegionName., [LocationGroup.WISH, LocationGroup.ACT_1]),


]

locations_items_pairs_by_name = {pair.location_name: pair for pair in all_locations_items_pairs}