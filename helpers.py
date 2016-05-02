from PIL import Image
import numpy as np
import sys

def is_array(x):
    return type(x).__module__ == np.__name__

def whatis(x):
    t = type(x)
    s = str(t)
    if t.__module__ == np.__name__:
        return 'ndarray'
    elif 'ImageArray' in s:
        return 'imagearray'
    elif t == Image.Image:
        return 'image'

