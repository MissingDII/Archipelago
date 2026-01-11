from typing import Union, Optional

from BaseClasses import ItemClassification, Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .items import ItemData, create_items, ItemGroup, items_by_name, item_names_by_groups, item_data_by_name
from .items import SilksongItem
from .locations import SilksongLocation, create_locations, locations_by_name
from .options.option_groups import silksong_option_groups
from .options.options import SilksongOptions
from .options.presets import silksong_options_presets
from .regions import create_regions
from .strings.generic_strings import GAME_NAME

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

    def create_regions(self):
        def create_region(name: str) -> Region:
            return Region(name, self.player, self.multiworld)

        world_regions = create_regions(create_region, self.options)

        def add_location(name: str, code: Optional[int], region: str):
            region: Region = world_regions[region]
            location = SilksongLocation(self.player, name, code, region)
            region.locations.append(location)

        create_locations(add_location, self.options, self.random)
        self.multiworld.regions.extend(world_regions.values())

    def set_rules(self):
        pass
        # set_rules(self.multiworld, self.player, self.options)

    def create_items(self):
        self.precollect_abilities()
        locations_count = len([location
                               for location in self.multiworld.get_locations(self.player)
                               if not location.advancement])

        items_to_exclude = [excluded_items.name
                            for excluded_items in self.multiworld.precollected_items[self.player]]

        created_items = create_items(self.create_item, self.options, locations_count, items_to_exclude, self.random)
        self.multiworld.itempool += created_items

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
        filler_name = self.multiworld.random.choice(item_names_by_groups[ItemGroup.FILLER])
        return filler_name

    def fill_slot_data(self):
        options_dict = self.options.as_dict(
            "death_link"
        )
        options_dict.update({
            "seed": self.random.randrange(99999999)
        })
        return options_dict
