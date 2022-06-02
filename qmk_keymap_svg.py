import sys
import settings
import style

from labels import get_label
from html import escape
from parse_keymap import parse_keymap
from parse_key_action import parse_key_action
from custom_keycodes import get_custom_keycode_definitions, expand_custom_keycodes
from layer_toggles import get_layer_toggles


# TODO: Move calculation of exact key positioning and size into a separate function

# Exit if there are no arguments
if len(sys.argv) != 2:
    print("Usage: qmk_keymap_svg.py keymap.c")
    sys.exit(1)

# Get the filename from the first argument
FILENAME = sys.argv[1]

# Read file
f = open(FILENAME, "r")
filecontents = f.read()

KEYMAP = parse_keymap(filecontents)

custom_keycodes = []
if settings.parse_custom_keycodes:
    custom_keycodes = get_custom_keycode_definitions(FILENAME)
    KEYMAP = expand_custom_keycodes(KEYMAP, custom_keycodes)

LAYER_TOGGLES = get_layer_toggles(KEYMAP)

def filter_key_word(string):
    for prefix in settings.keycode_prefixes:
        string = string.replace(prefix, "")

    key_label = get_label(string)
    if "_" not in key_label and settings.auto_capitalize_keycode:
        key_label = key_label.title()

    return key_label


def print_key(x, y, key, blockname, row_index, key_index, layername):
    key_class = ""
    key_hold_name = ""
    key_hold_type = ""
    key_label_classes = []
    key = parse_key_action(key)

    column_stagger_value = 0
    if blockname == "left":
        column_stagger_value = (settings.column_stagger[key_index] * settings.key_h / 100) if key_index <= len(settings.column_stagger) else 0
    elif blockname == "right":
        column_stagger_value = (settings.column_stagger[-1 - key_index] * settings.key_h / 100) if key_index <= len(settings.column_stagger) else 0

    y = y + column_stagger_value


    if type(key) is dict:
        key_class = key["class"] if "class" in key else ""
        key_hold_name = key["hold-key"] if "hold-key" in key else ""
        key_name = key["key"] if "key" in key else ""
        key_hold_type = key["type"] if "type" in key else "no-hold"
    else:
        key_name = key

    # Override key info if it's a held layer toggle
    if layername in LAYER_TOGGLES and key_index == LAYER_TOGGLES[layername]["key_index"] and row_index == LAYER_TOGGLES[layername]["row_index"] and blockname == LAYER_TOGGLES[layername]["block"]:
        key_class += " layer-toggle-held"
        key_label_classes.append("layer-toggle-held")
        key_hold_name = LAYER_TOGGLES[layername]["block"]
        key_hold_type = "block"
        key_name = layername

    print(
        f'<rect rx="{settings.key_rx}" ry="{settings.key_ry}" x="{x + settings.inner_pad_w}" y="{y + settings.inner_pad_h}" width="{settings.key_w}" height="{settings.key_h}" class="{key_class}" />'
    )

    if key_name in settings.dim_keycodes:
        key_label_classes.append("label-dim")
    
    key_name = filter_key_word(key_name)
    key_label_classes_str = " ".join(key_label_classes)

    words = key_name.split()
    label_y = y + KEYSPACE_H / 2

    if key_hold_type == "mod-tap":
        hold_action_font_size = settings.font_size * 0.75
        hold_action_y = y + KEYSPACE_H - hold_action_font_size
        print(
            f'<text text-anchor="middle" font-size="{settings.font_size}" class="{key_label_classes_str}" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{label_y}">{escape(key_name)}</text>'
        )
        print(
            f'<text text-anchor="middle" font-size="{hold_action_font_size}" class="{key_label_classes_str} hold-action -{key_hold_type}" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{hold_action_y}">{escape(key_hold_name)}</text>'
        )

    if key_hold_type == "layer":
        hold_action_font_size = settings.font_size * 0.75
        label_bg_height = hold_action_font_size * 1.2
        hold_action_y = y + KEYSPACE_H - settings.inner_pad_h - label_bg_height/2
        print(
            f'<text text-anchor="middle" font-size="{settings.font_size}" class="{key_label_classes_str}" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{label_y}">{escape(key_name)}</text>'
        )
        print(
           f'<rect rx="{settings.key_rx}" ry="{settings.key_ry}" x="{x + settings.inner_pad_w}" y="{y + settings.key_h + settings.inner_pad_w - label_bg_height}" width="{settings.key_w}" height="{label_bg_height}" class="layer-rect" />'
        )
        print(
            f'<text text-anchor="middle" font-size="{hold_action_font_size}" class="hold-action -{key_hold_type}" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{hold_action_y}">{escape(key_hold_name)}</text>'
        )

    else:
        label_y = y + (KEYSPACE_H - (len(words) - 1) * settings.line_spacing) / 2
        for word in key_name.split():
            print(
                f'<text text-anchor="middle" font-size="{settings.font_size}" class="{key_label_classes_str}" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{label_y}">{escape(word)}</text>'
            )
            label_y += settings.line_spacing


def print_row(x, y, row, blockname, row_index, layername):
    for key_index, key in enumerate(row):
        print_key(x, y, key, blockname, row_index, key_index, layername)
        x += KEYSPACE_W


def print_block(x, y, blockname, layername):
    block = KEYMAP[layername][blockname]
    for row_index, row in enumerate(block):
        print_row(x, y, row, blockname, row_index, layername)
        y += KEYSPACE_H


def print_layer(x, y, layername):
    layer = KEYMAP[layername]

    # Print the layer name
    print(
        f'<text text-anchor="middle" font-size="{settings.font_size*1.5}" dominant-baseline="middle" x="{BOARD_W / 2}" y="{y}">{escape(layername)}</text>'
    )

    y += settings.font_size * 1.5
    
    # Print the left side
    print_block(
        x,
        y,
        "left",
        layername
    )

    # Print the right side
    print_block(
        x + HAND_W + settings.middle_pad_w,
        y,
        "right",
        layername
    )

    # Print the left thumb cluster
    print_block(
        x + (settings.hand_cols - settings.hand_thumbs_cols) * KEYSPACE_W + (settings.thumb_offset["x"] * KEYSPACE_W / 100),
        y + settings.hand_rows * KEYSPACE_H + (settings.thumb_offset["y"] * KEYSPACE_H / 100),
        "thumbs_left",
        layername
    )

    # Print the right thumb cluster
    print_block(
        x + HAND_W + settings.middle_pad_w - (settings.thumb_offset["x"] * KEYSPACE_W / 100),
        y + settings.hand_rows * KEYSPACE_H + (settings.thumb_offset["y"] * KEYSPACE_H / 100),
        "thumbs_right",
        layername
    )


def print_board(x, y, keymap):
    x += settings.outer_pad_w
    for layername in keymap:
        y += settings.layer_pad_h
        print_layer(x, y, layername)
        y += LAYER_H


# Define global meassurements
KEYSPACE_W = settings.key_w + 2 * settings.inner_pad_w
KEYSPACE_H = settings.key_h + 2 * settings.inner_pad_h
HAND_W = settings.hand_cols * KEYSPACE_W
HAND_H = (settings.hand_rows + 1) * KEYSPACE_H + settings.font_size * 1.5
LAYER_W = 2 * HAND_W + settings.middle_pad_w
LAYER_H = HAND_H
BOARD_W = LAYER_W + 2 * settings.outer_pad_w
BOARD_H = len(KEYMAP) * LAYER_H + (len(KEYMAP) + 1) * settings.layer_pad_h

# If debug isn't enabled, route the output to keymap.svg
if settings.debug is False:
    orig_stdout = sys.stdout
    f = open("keymap.svg", "w")
    sys.stdout = f

# Start the output
print(
    f'<svg width="{BOARD_W}" height="{BOARD_H}" viewBox="0 0 {BOARD_W} {BOARD_H}" xmlns="http://www.w3.org/2000/svg">'
)
print(f"<style>{style.STYLE}</style>")
print_board(0, 0, KEYMAP)
print("</svg>")

# If debug isn't enabled, close the file and redirect output back to stdout
if settings.debug is False:
    sys.stdout = orig_stdout
    f.close()