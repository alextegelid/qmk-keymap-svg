import re

def parse_hold_action(key):
    # Layer toggle
    if key.startswith("LT(") and key.endswith(")"):
        key = key[3:-1]
        key = key.split(",")

        return {
            "key": key[1],
            "hold-key": key[0],
            "class": "has-hold-action",
            "type": "layer",
        }

    # Default layer
    df_toggle = re.findall(r"(DF)\((\w+)", key)
    if df_toggle:
        df = df_toggle[0]
        return {
            "key": df[0] + " " + df[1],
            "hold-key": "",
            "class": "default-layer",
            "type": "",
        }
        
    # Find mod-tap XXXX_T(...). Eg. LGUI_T(KC_A)
    mods = re.findall(r"([A-Z]+)(_T)\(([A-Z_]+)", key)
    if mods:
        mod = mods[0]
        return {
            "key": mod[2],
            "hold-key": mod[0],
            "class": "has-hold-action",
            "type": "mod-tap",
        }

    # Find modifiers XXXX(...). Eg. LCTL(KC_LALT)
    mods = re.findall(r"([A-Z]+)\(([A-Z_]+)", key)
    if mods:
        mod = mods[0]
        return mod[0] + " +" + mod[1]

    # Last resort. Return the key as is.
    return key