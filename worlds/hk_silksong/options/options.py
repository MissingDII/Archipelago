from dataclasses import dataclass
from typing import Protocol, ClassVar

from Options import Choice, PerGameCommonOptions, DeathLink, DefaultOnToggle


class SilksongOption(Protocol):
    internal_name: ClassVar[str]


class Goal(Choice):
    """Goal for this playthrough
    Fanatic: Free Bellhart
    Act 1: Enter the Citadel
    Weaver Queen: Bind Grand Mother Silk
    Snared Silk: Defeat Grand Mother Silk and Entrap Her with the Soul Snare
    Flea Friend: Rescue all of Pharloom's lost fleas and receive their final gift
    Sister of the Void: Complete Act 3
    Completion: Achieve 100% completion and finish the game
    """
    internal_name = "goal"
    display_name = "Goal"
    default = 2
    option_fanatic = 0
    option_act_1 = 1
    option_weaver_queen = 2
    option_snared_silk = 3
    option_flea_friend = 4
    option_sister_of_the_void = 5
    option_completion = 6


class ShuffleMovementAbilities(DefaultOnToggle):
    """Shuffle Movement abilities, such as Swift Step, Cling Grip, Clawline, Cloaks"""
    internal_name = "shuffle_movement_abilities"
    display_name = "Shuffle Movement Abilities"


@dataclass
class SilksongOptions(PerGameCommonOptions):
    goal: Goal
    shuffle_movement_abilities: ShuffleMovementAbilities
    death_link: DeathLink