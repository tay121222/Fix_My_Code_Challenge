#!/usr/bin/python3
"""Calculates perimeter and area of square"""


class Square():
    def __init__(self, width=0, height=0):
        """Initialize"""
        self.width = width
        self.height = height

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter(self):
        """ Perimeter of square """
        return (self.width * 4)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area())
    print(s.perimeter())
