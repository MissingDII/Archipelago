from dataclasses import dataclass
from typing import Protocol, ClassVar

from Options import Choice, PerGameCommonOptions, DeathLink, DefaultOnToggle


class SilksongOption(Protocol):
    internal_name: ClassVar[str]


class Goal(Choice):
    """Goal for this playthrough
    Goals lower than weaver queen will exclude the entirety of Act 2 and Act 3
    Goals lower than Sister of the Void will exclude the entirety of Act 3
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


class RandomizeMovementAbilities(DefaultOnToggle):
    """Shuffle movement abilities, such as Swift Step, Cling Grip, Clawline, Cloaks, etc."""
    internal_name = "randomize_movement_abilities"
    display_name = "Randomize Movement Abilities"


class RandomizeCombatAbilities(DefaultOnToggle):
    """Shuffle combat abilities, such as Needle Strike, Thread Storm, Silk Spear, etc."""
    internal_name = "randomize_combat_abilities"
    display_name = "Randomize Combat Abilities"


class RandomizeOtherAbilities(DefaultOnToggle):
    """Shuffle other unique abilities, such as Silk Hearts, Sylphsong, Farsight, Everbloom"""
    internal_name = "randomize_other_abilities"
    display_name = "Randomize Other Abilities"


class RandomizeBossRewards(DefaultOnToggle):
    """Shuffles rewards from beating every boss in the game. This also adds a location reward to bosses that don't usually have a reward, increasing filler."""
    internal_name = "randomize_boss_rewards"
    display_name = "Randomize Boss Rewards"


class RandomizeEvaRewards(Choice):
    """Shuffles rewards from showing Eva your increased nature through unlocked crest slots.
    None: The Eva rewards are not randomized
    Eva: The Eva rewards from the vanilla milestones are randomized
    Evasanity: Every single crest slot you show Eva has a location, increasing filler.
    """
    internal_name = "randomize_eva_rewards"
    display_name = "Randomize Eva Rewards"
    default = 1
    option_none = 0
    option_eva = 1
    option_evasanity = 2


class RandomizeMemoryLockets(DefaultOnToggle):
    """Shuffles memory lockets from all sources"""
    internal_name = "randomize_memory_lockets"
    display_name = "Randomize Memory Lockets"


class RandomizeWishRewards(DefaultOnToggle):
    """Shuffles rewards from all wishes"""
    internal_name = "randomize_wish_rewards"
    display_name = "Randomize Wish Rewards"


class RandomizeCrests(DefaultOnToggle):
    """Shuffles all crests and crest upgrades"""
    internal_name = "randomize_crests"
    display_name = "Randomize Crests"


class RandomStartingCrest(DefaultOnToggle):
    """Start with a random Crest, instead of the Hunter Crest. The random Crest could still be Hunter"""
    internal_name = "random_starting_crests"
    display_name = "Randomize Starting Crest"


class RandomizeShopItems(DefaultOnToggle):
    """Shuffles unique purchasable items in all shops"""
    internal_name = "randomize_shop_items"
    display_name = "Randomize Shop Items"


class RandomizePickups(Choice):
    """Shuffles items picked up from the floor
    None: None of the pickups are randomized
    Unique: The unique item pickups are randomized
    All: All item pickups are randomized
    """
    internal_name = "randomize_pickups"
    display_name = "Randomize Pickups"
    default = 1
    option_none = 0
    option_unique = 1
    option_all = 2


class RandomizeLostFleas(DefaultOnToggle):
    """Shuffles lost fleas around the world"""
    internal_name = "randomize_lost_fleas"
    display_name = "Randomize Lost Fleas"


class RandomizeStations(DefaultOnToggle):
    """Shuffles access to the various Bellway and Ventrica stations"""
    internal_name = "randomize_stations"
    display_name = "Randomize Stations"


@dataclass
class SilksongOptions(PerGameCommonOptions):
    goal: Goal
    randomize_movement_abilities: RandomizeMovementAbilities
    randomize_combat_abilities: RandomizeCombatAbilities
    randomize_other_abilities: RandomizeOtherAbilities
    randomize_boss_rewards: RandomizeBossRewards
    randomize_eva_rewards: RandomizeEvaRewards
    randomize_memory_lockets: RandomizeMemoryLockets
    randomize_wish_rewards: RandomizeWishRewards
    randomize_crests: RandomizeCrests
    random_starting_crests: RandomStartingCrest
    randomize_shop_items: RandomizeShopItems
    randomize_pickups: RandomizePickups
    randomize_lost_fleas: RandomizeLostFleas
    randomize_stations: RandomizeStations
    death_link: DeathLink