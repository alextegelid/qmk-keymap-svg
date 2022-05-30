import sys
import re

def parse_keymap(keymap_rows):
    # Parse the keymap.
    keymap = {}
    current_layer = ""
    current_layer_row = 0

    for row in keymap_rows:
        row = row.strip()

        # Skip layer closing lines.
        if row.startswith(")"):
            continue

        # Get the layer name.
        if (re.search("^\[(.*?)\]", row)):
            layername = re.findall("^\[(.*?)\]", row)
            current_layer = layername[0]
            current_layer_row = 0
             
            if (current_layer is None):
                continue

            keymap[current_layer] = {
                "left": [],
                "right": [],
                "thumbs": {
                    "left": [],
                    "right": [],
                },
            }
            continue
        else:
            keys = prepare_row(row)
            if not keys:
                continue

            if current_layer_row == 3:
                keymap[current_layer]["thumbs"]["left"] = keys[0:2]
                keymap[current_layer]["thumbs"]["right"] = keys[2:4]
                continue

            keymap[current_layer]["left"].append(keys[0:5])
            keymap[current_layer]["right"].append(keys[5:10])
            current_layer_row += 1


    return keymap

def prepare_row(row):
    # Remove whitespace inside parenthesis.
    safe_row = re.sub(r'\(.*?\)', lambda x: ''.join(x.group(0).split()), row)

    # Split the string in row by space. 
    keys = []
    for key in safe_row.split():
        # Trim unnecessary whitespace and commas.
        keys.append(key.strip("\t\n\r,"))
    return keys