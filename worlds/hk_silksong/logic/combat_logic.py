from ..data.connections_data import standardize_requirements
from ..options.options import CombatLogic
from ..strings.boss_names import Boss
from ..strings.item_names import ItemName

side_slash = [(ItemName.rightslash, ItemName.leftslash)]
any_slash_except_up = [(ItemName.rightslash, ItemName.leftslash, ItemName.downslash)]
any_slash_except_down = [(ItemName.rightslash, ItemName.leftslash, ItemName.upslash)]

combat_logic_requirements = {
    Boss.moss_mother: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: [],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [ItemName.upslash],
    },
    Boss.double_moss_mother: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: [ItemName.upslash, ItemName.needle_upgrade],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.bell_beast: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: side_slash,
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.lace: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: [],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.fourth_chorus: {
        CombatLogic.option_minimal: [ItemName.upslash],
        CombatLogic.option_usual: [ItemName.drifters_cloak],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.moorwing: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: any_slash_except_down,
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.sister_splinter: {
        CombatLogic.option_minimal: [ItemName.upslash],
        CombatLogic.option_usual: [],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.widow: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: side_slash,
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.great_conchflies: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: [ItemName.needle_upgrade],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.last_judge: {
        CombatLogic.option_minimal: any_slash_except_up,
        CombatLogic.option_usual: [ItemName.needle_upgrade],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.cogwork_dancers: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: [ItemName.needle_upgrade],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.trobbio: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: [ItemName.needle_upgrade],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.tormented_trobbio: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.groal_the_great: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.the_unraveled: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.disgraced_chef_lugoli: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.craggler: {
        CombatLogic.option_minimal: [ItemName.upslash],
        CombatLogic.option_usual: [ItemName.needle_upgrade],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 2},
    },
    Boss.father_of_the_flame: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.voltvyrm: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 1},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.second_sentinel: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.broodmother: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 1},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [],
    },
    Boss.plasmified_zango: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.shrine_guardian_seth: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.palestag: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.lost_garmond: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.pinstress: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.gurr_the_outcast: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.watcher_at_the_edge: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 3},
    },
    Boss.crawfather: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    # Boss.summoned_savior: {
    #     CombatLogic.option_minimal: [],
    #     CombatLogic.option_usual: [],
    #     CombatLogic.option_nice_tools: [],
    #     CombatLogic.option_skill_issue: [],
    # },
    Boss.shakra: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 3},
    },
    Boss.garmond_and_zaza: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 3},
    },

    Boss.savage_beastfly_beast: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: [],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [ItemName.needle_upgrade],
    },
    Boss.savage_beastfly_wish: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 1},
        CombatLogic.option_nice_tools: [],  # Lava Bell
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 2},
    },

    Boss.skull_tyrant_wish: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: [],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [ItemName.needle_upgrade],
    },
    Boss.skull_tyrant_bone_bottom: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: [],
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: [ItemName.needle_upgrade],
    },

    Boss.phantom: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 1},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 2},
    },

    Boss.raging_conchfly: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 3},
    },
    Boss.first_sinner: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 3},
    },
    Boss.lace_cradle: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],  # tacks
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 3},
    },
    Boss.grand_mother_silk: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 2},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 3},
    },

    Boss.bell_eater: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.black_thread_moss_mother: {
        CombatLogic.option_minimal: [],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.crust_king_khann: {
        CombatLogic.option_minimal: [ItemName.cling_grip, ItemName.drifters_cloak],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.nyleth: {
        CombatLogic.option_minimal: [ItemName.cling_grip, ItemName.drifters_cloak],
        CombatLogic.option_usual: {ItemName.faydown_cloak: 1, ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.skarrsinger_karmelita: {
        CombatLogic.option_minimal: [ItemName.drifters_cloak],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],  # tacks
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.clover_dancers: {
        CombatLogic.option_minimal: [ItemName.faydown_cloak],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
    Boss.lost_lace: {
        CombatLogic.option_minimal: [ItemName.faydown_cloak, ItemName.drifters_cloak, ItemName.swift_step],
        CombatLogic.option_usual: {ItemName.needle_upgrade: 3},
        CombatLogic.option_nice_tools: [],  # tacks
        CombatLogic.option_skill_issue: {ItemName.needle_upgrade: 4},
    },
}

for boss in combat_logic_requirements:
    for val in combat_logic_requirements[boss]:
        combat_logic_requirements[boss][val] = standardize_requirements(combat_logic_requirements[boss][val])