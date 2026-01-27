from typing import Union, Optional, List

from BaseClasses import ItemClassification, Region, Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from .data.items_locations_data import all_locations_items_pairs, locations_items_pairs_by_name
from .events import create_events
from .items.items import items_by_name, create_items, SilksongItem, filler_items, item_data_by_name, ItemData
from .locations import SilksongLocation, create_locations, locations_by_name, LocationData, location_data_by_name
from .options.option_groups import silksong_option_groups
from .options.options import SilksongOptions, Goal
from .options.presets import silksong_options_presets
from .regions import create_regions, set_entrance_rules
from .strings.generic_strings import GAME_NAME
from .strings.goal_names import GoalName

client_version = 0


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
    topology_present = False
    web = SilksongWebWorld()

    item_name_to_id = items_by_name
    location_name_to_id = locations_by_name

    options_dataclass = SilksongOptions
    options: SilksongOptions

    enabled_locations: List[str]

    def create_regions(self):
        def create_region(name: str) -> Region:
            return Region(name, self.player, self.multiworld)

        world_regions = create_regions(create_region, self.options)

        def add_location(name: str, code: Optional[int], region: str):
            region: Region = world_regions[region]
            location = SilksongLocation(self.player, name, code, region)
            region.locations.append(location)
            self.enabled_locations.append(name)

        create_locations(add_location, self.options, all_locations_items_pairs, self.random)
        self.multiworld.regions.extend(world_regions.values())

    def set_rules(self):
        set_entrance_rules(self.multiworld, self.player, self.options)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_items(self):
        self.precollect_abilities()
        my_locations = self.multiworld.get_locations(self.player)
        locations_count = len([location
                               for location in my_locations
                               if not location.advancement])

        items_to_exclude = [excluded_items.name
                            for excluded_items in self.multiworld.precollected_items[self.player]]

        created_items = create_items(self.create_item, self.options, locations_items_pairs_by_name, self.enabled_locations, items_to_exclude, self.random)
        self.multiworld.itempool += created_items
        create_events(self.multiworld, self.player, self.enabled_locations)
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

    def precollect_abilities(self):
        pass
        # early_items[self.player]["Incredibly Important Pack"] = 1
        # if self.options.campaign == Options.Campaign.option_basic:
        #     if self.options.coinsanity == Options.CoinSanity.option_coin and self.options.coinbundlequantity >= 5:
        #         self.multiworld.push_precollected(self.create_item("DLC Quest: Coin Bundle"))

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
            "death_link"
        )
        options_dict.update({
            "seed": self.random.randrange(99999999)
        })
        return options_dict
