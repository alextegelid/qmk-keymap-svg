def get_label(keycode):
    return keylabels[keycode] if keycode in keylabels else keycode

keylabels = {
    "XXXXXXX": "———",
    "_______": "▽",
    "ODIA": "Ö",
    "MINS": "-",
    "MINUS": "-",
    "COMM": ",",
    "COMMA": ",",
    "COLON": ":",
    "COLN": ":",
    "SCLN": ";",
    "SEMICOLON": ";",
    "DOT": ".",
    "QUES": "?",
    "EXLM": "!",
    "QUOT": "'",
    "QUOTE": "'",
    "AT": "@",
    "LPRN": "(",
    "RPRN": ")",
    "LCBR": "{",
    "RCBR": "}",
    "LABK": "<",
    "RABK": ">",
    "LBRC": "[",
    "LEFT_BRACKET": "[",
    "RBRC": "]",
    "RIGHT_BRACKET": "]",
    "SLASH": "/",
    "SLSH": "/",
    "BACKSLASH": "\\",
    "BSLS": "\\",
    "GRAVE": "`",
    "GRV": "`",
    "PLUS": "+",
    "PERC": "%",
    "PPLS": "+",
    "PMNS": "-",
    "PEQL": "=",
    "PSLS": "/",
    "PAST": "*",
    "EQL": "=",
    "EQUAL": "=",
    "CIRC": "^",
    "ASTR": "*",
    "AMPR": "&",
    "HASH": "#",
    "TILD": "~",
    "UNDS": "_",
    "PIPE": "|",
    "DQUO": "\"",
    "DLR": "$",
    "BACKSPACE": "Bsps",
    "BSPC": "Bsps",
    "ESC": "Esc",
    "ESCAPE": "Esc",
    "ENTER": "Enter",
    "ENT": "Enter",
    "LSFT": "Shift",
    "LGUI": "CMD",
    "NONUS_BACKSLASH": "Non-US \ and |",
    "NUBS": "Non-US \ and |",
    "NONUS_HASH": "Non-US # and ~",
    "NUHS": "Non-US # and ~",
    "RIGHT": "→",
    "RGHT": "→",
    "LEFT": "←",
    "DOWN": "↓",
    "UP": "↑",
    "PGDN": "PgDn",
    "PGUP": "PgUp",
    "CAPSWORD": "Caps Word",
}