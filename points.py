#  Paula Farebrother
#  Created on 2nd August 2024
#  Last updated Oct 2024

# ________________________________________________________________
#                        Point Class
# ________________________________________________________________

import math


class Point:
    def __init__(self, x, y):
        """ Sets x and y for point. """
        self.x = x
        self.y = y

    def distance(self, point):
        """ Calculates distances between two given points. """
        dx = self.x - point.x  # point 1 (object) minus point 2 (parameter)
        dy = self.y - point.y
        return round(math.sqrt(dx * dx + dy * dy), 2)

    def __str__(self):
        """ returns string of x and y. """
        return f"x: {self.x}  y: {self.y}"

