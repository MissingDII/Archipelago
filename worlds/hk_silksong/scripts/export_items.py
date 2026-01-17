"""Items export script
This script can be used to export all the AP items into a json file in the output folder. This file is used by the tests
of the mod to ensure it can handle all possible items.

To run the script, use `python -m worlds.stardew_valley.scripts.export_items` from the repository root.
"""

import json
import os.path

from worlds.hk_silksong.items import all_items

if not os.path.isdir("output"):
    os.mkdir("output")

if __name__ == "__main__":
    with open("output/silksong_item_table.json", "w+") as f:
        items = {
            item.name: {
                "code": item.id,
                "classification": item.classification.name
            }
            for item in all_items
            if item.id is not None
        }
        json.dump({"items": items}, f)
