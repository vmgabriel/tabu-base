"""
Module for app - load
"""

# Libraries

# Utils
from src.utils import (
    csv,
    composer,
    dict_module,
    greedy_util,
    math_util,
    tabu_util,
    tabu_oop_util
)

# Exceptions
from src.exceptions import input_exception


def input_assignation():
    """
    read input assignation

    if not valid assign input this send Exception based in InvalidInput
    """
    tabu_input = input('Tabu Aspiration\n(t)rue\n(f)alse\n# ')
    if tabu_input not in ['t', 'f']:
        raise input_exception.InvalidInput(tabu_input)
    return tabu_input


def tabu_without_aspirations():
    """
    Tabu module without aspirations
    """
    file_path = 'in/base0.csv'
    init_data = composer(
        dict_module.all_data_to_int,
        csv.read_file
    )(file_path)
    print('Data - ', init_data)
    distances = math_util.matrix_distance(init_data, 'cx', 'cy')
    print('Distances - ', distances)
    response = greedy_util.worst_solution(distances)
    print('First Solution - ', response)
    iterable_control = greedy_util.generate_local_search(distances, response)
    print('Solution - ', iterable_control)
    print('tabu solutions - ')
    ts = tabu_oop_util.TabuSearch(
        distances=distances,
        iter_num=700,
        tabu_duration=4,
        first_solution=iterable_control[2]
    )
    for ite in range(4, 24):
        print(ite, ts.solve(tabu_duration=ite))


def tabu_with_aspirations():
    """
    Tabu module with aspirations
    """
    print('[In Develop] - not completed')


def run():
    """Load process for app"""
    try:
        load_algorith = (
            tabu_with_aspirations
            if input_assignation() == 't' else
            tabu_without_aspirations
        )
        load_algorith()
    except input_exception.InvalidInput as _a:
        print(f'data - {_a}')
