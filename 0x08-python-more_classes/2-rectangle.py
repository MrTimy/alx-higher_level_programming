#!/usr/bin/python3

""" Class to define a rectangle """


class Rectangle:
    """ Initialization properties """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """ Return area of the rectangle """

        area = self.__width * self.__height
        return area

    def perimeter(self):
        """ Return perimeter of the rectangle if either side not null """

        if self.__width != 0 or self.__height != 0:
            perimeter = 2 * (self.__width + self.__height)
            return perimeter
        else:
            return 0
