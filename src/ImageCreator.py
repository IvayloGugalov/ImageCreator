import os
import random
from typing import Tuple

import numpy
import math

import numpy as np
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

from RectangleProperties import get_symbol_id, get_rectangle_color_outline, \
    try_write_symbol_annotation, get_rectangle_coordinates

from ConvertToYoloFormat import convert_labels

symbols = ['~', ':', '+', '@', '^', '{', '%', '0', '*', '|', ',', '&', '<', '`', '.', '=', '!', '>', ';', '?', '#', '$', '/', '1', '8']

def create_initial_images():
    for num in range(1):
        file_path = 'InitialImages/'
        image = draw_symbols_to_image(num=num, file_path=file_path)
        # image.save(file_path + '{}.jpg'.format(num))
        image.show()

def create_rotated_images():
    for num in range(1):
        file_path = 'RotatedImages/'
        image = draw_symbols_to_image(num=num, file_path=file_path, rotation_angle=45)
        # image.save(file_path + '{}.jpg'.format(num))
        image.show()

def create_images_with_perspective_transformation():
    for num in range(1):
        file_path = 'PerspectiveTransformedImages/'
        image = draw_symbols_to_image(num=num, file_path=file_path)
        # image.save(file_path + '{}.jpg'.format(num))
        image.show()

def draw_symbols_to_image(num, file_path, rotation_angle=0):
    img = Image.new('RGB', (512, 512), (250, 250, 250))
    draw = ImageDraw.Draw(img)
    rows, cols = (5, 5)
    counter = 0

    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(symbols[counter])

            x = 100 * j + random.randint(10, 50)
            y = 100 * i + random.randint(10, 50)

            symbol = str(symbols[random.randint(0, 24)])
            font = ImageFont.truetype('OpenSans-Regular.ttf', random.randint(20, 50))

            # rotated_symbol_img, new_img, symbol_width, symbol_height  = get_rotated_symbol(font, symbol, rotation_angle)
            # rotated_symbol_img_width = rotated_symbol_img.width
            # rotated_symbol_img_height = rotated_symbol_img.height

            im = transform_symbol_with_perspective(font, symbol)

            img.paste(
                im,
                (x,y),
                im)

            # if get_symbol_id(symbol) >= 0:
            #     x1, y1, x2, y2 = get_rectangle_coordinates(
            #         symbol, x, y, rotated_symbol_img_width, rotated_symbol_img_height, symbol_width, symbol_height)
            #
            #     draw.rectangle(
            #         xy=(x1, y1, x2, y2),
            #         outline=get_rectangle_color_outline(symbol),
            #         width=1)
            #
            #     # SAFE COORDINATES TO TXT FILE
            #     save_coordinates_to_file(file_path, num, symbol, x1, y1, x2, y2)

            counter += 1
    return img

def save_coordinates_to_file(file_path, file_name, symbol, x1, y1, x2, y2):
    file_full_path = file_path + '{}.txt'.format(file_name)
    try_write_symbol_annotation(text_file_path=file_full_path, symbol=symbol, x1=x1, y1=y1, x2=x2, y2=y2)

def get_rotated_symbol(font, symbol, angle) -> Tuple[Image.Image, Image.Image, int, int]:
    symbol_size = font.getbbox(symbol)
    (x1, y1, x2, y2) = symbol_size
    x = font.getsize(symbol)[0]
    y = font.getsize(symbol)[1]

    symbol_image = Image.new('RGB', (x, y), (250, 250, 250))
    symbol_draw = ImageDraw.Draw(symbol_image)
    symbol_draw.text(
        #x/2 y/2 : draw in the center
        xy=(x/2, y/2),
        font=font,
        text=symbol,
        fill=(0, 0, 0),
        anchor="mm"
    )
    rotated_img = symbol_image.rotate(angle=angle, expand=True, fillcolor=(250, 250, 250))

    angle_sine = math.fabs(math.sin(math.radians(angle)))

    #Switching the width and height for better accuracy depending on the angle
    if ((angle_sine > 0.5) & (angle_sine < 1)) | (angle==270 | angle==90):
        return rotated_img, symbol_image, symbol_image.height-y1, symbol_image.width-x1

    return rotated_img, symbol_image, symbol_image.width-x1, symbol_image.height-y1


def transform_symbol_with_perspective(font, symbol):
    symbol_size = font.getbbox(symbol)
    (x1, y1, x2, y2) = symbol_size
    x = font.getsize(symbol)[0]
    y = font.getsize(symbol)[1]

    symbol_image = Image.new('RGB', (x, y), (250, 250, 250))
    symbol_draw = ImageDraw.Draw(symbol_image)
    symbol_draw.text(
        # x/2 y/2 : draw in the center
        xy=(x / 2, y / 2),
        font=font,
        text=symbol,
        fill=(0, 0, 0),
        anchor="mm"
    )
    width, height = symbol_image.size

    m = 0.3
    x_shift = abs(m) * width
    new_width = width + int(round(x_shift))
    new_size = (int(width+width*0.3), int(height+height*0.3))
    symbol_image = symbol_image.resize(new_size)
    return symbol_image.transform(size=(new_width, height), method=Image.AFFINE,
        data=(1, m, -x_shift if m > 0 else 0, 0, 1, 0), resample=Image.BICUBIC)

# def draw_symbols_to_image(num, file_path):
#     img = Image.new('RGB', (512,512), (250,250,250))
#     draw = ImageDraw.Draw(img)
#     rows, cols = (5, 5)
#     counter = 0
#
#     for i in range(rows):
#         col = []
#         for j in range(cols):
#             col.append(symbols[counter])
#
#             symbol = str(symbols[random.randint(0, 24)])
#             font = ImageFont.true_type('OpenSans-Regular.ttf', random.randint(20, 50))
#             text_size = font.getsize(symbol)
#
#             x = 100 * j + random.randint(10, 50)
#             y = 100 * i + random.randint(10, 50)
#
#             (x1, y1, x2, y2) = rectangle_get_coordinates(symbol, x, y, text_size[0], text_size[1])
#             draw.text(
#                 xy=(x, y),
#                 text=symbol,
#                 fill=(0, 0, 0),
#                 font=font)
#
#             if get_symbol_id(symbol) >= 0:
#                 draw.rectangle(xy=(x1, y1, x2, y2), outline=get_rectangle_color_outline(symbol), width=1)
#
#             text_file_path = file_path + '{}.txt'.format(num)
#             try_write_symbol_annotation(text_file_path=text_file_path, symbol=symbol, x1=x1, y1=y1, x2=x2, y2=y2)
#
#             counter += 1
#
#     return img


