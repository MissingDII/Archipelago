"""Items export script
This script can be used to export all the AP items into a json file in the output folder. This file is used by the tests
of the mod to ensure it can handle all possible items.

To run the script, use `python -m worlds.stardew_valley.scripts.export_items` from the repository root.
"""

import json
import os.path

from worlds.hk_silksong import item_data_by_name

if not os.path.isdir("output"):
    os.mkdir("output")

if __name__ == "__main__":
    with open("output/silksong_item_table.json", "w+") as f:
        items = {
            item_name: {
                "code": item_data.id,
                "classification": item_data.classification.name
            }
            for item_name, item_data in item_data_by_name.items()
            if item_data.id is not None and item_data.id >= 0
        }
        json.dump({"items": items}, f)
