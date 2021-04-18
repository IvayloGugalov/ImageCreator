from Convert_To_Yolo_Format import convert_labels

special_symbols = {
	'0': 0,
	'%': 1,
	'@': 2,
	'/': 3,
	'|': 4,
	'=': 5,
	'!': 6,
	'.': 7,
	'&': 8,
	'?': 9
}

def get_symbol_id(symbol):
    if symbol in special_symbols.keys():
        return special_symbols.get(symbol)
    else: 
        return -1

def try_write_symbol_annotation(text_file_path, symbol, x1, y1, x2, y2):
    symbol_id = get_symbol_id(symbol)

    if symbol_id < 0:
        return
    else:
        (x_center_norm, y_center_norm, width_norm, height_norm) = convert_labels(x1, y1, x2, y2)

        with open(text_file_path, "a") as file:
            file.write("{symbol_id} {x_center_norm} {y_center_norm} {width_norm} {height_norm}\n"
                .format(symbol_id=symbol_id, x_center_norm=x_center_norm, y_center_norm=y_center_norm, width_norm=width_norm, height_norm=height_norm))

def rectangle_get_coordinates(symbol, x, y, text_size_x, text_size_y):
    x_top_point = x - 2
    x_lower_point = x + text_size_x + 2
    y_lower_point = y + text_size_y + 2
    # ImageDraw.text has margins on the text that is drawn, so we are compensating it here
    if symbol == '.':
        y_top_point = y + (y_lower_point - y) * 0.8
    elif symbol == '=':
        y_top_point = y + (y_lower_point - y) * 0.5 - 3
        y_lower_point = y_lower_point - (y_lower_point - y_top_point) * 0.25
    else:
        y_top_point = y + (y_lower_point - y) * 0.3 - 3

    return (x_top_point, y_top_point, x_lower_point, y_lower_point)
    # return ((x_top_point, y_top_point), (x_lower_point, y_lower_point))

def rectangle_color_outline(symbol):
    if symbol in special_symbols.keys():
        switcher = {
            # Red
            '0': (255, 0, 0),
            # Green
            '%': (0, 255, 0),
            # Blue
            '@': (0, 0, 255),
            # Yellow
            '/': (255, 255, 0),
            # Cyan
            '|': (0, 255, 255),
            # Orange
            '=': (255, 180, 0),
            # Purple
            '!': (160, 25, 100),
            # Brown
            '.': (140, 80, 10),
            # Grey
            '&': (96, 96, 96),
            # Pink
            '?': (255, 50, 255)
        }
        return switcher.get(symbol)

    else:
        return ()
