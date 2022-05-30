# Draw an svg image from keymap.c
Derived from [callum-oakley/keymap](https://github.com/callum-oakley/keymap) this adaptation takes the keymap.c as an argument and parses it to generate the svg.

Currently only works with the layout of the Ferris Sweep keyboard.

## Usage
`> python3 draw.py path/to/keymap.c`

## Todo
- [ ] Parse and show layer toggles
- [ ] Show held layer toggles on the correct layer
- [ ] Find and parse custom keycodes
- [X] Find and parse mod-tap and modifier keys
- [X] Show default layer keys
- [X] Make sure whitespace inside parentheses is ignored