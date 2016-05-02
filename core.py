class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)

class BBox:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1 if x1 < x2 else x2
        self.y1 = y1 if y1 < y2 else y2
        self.x2 = x2 if x2 > x1 else x1
        self.y2 = y2 if y2 > y1 else y1

    @classmethod
    def from_array(cls, array):
        h, w = array.shape[:2]
        return cls(0, 0, w, h)

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

    def __str__(self):
        return '(%s, %s, %s, %s)' % (self.x1, self.y1, self.x2, self.y2)

    def __repr__(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def __iter__(self):
        yield self.x1
        yield self.y1
        yield self.x2
        yield self.y2

    def __getitem__(self, index):
        if index == 0: return self.x1
        if index == 1: return self.y1
        if index == 2: return self.x2
        if index == 3: return self.y2

    def __len__(self):
        return 4
