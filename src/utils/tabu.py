"""
Tabu Algorithm
"""

# Libraries
from typing import List

# Configuration
from src.config import configuration as conf

# Modules
from src.utils.math import evaluate_fo, invert_positions


def best_change_not_tabu(
        matrix_distance: List[List[float]],
        solution: List[float]
) -> (float, tuple):
    """
    best change for not tabu
    ex:
    matrix_distance: List[List[float]]
    solution: List[float]

    return: (3, (1,2))
    """
    best_fo = evaluate_fo(matrix_distance, solution)
    change = (0, 0)
    tam = len(solution)
    for i in range(tam):
        for j in range(i, tam):
            data = invert_positions(solution, i, j)
            moment_fo = evaluate_fo(matrix_distance, data)
            if moment_fo < best_fo:
                best_fo = moment_fo
                change = (i, j)
    return (best_fo, change)


def load_tabu(
        matrix_distance: List[List[float]],
        solution: List[float]
):
    """Load tabu"""
    for i in range(conf['tabu']['iterations']):
        best_change = best_change_not_tabu(matrix_distance, solution)
        solution = invert_positions(
            solution,
            best_change[1][0],
            best_change[1][1]
        )

    return (range(conf['tabu']['iterations']), solution)
