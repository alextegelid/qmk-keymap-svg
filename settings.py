hand_cols = 5
hand_rows = 3
hand_thumbs_cols = 2

debug = False

key_w = 80
key_h = 65
key_rx = 5
key_ry = 5
inner_pad_w = 5
inner_pad_h = 5
outer_pad_w = 40
outer_pad_h = 40

font_size = 16
line_spacing = font_size * 1.2

# Auto capitalize keycodes that is not in the labels list.
# Keycodes that includes an underscore will not be capitalized.
auto_capitalize_keycode = True

# Define keys that should appear as dimmed.
# Use original raw keycodes before they are filtered and converted to labels.
# Eg. KC_NO and KC_TRNS
dim_keycodes = [
    "KC_NO",
    "KC_TRNS",
    "_______",
    "XXXXXXX",
]

# Define keycode prefixes that should be stripped from the keycode. The prefix 
# will be replaced before the keycode is replaces with a label.
keycode_prefixes = [
    "KC_",
    "SE_",
]

parse_custom_keycodes = True
search_included_header_files = True