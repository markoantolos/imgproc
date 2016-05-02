import os, sys, subprocess
from random import randint
import numpy as np
from PIL import Image, JpegImagePlugin

from core import BBox, Point
import conversion
import slicing

def threshold(array, value=120):
    array[array <= value] = 0
    array[array > value] = 255
    return array

def invert(array):
    return np.invert(array)

def binary(array):
    array[array <= 1] = 0
    array[array > 1] = 1
    return array

def paste(src, b1, dest, b2):
    pass

def show(im, directory, ftype='png'):
    path = os.path.join(directory, 'last.%s' % ftype)
    tp = 'PNG' if ftype == 'png' else 'JPEG'
    im.save(path, tp)
    subprocess.call(['feh', path])

def show2(image, directory, ftype='png'):
    path = os.path.join(directory, 'last.%s' % ftype)
    im = conversion.from_array(image).convert('RGB')

    tp = 'PNG' if ftype == 'png' else 'JPEG'
    im.save(path, tp)
    subprocess.call(['feh', path])

def get_shape(image):
    if isinstance(image, Image.Image):
        return image.size
    else:
        return image.shape[1], image.shape[0]


