import sys
import settings
import style

from labels import get_label
from html import escape
from parse_keymap import parse_keymap
from parse_hold_action import parse_hold_action

# Exit if there are no arguments
if len(sys.argv) != 2:
    print("Usage: draw.py keymap.c")
    sys.exit(1)

# Get the filename from the first argument
FILENAME = sys.argv[1]

# Read file
f = open(FILENAME, "r")
filecontents = f.read()

# Find the beginning of the keymap definition
start_marker_pos = filecontents.find("[MATRIX_ROWS][MATRIX_COLS]")

if start_marker_pos == -1:
    print("The keymap definition was not found in the keymap.")
    sys.exit(1)

start_pos = filecontents.find("\n", start_marker_pos)
end_pos = filecontents.find("}", start_pos + 1) - 1
keymap_extracted = filecontents[start_pos:end_pos]

keymap_rows = keymap_extracted.split("\n")

KEYMAP = parse_keymap(keymap_rows)

def held(key):
    return {"key": key, "class": "held"}


def filter_key_word(string):
    stripped_keycode = string\
        .replace("KC_", "")\
        .replace("SE_", "")

    keylabel = get_label(stripped_keycode)
    return get_label(keylabel)


def print_key(x, y, key):
    key_class = ""
    key_hold_name = ""
    key_hold_type = ""
    key = parse_hold_action(key)

    print

    if type(key) is dict:
        key_class = key["class"] if "class" in key else ""
        key_hold_name = key["hold-key"] if "hold-key" in key else ""
        key_name = key["key"] if "key" in key else ""
        key_hold_type = key["type"] if "type" in key else "no-hold"
    else:
        key_name = key

    print(
        f'<rect rx="{settings.key_rx}" ry="{settings.key_ry}" x="{x + settings.inner_pad_w}" y="{y + settings.inner_pad_h}" width="{settings.key_w}" height="{settings.key_h}" class="{key_class}" />'
    )
    
    words = key_name.split()
    label_y = y + KEYSPACE_H / 2

    if key_hold_type == "mod-tap":
        hold_action_font_size = settings.font_size * 0.8
        hold_action_y = y + KEYSPACE_H - hold_action_font_size
        print(
            f'<text text-anchor="middle" font-size="{settings.font_size}" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{label_y}">{escape(filter_key_word(key_name))}</text>'
        )
        print(
            f'<text text-anchor="middle" font-size="{hold_action_font_size}" class="hold-action -{key_hold_type}" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{hold_action_y}">{escape(key_hold_name)}</text>'
        )

    elif key_hold_type == "default-layer":
        label_y = y + (KEYSPACE_H - (len(words) - 1) * settings.line_spacing) / 2
        for word in key_name.split():
            print(
                f'<text text-anchor="middle" font-size="{settings.font_size}" class="default-layer" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{label_y}">{escape(filter_key_word(word))}</text>'
            )
            label_y += settings.line_spacing

    else:
        label_y = y + (KEYSPACE_H - (len(words) - 1) * settings.line_spacing) / 2
        for word in key_name.split():
            print(
                f'<text text-anchor="middle" font-size="{settings.font_size}" dominant-baseline="middle" x="{x + KEYSPACE_W / 2}" y="{label_y}">{escape(filter_key_word(word))}</text>'
            )
            label_y += settings.line_spacing


def print_row(x, y, row):
    for key in row:
        print_key(x, y, key)
        x += KEYSPACE_W


def print_block(x, y, block):
    for row in block:
        print_row(x, y, row)
        y += KEYSPACE_H


def print_layer(x, y, layername):

    layer = KEYMAP[layername]

    # Print the layer name
    print(
        f'<text text-anchor="middle" font-size="{settings.font_size*1.5}" dominant-baseline="middle" x="{BOARD_W / 2}" y="{y}">{escape(layername)}</text>'
    )

    y += settings.font_size * 1.5
    
    print_block(
        x,
        y,
        layer["left"]
    )
    print_block(
        x + HAND_W + settings.outer_pad_w,
        y,
        layer["right"],
    )
    print_row(
        x + 3 * KEYSPACE_W,
        y + 3 * KEYSPACE_H,
        layer["thumbs"]["left"],
    )
    print_row(
        x + HAND_W + settings.outer_pad_w,
        y + 3 * KEYSPACE_H,
        layer["thumbs"]["right"],
    )


def print_board(x, y, keymap):
    x += settings.outer_pad_w
    for layername in keymap:
        y += settings.outer_pad_h
        print_layer(x, y, layername)
        y += LAYER_H



KEYSPACE_W = settings.key_w + 2 * settings.inner_pad_w
KEYSPACE_H = settings.key_h + 2 * settings.inner_pad_h
HAND_W = settings.hand_cols * KEYSPACE_W
HAND_H = (settings.hand_rows + 1) * KEYSPACE_H + settings.font_size * 1.5
LAYER_W = 2 * HAND_W + settings.outer_pad_w
LAYER_H = HAND_H
BOARD_W = LAYER_W + 2 * settings.outer_pad_w
BOARD_H = len(KEYMAP) * LAYER_H + (len(KEYMAP) + 1) * settings.outer_pad_h

if settings.debug is False:
    orig_stdout = sys.stdout
    f = open("keymap.svg", "w")
    sys.stdout = f

print(
    f'<svg width="{BOARD_W}" height="{BOARD_H}" viewBox="0 0 {BOARD_W} {BOARD_H}" xmlns="http://www.w3.org/2000/svg">'
)
print(f"<style>{style.STYLE}</style>")
print_board(0, 0, KEYMAP)
print("</svg>")

if settings.debug is False:
    sys.stdout = orig_stdout
    f.close()