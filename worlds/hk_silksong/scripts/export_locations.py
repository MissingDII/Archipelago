"""Locations export script
This script can be used to export all the AP locations into a json file in the output folder. This file is used by the
tests of the mod to ensure it can handle all possible locations.

To run the script, use `python -m worlds.stardew_valley.scripts.export_locations` from the repository root.
"""

import json
import os

from worlds.hk_silksong import location_data_by_name

if not os.path.isdir("output"):
    os.mkdir("output")

if __name__ == "__main__":
    with open("output/silksong_location_table.json", "w+") as f:
        locations = {
            "Cheat Console":
                {"code": -1, "region": "Archipelago"},
            "Server":
                {"code": -2, "region": "Archipelago"}
        }
        locations.update({
            location_name: {
                "code": location_data.id,
                "region": location_data.region,
                "groups": [group.name for group in location_data.groups],
            }
            for location_name, location_data in location_data_by_name.items()
            if location_data.id is not None
        })
        json.dump({"locations": locations}, f)
