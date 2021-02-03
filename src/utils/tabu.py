"""
Tabu Algorithm
"""

# Libraries
from typing import List

# Configuration
from src.config import configuration as conf

# Modules
from src.utils.math import (
    evaluate_fo,
    invert_positions,
    euclidean_vector_distance
)


def best_change_not_tabu(
        matrix_distance: List[List[float]],
        solution: List[float],
        tabu_matrix: List[List[float]],
        duration: int
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
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            solution = invert_positions(solution, i, j)
            moment_fo = get_cost(solution, matrix_distance)
            if (
                    moment_fo < best_fo and
                    tabu_matrix[i][j] == 0 and
                    tabu_matrix[j][i] < duration * 3
            ):
                best_fo = moment_fo
                change = (i, j)
    return (best_fo, change)


def init_tabu_matrix(tam: int) -> List[List[int]]:
    """Generate the first matrix solution"""
    return [[0 for _ in range(tam)] for _ in range(tam)]


def get_first_solution(tam: int, first_solution: List[int] = []) -> List[int]:
    """Get the first solution"""
    return list(range(tam)) if len(first_solution) == 0 else first_solution


def get_cost(solution: List[int], distances: List[List[float]]) -> List[int]:
    """Generate a list for cost"""
    cost = 0
    for i, item in enumerate(solution):
        if not i:
            init_item = prev_item = item
            continue
        cost = distances[prev_item][item]
        prev_item = item
        if i == len(solution) - 1:
            cost += distances[item][init_item]
    return cost


def update_tabu_matrix(
        tabu_matrix: List[List[float]],
        tabu_duration: int
) -> List[List[float]]:
    """Update tabu"""
    size = len(tabu_matrix)
    for pos_1 in range(size - 1):
        for pos_2 in range(pos_1 + 1, size):
            if tabu_matrix[pos_1][pos_2] > 0:
                tabu_matrix[pos_1][pos_2] -= 1
                if tabu_matrix[pos_1][pos_2] == 0:
                    tabu_matrix[pos_2][pos_1] += 1
    tabu_matrix[pos_1][pos_2] = tabu_duration
    return tabu_matrix


def solve(
        matrix_distance: List[List[float]],
        first_solution: List[int] = [],
        tabu_duration: int = conf['tabu']['tabu_duration'],
):
    """Solve the tabu"""
    # Generate first solution and matrix tabu
    tam = len(first_solution) if len(first_solution) > 0 else 10
    solution = get_first_solution(tam, first_solution)
    tabu_solution = get_first_solution(tam, first_solution)
    matrix_tabu = init_tabu_matrix(tam)
    tabu_cost = get_cost(solution, matrix_distance)

    solutions = []
    for _ in range(conf['tabu']['iterations']):
        (best_cost, positions) = best_change_not_tabu(
            matrix_distance,
            solution,
            matrix_tabu,
            tabu_duration
        )
        solution = invert_positions(solution, positions[0], positions[1])
        solutions.append((best_cost, solution[:]))
        if best_cost < tabu_cost:
            tabu_solution = solution[:]
            tabu_cost = get_cost(solution, matrix_distance)
        matrix_tabu = update_tabu_matrix(matrix_tabu, tabu_duration)
    solutions.sort()
    return (
        get_cost(tabu_solution, matrix_distance),
        tabu_solution,
        solutions[0],
        get_cost(solutions[0][1], matrix_distance)
    )
