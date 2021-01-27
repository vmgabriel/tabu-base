"""
Greedy Module Solution for Utils control
"""

# Libraries
from typing import List

# Modules
from src.utils.math import list_negative


# Constants
COMPARE_VALUE = 99999999


def worst_solution(distance_matrix: List[List[float]]) -> List[int]:
    """This generate the worst solution"""
    negative_matrix = list(map(
        list_negative,
        distance_matrix
    ))
    return neghbord_most_near(negative_matrix)


def neghbord_most_near(
        distance_matrix: List[List[float]],
        start_city: int = 0
) -> List[int]:
    """
    get the city most near in distance
    """
    neghbord_used = [start_city]

    def city_most_near(line: int) -> int:
        """
        Get City most near
        """
        compare_value = COMPARE_VALUE
        most_near = -1
        for key, value in enumerate(distance_matrix[line]):
            if (
                    line != key and
                    value < compare_value and
                    key not in neghbord_used
            ):
                compare_value = value
                most_near = key
        neghbord_used.append(most_near)
        return most_near

    return list(map(
        lambda x: city_most_near(x) if x != start_city else start_city,
        range(len(distance_matrix))
    ))
