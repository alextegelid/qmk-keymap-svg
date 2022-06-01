import re
import sys
import settings

def parse_keymap(filecontents):
    # Find the beginning of the keymap definition
    start_marker_pos = filecontents.find("[MATRIX_ROWS][MATRIX_COLS]")

    if start_marker_pos == -1:
        print("The keymap definition was not found in the keymap file.")
        sys.exit(1)

    start_pos = filecontents.find("\n", start_marker_pos)
    end_pos = filecontents.find("}", start_pos + 1) - 1
    keymap_extracted = filecontents[start_pos:end_pos]

    keymap_rows = keymap_extracted.split("\n")
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
                "thumbs_left": [],
                "thumbs_right": [],
            }
            continue
        else:
            keys = prepare_row(row)
            if not keys:
                continue

            if current_layer_row == settings.hand_rows:
                keymap[current_layer]["thumbs_left"].append(keys[0:settings.hand_thumbs_cols])
                keymap[current_layer]["thumbs_right"].append(keys[settings.hand_thumbs_cols:settings.hand_thumbs_cols*2])
                continue

            keymap[current_layer]["left"].append(keys[0:settings.hand_cols])
            keymap[current_layer]["right"].append(keys[settings.hand_cols:settings.hand_cols*2])
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