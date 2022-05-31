def get_custom_keycode_definitions(filepath):
    """
    Finds the custom keycodes in the given keycode file.
    """
    custom_keycodes = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('#define'):
                line = line.split(" ", 2)
                custom_keycodes.append({
                    line[1].strip(): line[2].strip()
                })
                    
    return custom_keycodes

def expand_custom_keycode(custom_keycodes, keycode):
    """
    Translates a custom keycode to a keycode.
    """
    for custom_keycode in custom_keycodes:
        if keycode in custom_keycode:
            return custom_keycode[keycode]
    return keycode