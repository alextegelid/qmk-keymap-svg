# Draw an svg image from your QMK keymap.c file
Derived from [callum-oakley/keymap](https://github.com/callum-oakley/keymap) this adaptation takes the keymap.c as an argument and parses it to generate the svg.

This is very much a work in progress. If you have any suggestions, please open a PR or an issue.

Currently only works with the layout of the Ferris Sweep keyboard.

## Usage
```
python3 draw.py path/to/keymap.c
```
The `keymap.svg` file will be saves (or overwritten) in the same folder as `draw.py`. 

## Todo
- [X] Parse and show layer toggles
- [ ] Show held layer toggles on the correct layer
- [ ] Find and parse custom keycodes
- [X] Find and parse mod-tap and modifier keys
- [X] Show default layer keys
- [X] Make sure whitespace inside parentheses is ignored