# Draw an svg image from keymap.c
Derived from [callum-oakley/keymap](https://github.com/callum-oakley/keymap) this adaptation takes the keymap.c as an argument and parses it to generate the svg.

Currently only works with the layout of the Ferris Sweep keyboard.

## Usage
`> python3 draw.py path/to/keymap.c`

## Todo
[ ] Parse layer toggles
[ ] Find and parse custom keycodes
[X] Make sure whitespace inside parentheses is ignored