"""
Greedy Module Solution for Utils control
"""

# Libraries
from typing import List
from functools import reduce

# Modules
from src.utils.math import list_negative, invert_positions


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


def evaluate_fo(
        matrix_distance: List[List[float]],
        solution: List[int]
) -> float:
    """
    Minizing evaluate function objective

    ex:
    matrix_distance = [
      [0,1,2,3,4],
      [0,2,3,4,5],
      [0,3,5,6,7],
      [7,8,9,0,1],
      [4,5,6,7,8]
    ]
    solution: [1,2,3,4,0]

    resolved:
    15
    """
    return reduce(
        lambda acc, x: acc + matrix_distance[x[0]][x[1]],
        enumerate(solution),
        0
    )


def best_change_not_tabu(
        matrix_distance: List[List[float]],
        solution: List[int]
) -> (float, tuple):
    """
    change the data for best change based into function objective
    matrix_distance: List[List[float]] -> Matrix of distances
    solution: List[int] -> all solutions

    return (float, (posx, posy)) -> the best solution into position
    """
    # fun_before = evaluate_fo(matrix_distance, solution)
    best_fo = 1E+100
    position = (-1, -1)
    tam = len(solution)
    for posx in range(tam-1):
        for posy in range(posx+1 if posx+1 != tam else tam, tam):
            funobj = evaluate_fo(
                matrix_distance,
                invert_positions(solution, posx, posy)
            )
            if funobj < best_fo:
                best_fo = funobj
                position = (posx, posy)
    return (best_fo, position)


def generate_local_search(
        matrix_distance: List[List[float]],
        solution: List[int]
) -> (int, List[int]):
    """
    This generate a local search for the minize way based in fo
    matrix_distance: List[List[float]]
    """
    counter = 0
    manage = True
    best_change = best_change_not_tabu(matrix_distance, solution)
    prev_change = (1E+100,)

    while manage:
        if prev_change[0] < best_change[0]:
            manage = False
        else:
            prev_change = best_change
            best_change = best_change_not_tabu(matrix_distance, solution)
            solution = invert_positions(
                solution,
                origin=best_change[1][0],
                destiny=best_change[1][1]
            )
        counter += 1
    return (counter, best_change[0], solution)
