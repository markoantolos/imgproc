import os, sys
import numpy as np

from core import BBox 
import proc
import slicing
import conversion
from helpers import whatis

class ImageArray:
    def __init__(self, array):
        self.array = conversion.ndarray(array)
        self._box = None

    @property
    def box(self):
        if not self._box:
            self._box = BBox.from_array(self.array)
        return self._box

    @property
    def image(self):
        return conversion.image(self.array)

    def copy(self):
        result = ImageArray(np.copy(self.array))
        return result

    def to_rgba(self, alpha=255):
        self.array = conversion.to_rgba_array(self.array)
        return self

    def threshold(self, value=128):
        proc.threshold(self.array, value)
        return self

    def invert(self):
        self.array = proc.invert(self.array)
        return self

    def binary(self):
        proc.binary(self.array)
        return self

    def slices(self, box=None, axis=0, depth=1, noise=0, tolerance=0):
        print('slices')
        box = box if box else self.box
        v1, v2 = (box.x1, box.x2) if axis else (box.y1, box.y2)
        sums = self.array.sum(axis=axis)
        rows = [0 if v <= noise else 1 for v in sums]
        gs = slicing.gaps(rows, tolerance=tolerance)
        for g1, g2 in gs:
            if axis:
                yield BBox(v1, g1, v2, g2)
            else:
                yield BBox(g1, v1, g2, v2)

