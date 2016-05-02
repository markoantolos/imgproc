import os, sys
import numpy as np
from PIL import Image

from core import BBox, Point
from helpers import is_array, whatis


def ndarray(x):
    tp = whatis(x)
    if tp == 'ndarray':
        return x
    elif tp == 'image':
        return np.array(x)
    elif tp == 'imagearray':
        return x.array
    else:
        return None

def rgba_array(array):
    if not is_array(array):
        array = ndarray(array)
    shape = array.shape
    w, h = shape[:2]
    ret = np.empty((w, h, 4), dtype=np.uint8)
    if len(shape) > 2:
        if shape[2] == 4:
            return array
        r, b, b = shape[2]
        ret[:, :, 0] = r
        ret[:, :, 1] = g
        ret[:, :, 2] = b
        ret[:, :, 3] = 255
        return ret
    ret[:, :, 0] = array
    ret[:, :, 1] = array
    ret[:, :, 2] = array
    ret[:, :, 3] = 255
    return ret

def from_array(value):
    if is_array(value):
        try:
            r = Image.fromarray(value)
            return r
        except Exception as e:
            print(e)
            sys.exit()
    return value

def image(x):
    tp = whatis(x)
    if tp == 'image':
        return x
    elif tp == 'ndarray':
        return Image.fromarray(x)
    elif tp == 'imagearray':
        return Image.fromarray(x.array)
    else:
        return None

