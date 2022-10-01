# Define column and row count
hand_cols = 5
hand_rows = 3
hand_thumbs_cols = 2

# Misc settings
parse_custom_keycodes = True # Set to False if you don't want to parse custom keycodes
search_included_header_files = True # Search for included header files in the same directory as the keymap file
debug = False # Debug mode prints the SVG to stdout
auto_capitalize_keycode = True # Auto capitalize keycodes that is not in the labels list. Keycodes that includes an underscore will not be capitalized.
mark_homing_keys = False # Mark keys that are used as homing keys

# Define global meassurements in pixels
key_w = 75
key_h = 65
key_rx = 5
key_ry = 5
inner_pad_w = 5 # Padding between keys horizontally
inner_pad_h = 5 # Padding between keys vertically
middle_pad_w = 150 # Padding between left and right hand
layer_pad_w = 0 # Padding on the outer layer edges
layer_pad_h = 150 # Padding between layers

# Column stagger values as percentage of the key height,
# counting from the outer edge of the board
column_stagger = [
    60,
    -10,
    -40,
    -10,
    0,
]

# Thumb cluster offset as percentage of the key width and height, 
# counting from the outer edge of the board
thumb_offset = {
    "x": 40,
    "y": 15,
}

font_size = 14
line_spacing = font_size * 1.2

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

# Exclude custom keycodes from being replaced with default ones.
untouched_custom_keycodes = [
    # "EXAMPLE_KEYCODE",
]