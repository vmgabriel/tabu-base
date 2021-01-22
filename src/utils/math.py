"""
Module of Control math
"""

# Libraries
import math
from typing import List, Callable


# Modules
from src.utils.composer import composer
from src.utils.dict import to_items


def euclidean_vector_distance(vec1: tuple, vec2: tuple) -> float:
    """
    Eucledian vector difference

    vec1: vector (a,b)
    vec2: vector (c,d)

    return vector1 - vector2
    """
    return math.sqrt(
        ((vec1[0] - vec2[0]) ** 2) +
        ((vec1[1] - vec2[1]) ** 2)
    )


def matrix_distance(
        data: List[dict],
        axis_name_x: str,
        axis_name_y: str
) -> List[List[float]]:
    """
    Generate a Matrix of distances
    """
    tam = len(data)

    def filter_axis(axis_1: str, axis_2: str) -> Callable:
        """Filter Callable function for get data base for axis"""
        return lambda x: list(
            filter(
                lambda y: y[0] in [axis_1, axis_2],
                x
            )
        )

    def value_data(defined: List[dict]):
        """Get only the value"""
        return list(map(
            lambda x: x[1],
            defined
        ))

    to_vector = composer(
        tuple,
        value_data,
        filter_axis(axis_name_x, axis_name_y),
        to_items
    )

    distance = [
        [
            euclidean_vector_distance(
                to_vector(data[i]),
                to_vector(data[j])
            )
            for j in range(tam)
        ]
        for i in range(tam)
    ]

    return distance
