import os, sys, types
import numpy as np
import conversion
from helpers import whatis

def join(images, axis=0):
    if isinstance(images, types.GeneratorType):
        images = list(images)

    w, h = 0, 0
    x, y = 0, 0
    # Make all images numpy arrays and get their shapes
    arrays = []
    for im in images:
        arrays.append(conversion.rgba_array(im))

    shapes = [a.shape[:2] for a in arrays]

    # Calculate output dimensions
    if axis:
        w, h = sum([sh[1] for sh in shapes]), shapes[0][0]
    else:
        h, w = sum([sh[0] for sh in shapes]), shapes[0][1]

    # Create output image and paste all images into it
    output = np.zeros((h, w, 4), dtype=np.uint8)
    for a, (ih, iw) in zip(arrays, shapes):
        if axis == 1:
            output[:, x:x+iw] = a
            x += iw
        else:
            output[y:y+ih, :] = a
            y += ih
    return output
