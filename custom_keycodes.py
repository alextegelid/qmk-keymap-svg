import settings
from os.path import exists, dirname, realpath

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

    custom_keycodes = []
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
                    custom_keycodes.append({
                        line[1].strip(): line[2].strip()
                    })
                    
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

def expand_custom_keycode(custom_keycodes, keycode):
    """
    Translates a custom keycode to a keycode.
    """
    for custom_keycode in custom_keycodes:
        if keycode in custom_keycode:
            return custom_keycode[keycode]
    return keycode