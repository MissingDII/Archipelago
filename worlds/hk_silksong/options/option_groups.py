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
            options.ShuffleMovementAbilities,
        ]),
        OptionGroup("Advanced Options", [
            ap_options.DeathLink,
            ap_options.ProgressionBalancing,
            ap_options.Accessibility,
        ]),
    ]
