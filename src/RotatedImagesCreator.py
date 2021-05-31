import math
import operator
import random

from PIL import Image, ImageFont, ImageDraw
from typing import Tuple

from src.RectangleProperties import rectangle_get_coordinates, get_symbol_id, get_rectangle_color_outline, get_rectangle_coordinates

symbols = ['~', ':', '+', '@', '^', '{', '%', '0', '*', '|', ',', '&', '<', '`', '.', '=', '!', '>', ';', '?', '#', '$', '/', '1', '8']
true_sym = ['0', '%' ,'@','/','|','=', '!','.','&','?']


