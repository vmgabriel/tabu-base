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
    Generate a Matrix of distances based in euclidean vector distances
    data: List[dict] - list of data to get matrix_distance
    axis_name_x: str - axis based into data 'x'
    axis_name_y: str - axis based into data 'y'
    return: List[List[float]] -
    based in length of data List [len(data), len(data)] dimension

    Get data of distance vector based into data get
    """
    tam = len(data)

    def filter_axis(axis_1: str, axis_2: str) -> Callable:
        """
        Filter Callable function for get data base for axis
        if axis_1 is 'x' as name of x
        if axis_2 is 'y' as name of y

        This return a function that
        verify the first data of tuple that show in axis only name
        ex:
        filter_axis(
        'x', 'y'
        )([('x': 1, 'y': 2, 'z': 3),('x': 4, 'y': 5, 'z': 6)])
        -> this return
        [('x': 1, 'y': 2),('x': 4, 'y': 5)]
        """
        return lambda x: list(
            filter(
                lambda y: y[0] in [axis_1, axis_2],
                x
            )
        )

    def value_data(defined: List[tuple]) -> List[int]:
        """
        Get only the value
        ex:
        [('a', 1),('b', 2)] -> [1,2]
        """
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


def list_negative(_l: List[int]) -> List[int]:
    """
    Convert all data of the matrix to negative
    ex:
    [1,2,3,4] -> [-1,-2,-3,-4]
    """
    return list(map(
        lambda x: -x,
        _l
    ))


def invert_positions(
        solution: List[int],
        origin: int,
        destiny: int
) -> List[int]:
    """
    Definition for invert position
    ex:
    solution: [1,2,3]
    origin: 2
    destiny: 3
    return: [1,3,2]
    """
    solution[destiny], solution[origin] = solution[origin], solution[destiny]
    return solution
