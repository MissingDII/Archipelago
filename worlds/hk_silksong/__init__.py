from typing import Union, Optional, List

from BaseClasses import ItemClassification, Region, Tutorial, CollectionState
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from worlds.hk_silksong.data.crests_data import crest_purchasable_slots, crest_default_slots, hunter_crest_purchasable_slots
from .data.items_locations_data import all_locations_items_pairs, locations_items_pairs_by_name
from .events import create_events
from .items.items import items_by_name, create_items, SilksongItem, filler_items, item_data_by_name, ItemData
from .locations import SilksongLocation, create_locations, locations_by_name, LocationData, goal_events_locations, set_item_rules
from .options.option_groups import silksong_option_groups
from .options.options import SilksongOptions, Goal, RandomStartingCrest, RandomizeMovementAbilities, RandomizeCombatAbilities, RandomizePickups, \
    RandomizeShopItems, RandomizeCrests, RandomizeWishRewards, RandomizeMemoryLockets, RandomizeEvaRewards, RandomizeBossRewards, RandomizeOtherAbilities, \
    StartingBind, StartingSlashes, RandomizeNeedleUpgrades, RandomizeLostFleas, RandomizeStations
from .options.presets import silksong_options_presets
from .regions import create_regions, set_entrance_rules, set_combat_logic_entrance_rules
from .strings.generic_strings import GAME_NAME
from .strings.goal_names import GoalName
from .strings.item_names import ItemName

client_version = 0

location_data_by_name = {location.name: location for location in goal_events_locations}
for pair in all_locations_items_pairs:
    location_data_by_name[pair.location_name] = pair.location_data


class SilksongWebWorld(WebWorld):
    options_presets = silksong_options_presets
    option_groups = silksong_option_groups
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Silksong game on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Kaito Kid"]
    )
    tutorials = [setup_en]
    game_info_languages = ["en"]


class SilksongWorld(World):
    """
    Hollow Knight: Silksong is the sequel to the renowned Action-Adventure Metroidvania Hollow Knight
    """
    game = GAME_NAME
    topology_present = True
    web = SilksongWebWorld()

    item_name_to_id = items_by_name
    location_name_to_id = locations_by_name

    options_dataclass = SilksongOptions
    options: SilksongOptions

    enabled_locations: List[str]

    def create_regions(self):
        def create_region(name: str) -> Region:
            return Region(name, self.player, self.multiworld)

        self.enabled_locations = []
        world_regions = create_regions(create_region, self.options)

        def add_location(name: str, code: Optional[int], region: str):
            region: Region = world_regions[region]
            location = SilksongLocation(self.player, name, code, region)
            region.locations.append(location)
            self.enabled_locations.append(name)

        create_locations(add_location, self.options, all_locations_items_pairs, self.random)
        self.multiworld.regions.extend(world_regions.values())

    def set_rules(self):
        set_entrance_rules(self.multiworld, self.player)
        set_combat_logic_entrance_rules(self.multiworld, self.player, self.options)
        set_item_rules(self.multiworld, self.player, self.enabled_locations)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_items(self):
        self.precollect_starting_crest()
        self.precollect_starting_bind()
        self.precollect_starting_slashes()
        self.precollect_wip_stuff()
        my_locations = self.multiworld.get_locations(self.player)
        locations_count = len([location
                               for location in my_locations
                               if not location.advancement])

        items_to_exclude = [excluded_items.name
                            for excluded_items in self.multiworld.precollected_items[self.player]]

        created_items = create_items(self.create_item, self.options, locations_items_pairs_by_name, self.enabled_locations, items_to_exclude, self.random)
        self.multiworld.itempool += created_items
        create_events(self.multiworld, self.player, self.enabled_locations, self.options)
        self.setup_victory()

    def setup_victory(self):
        if self.options.goal == Goal.option_fanatic:
            goal_location = location_data_by_name[GoalName.fanatic]
        elif self.options.goal == Goal.option_act_1:
            goal_location = location_data_by_name[GoalName.act_1]
        elif self.options.goal == Goal.option_weaver_queen:
            goal_location = location_data_by_name[GoalName.weaver_queen]
        elif self.options.goal == Goal.option_snared_silk:
            goal_location = location_data_by_name[GoalName.snared_silk]
        elif self.options.goal == Goal.option_flea_friend:
            goal_location = location_data_by_name[GoalName.flea_friend]
        elif self.options.goal == Goal.option_sister_of_the_void:
            goal_location = location_data_by_name[GoalName.sister_of_the_void]
        elif self.options.goal == Goal.option_completion:
            goal_location = location_data_by_name[GoalName.completion]
        else:
            raise OptionError(f"Invalid Goal: {self.options.goal}")

        region = self.multiworld.get_region(goal_location.region, self.player)
        region.add_event(goal_location.name, "Victory", None, SilksongLocation, SilksongItem)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def precollect_starting_crest(self):
        starting_crest = ItemName.crest_hunter_progressive
        if self.options.random_starting_crests == RandomStartingCrest.option_true:
            potential_crests = [starting_crest, ItemName.crest_wanderer, ItemName.crest_reaper, ItemName.crest_beast, ItemName.crest_witch, ItemName.crest_architect, ItemName.crest_shaman]
            starting_crest = self.random.choice(potential_crests)
        self.multiworld.push_precollected(self.create_item(starting_crest))

    def precollect_starting_bind(self):
        if self.options.starting_bind == StartingBind.option_true:
            self.multiworld.push_precollected(self.create_item(ItemName.bind))

    def precollect_starting_slashes(self):
        all_slashes = [ItemName.downslash, ItemName.upslash, ItemName.leftslash, ItemName.rightslash]
        starting_slashes = set()
        if self.options.starting_slashes == StartingSlashes.option_all:
            starting_slashes += all_slashes
        elif self.options.starting_slashes == StartingSlashes.option_random_direction:
            starting_slashes.add(self.random.choice(all_slashes))
        elif self.options.starting_slashes == StartingSlashes.option_two_random_directions:
            starting_slashes.add(self.random.sample(all_slashes, k=2))
        elif self.options.starting_slashes == StartingSlashes.option_down:
            starting_slashes.add(ItemName.downslash)
        elif self.options.starting_slashes == StartingSlashes.option_down_and_random_direction:
            starting_slashes.add(ItemName.downslash)
            starting_slashes.add(self.random.choice([ItemName.upslash, ItemName.leftslash, ItemName.rightslash]))

        for starting_slash in starting_slashes:
            self.multiworld.push_precollected(self.create_item(starting_slash))

    def precollect_wip_stuff(self):
        pass
        # self.multiworld.push_precollected(self.create_item(ItemName.twisted_bud))
        # self.multiworld.push_precollected(self.create_item(ItemName.soul_snare))

    def create_item(self, item: Union[str, ItemData], classification: ItemClassification = None) -> SilksongItem:
        if isinstance(item, str):
            item = item_data_by_name[item]
        if classification is None:
            classification = item.classification

        return SilksongItem(item.name, classification, item.id, self.player)

    def get_filler_item_name(self) -> str:
        filler = self.multiworld.random.choice(filler_items)
        return filler.name

    def fill_slot_data(self):
        options_dict = self.options.as_dict(
            Goal.internal_name,
            RandomizeMovementAbilities.internal_name,
            RandomizeCombatAbilities.internal_name,
            RandomizeOtherAbilities.internal_name,
            RandomizeNeedleUpgrades.internal_name,
            StartingSlashes.internal_name,
            StartingBind.internal_name,
            RandomizeBossRewards.internal_name,
            RandomizeEvaRewards.internal_name,
            RandomizeMemoryLockets.internal_name,
            RandomizeWishRewards.internal_name,
            RandomizeCrests.internal_name,
            RandomStartingCrest.internal_name,
            RandomizeShopItems.internal_name,
            RandomizePickups.internal_name,
            RandomizeLostFleas.internal_name,
            RandomizeStations.internal_name,
            "death_link"
        )
        options_dict.update({
            "seed": self.random.randrange(99999999),
            "client_version": self.world_version.as_simple_string(),
        })
        return options_dict

    def collect(self, state: CollectionState, item: SilksongItem) -> bool:
        change = super().collect(state, item)
        if not change:
            return change

        if item.name not in crest_purchasable_slots and item.name != ItemName.memory_locket:
            return change

        self.update_crest_slots(state)
        return change

    def remove(self, state: CollectionState, item: SilksongItem) -> bool:
        change = super().remove(state, item)
        if not change:
            return change

        if item.name not in crest_purchasable_slots and item.name != ItemName.memory_locket:
            return change

        self.update_crest_slots(state)
        return change

    def update_crest_slots(self, state: CollectionState):
        current_slots = 0
        for crest in crest_default_slots:
            if state.prog_items[self.player][crest] >= 1:
                current_slots += crest_default_slots[crest]

        available_purchasable_slots = 0
        for crest in crest_purchasable_slots:
            if state.prog_items[self.player][crest] >= 1:
                available_purchasable_slots += crest_purchasable_slots[crest]

        number_lockets = state.prog_items[self.player][ItemName.memory_locket]
        if state.prog_items[self.player][ItemName.crest_hunter_progressive] >= 1:
            number_lockets -= hunter_crest_purchasable_slots  # We assume that the player might waste their lockets on Hunter Crest, which Eva doesn't count

        current_slots += min(available_purchasable_slots, max(number_lockets, 0))

        state.prog_items[self.player][ItemName.crest_slots] = current_slots
