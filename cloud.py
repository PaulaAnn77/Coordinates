#  Paula Farebrother
#  Created on 2nd August 2024
#  Last updated Oct 2024

# ________________________________________________________________
#              Module: Find neighbouring coordinates by
#                     creating a 'Cloud' object
# ________________________________________________________________

from .points import *


class Cloud:
    def __init__(self):
        self.cloud = []
        self.distances = []

    def get_point_objects(self, coord_list):  # creates a list
        # of x and y points
        """ Accepts a list, creates pairs of coordinates incrementing
        x by 1 each time and returns as a list called 'cloud'. """
        x = 1
        for y in coord_list:
            # print(x, y)                    # use for debugging
            self.cloud.append(Point(x, y))
            x += 1
        return self.cloud

    def return_neighbours_complete(self, single_point, max_distance):
        """ Returns adjacency list of all neighbours within a given radius. """
        dict = {(single_point.x, single_point.y): {}}
        for target in range(0, len(self.cloud)):
            distance = single_point.distance(self.cloud[target])
            if distance <= max_distance:
                dict[(single_point.x, single_point.y)][(self.cloud[target].x,
                    self.cloud[target].y)] = distance
        return dict

    def return_neighbours_part(self, single_point, max_distance):
        """ Returns adjacency list of all neighbours within a given radius. """
        dict = {single_point.x: {}}
        for target in range(0, len(self.cloud)):
            distance = single_point.distance(self.cloud[target])
            if distance <= max_distance and distance > 0:
                dict[single_point.x][self.cloud[target].x] = distance
        return dict

    def unpack_dict(self, listed_dict):  # create a new dictionary
        new_dict = {}
        for element in listed_dict:
            for key, value in element.items():
                if key not in new_dict:
                    new_dict[key] = {}
                new_dict[key].update(value)
        return new_dict

    def return_dict(self, coords):
        neighbour_results_part = []
        for i in coords:
            neighbours = self.return_neighbours_part(i, 20)
            neighbour_results_part.append(neighbours)
        results = self.unpack_dict(neighbour_results_part)
        return results

    def print_points(self):
        for point in self.cloud:
            print(point)

    def print_neighbours_dict(self, points, max_distance):
        """ Creates and displays the adjacency list. """
        results = []
        for i in points:
            neighbours = self.return_neighbours_complete(i, max_distance)
            results.append(neighbours)
        print(results)
