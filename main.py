#!/usr/local/bin/python3

import sys, os 
import numpy as np
from PIL import Image

from imagearray import ImageArray
import proc
import conversion
import sequence
import slicing
import drawing

PREVIEW_DIR = os.path.abspath('./images/preview')
if not os.path.exists(PREVIEW_DIR):
    os.numpy(PREVIEW_DIR)

def main():
    im = Image.open('images/osobna-prednja.jpg')
    im = im.convert('L')

    w, h = im.size

    scale = 1/2.2
    w1, h1 = int(w * scale), int(h * scale)
    im.thumbnail((w1, h1))

    base = ImageArray(im)
    bw = base.copy().threshold(120)
    inverted = bw.copy().invert()
    binary = inverted.copy().binary()

    boxes = binary.slices(axis=1, noise=0, tolerance=0)
    output = drawing.boxes(bw.image, boxes)

    joined = sequence.join([base, bw, inverted, output], axis=0)
    proc.show2(joined, PREVIEW_DIR, 'png')

if __name__ == '__main__':
    main()
