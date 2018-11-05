#!/usr/bin/env python3

class Point():
    """ Point class represents and manipulates x, y coords."""

    def __init__(self, x = 0, y = 0):
        """ Create a new point at the origin"""
        self.x = x
        self.y = y
    def distance_from_origin(self):
        """ Compute my distance from the origin"""
        return(self.x**2 + self.y**2)**0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target_point):
        """ Return the halfway point"""
        
        a = (self.x+target_point.x)/2
        b = (self.y+target_point.y)/2
        
        return Point(a, b)
    
    def distance(self, another_point):
        """ Return the distance between two points. """
        return ((another_point.x-self.x)**2 + (another_point.y-self.y)**2)**0.5

    def reflect_x(self):
        return Point(self.x, -self.y)
    
    def slope_from_origin(self):
        return self.y/self.x

    def get_line_to(self, point):
        a = (point.y - self.y)/(point.x - self.x)
        b = self.y - (self.x)*a
        return (a, b)


class Rectangle():
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle with left upper corner at posn, and width as w, height as h """
        self.corner = posn
        self.width = w
        self.height = h
    
    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, w_delta, h_delta):
        """ Grow the object by delta """
        self.width += w_delta
        self.height += h_delta
    
    def move(self, x_delta, y_delta):
        """ Move the object by delta """
        self.corner.x += x_delta
        self.corner.y += y_delta

    def area(self):
        """ Calculate the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Return the perimeter of the rectangle """
        return 2*(self.width + self.height)

    def flip(self):
        """ Swap the width and height of a rectangle """
        temp = self.width
        self.width = self.height
        self.height = temp

    def contains(self, point):
        """ Return if point falls into the scope of the rectangle """
        if (self.corner.x <= point.x < self.corner.x + self.width) and (self.corner.y <= point.y < self.corner.y - point.y):
            return True
        else:
            return False

    def overlap(self, rctgl):
        pass



    
