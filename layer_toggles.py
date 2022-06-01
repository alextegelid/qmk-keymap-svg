def get_layer_toggles(keymap):
    layer_toggles = {}
    for layer_name, layer in keymap.items():
        for block_name, block in layer.items():
            for row_index, row in enumerate(block):
                for key_index, key in enumerate(row):
                    if key.startswith("LT("):
                        toggle_data = key[3:-1].split(",")
                        layer_toggles[toggle_data[0]] = {
                            "block": block_name,
                            "row_index": row_index,
                            "key_index": key_index,
                        }
    return layer_toggles