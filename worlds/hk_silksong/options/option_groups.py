import logging

import Options as ap_options
from . import options

silksong_option_groups = []
try:
    from Options import OptionGroup
except ImportError:
    logging.warning("Old AP Version, OptionGroup not available.")
else:
    sv_option_groups = [
        OptionGroup("General", [
            options.Goal,
            options.RandomizeMovementAbilities,
            options.RandomizeCombatAbilities,
            options.RandomizeOtherAbilities,
            options.RandomizeBossRewards,
            options.RandomizeEvaRewards,
            options.RandomizeMemoryLockets,
            options.RandomizeWishRewards,
            options.RandomizeCrests,
            options.RandomStartingCrest,
            options.RandomizeShopItems,
            options.RandomizePickups,
        ]),
        OptionGroup("Advanced Options", [
            ap_options.DeathLink,
            ap_options.ProgressionBalancing,
            ap_options.Accessibility,
        ]),
    ]
