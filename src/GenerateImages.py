from PIL import Image, ImageFont, ImageDraw, ImageEnhance

from Image_Creator import create_initial_images, create_rotated_images

import os
import random
import numpy

# 25 symbols
symbols = ['~', ':', '+', '@', '^', '{', '%', '0', '*', '|', ',', '&', '<', '`', '.', '=', '!', '>', ';', '?', '#', '$', '/', '1', '8']
special_symbols = ['0', '%', '@', '/', '|', '=', '!', '.', '&', '?']

create_initial_images()
