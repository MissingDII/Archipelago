from typing import Any, Dict

from . import options

# @formatter:off
all_random_settings = {
    "progression_balancing":                        "random",
    "accessibility":                                "random",
    options.Goal.internal_name:                     "random",
    options.RandomizeMovementAbilities.internal_name: "random",
    "death_link":                                   "random",
}
# @formatter:on


silksong_options_presets: Dict[str, Dict[str, Any]] = {
    "All random": all_random_settings,
}
