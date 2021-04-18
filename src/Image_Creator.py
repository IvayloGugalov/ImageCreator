import os
import random
import numpy

from PIL import Image, ImageFont, ImageDraw, ImageEnhance

from Rectangle_Properties import get_symbol_id, rectangle_color_outline, rectangle_get_coordinates, try_write_symbol_annotation
from Convert_To_Yolo_Format import convert_labels

symbols = ['~', ':', '+', '@', '^', '{', '%', '0', '*', '|', ',', '&', '<', '`', '.', '=', '!', '>', ';', '?', '#', '$', '/', '1', '8']

def create_initial_images():
    for num in range(1):
        file_path = 'InitialImages/'
        image = draw_symbols_to_image(num=num, file_path=file_path)
        image.save(file_path + '{}.jpg'.format(num))

def create_rotated_images():
    for num in range(50):
        file_path = 'RotatedImages/'
        image = draw_symbols_to_image(num=num, file_path=file_path)
        image.rotate(270).save(file_path + '{}.jpg'.format(num))

def draw_symbols_to_image(num, file_path):
    img = Image.new('RGB', (512,512), (250,250,250))
    draw = ImageDraw.Draw(img)
    rows, cols = (5, 5)
    counter = 0

    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(symbols[counter])

            symbol = str(symbols[random.randint(0, 24)])
            font = ImageFont.truetype('OpenSans-Regular.ttf', random.randint(20, 50))
            textSize = font.getsize(symbol)

            x = 100 * j + random.randint(10, 50)
            y = 100 * i + random.randint(10, 50)

            draw.text(
                xy=(x, y),
                text=symbol,
                fill=(0, 0, 0),
                font=font)

            (x1, y1, x2, y2) = rectangle_get_coordinates(symbol, x, y, textSize[0], textSize[1])

            if get_symbol_id(symbol) >= 0:
                draw.rectangle(xy=((x1, y1), (x2, y2)), outline=rectangle_color_outline(symbol), width=1)
            
            text_file_path = file_path + '{}.txt'.format(num)
            try_write_symbol_annotation(text_file_path=text_file_path, symbol=symbol, x1=x1, y1=y1, x2=x2, y2=y2)

            counter += 1

    return img
