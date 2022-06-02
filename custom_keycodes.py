from os.path import exists, dirname, realpath

# Import the user settings file or the default one
if exists("settings_user.py"):
    import settings_user as settings
else:
    import settings_default as settings

def get_custom_keycode_definitions(filepath):
    """
    Finds the custom keycodes in the given keycode file.
    """
    
    base_dir = dirname(realpath(filepath))
    filepaths = [filepath]

    # Find the included header files
    if settings.search_included_header_files:
        included_header_files = find_included_header_files(filepath)
        filepaths += included_header_files

    custom_keycodes = {}
    for filepath in filepaths:
        # Add the base dir if it's not already there
        if not base_dir in filepath:
            filepath = base_dir + "/" + filepath

        # Skip if the file doesn't exist
        if not exists(filepath):
            continue
        
        # Read the file
        with open(filepath, 'r') as f:
            for line in f:
                if line.startswith('#define'):
                    line = line.split(" ", 2)
                    custom_keycodes[line[1].strip()] = line[2].strip()
                    
    return custom_keycodes

def find_included_header_files(filepath):
    """
    Finds the included header files in the given file.
    """
    included_header_files = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#include') and line.endswith('.h"'):
                line = line.split(" ", 2)
                included_header_files.append(line[1].strip('"').strip())
                    
    return included_header_files

def expand_custom_keycodes(keymap, custom_keycodes):
    for layer_name, layer in keymap.items():
        for block_name, block in layer.items():
            for row_index, row in enumerate(block):
                for key_index, key in enumerate(row):
                    if key in custom_keycodes:
                        keymap[layer_name][block_name][row_index][key_index] = custom_keycodes[key]

    return keymap

def expand_custom_keycode(custom_keycodes, keycode):
    """
    Translates a custom keycode to a keycode.
    """
    if keycode in custom_keycodes:
        return custom_keycodes[keycode]
    return keycode