import itertools
import math


def distance_between(city1, city2):
    """
    Given two cities as (x, y) tuples, returns the Euclidean distance between them.
    """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def tsp_brute_force(cities):
    """
    Given a list of cities to visit, returns the shortest possible route that visits all cities exactly once.
    """
    shortest_route = None
    shortest_distance = float('inf')

    for route in itertools.permutations(cities):
        distance = 0
        for i in range(len(route) - 1):
            distance += distance_between(route[i], route[i+1])
        distance += distance_between(route[-1], route[0])

        if distance < shortest_distance:
            shortest_distance = distance
            shortest_route = route

    return shortest_route, shortest_distance
