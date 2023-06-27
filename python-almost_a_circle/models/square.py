#!/usr/bin/python3
"""WWrite the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.update(width=value, height=value)

    def __str__(self):
        """returns the object Square with all their values"""
        txt = "[Square] ({}) {}/{} - {}"
        rec = txt.format(self.id, self.x, self.y, self.width)
        return rec
