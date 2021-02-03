"""
tabu in oo
"""

import time
import math


def timeit(method):
    """Genering time"""
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            code = kw.get('log_code', method.__code__.upper())
            kw['log_time'][code] = int((te - ts) * 1000)
        else:
            print(
                '%r  %2.2f ms' % (method.__code__, (te - ts) * 1000)
            )
        return result
    return timed


class TabuSearch:
    """Class tabu"""
    def __init__(self, distances, iter_num, tabu_duration, first_solution=None):
        self.iter_num = iter_num
        self.tabu_duration = tabu_duration
        self.size = len(distances)
        self.first_solution = None
        self.distances = distances
        self.tabu_matrix = None
        self.solution = None
        self.pos_1 = 0
        self.pos_2 = 0
        self.__set_first_solution(first_solution=first_solution)

    def define_distance(self, data: int):
        """distances"""
        print('data -', data)

    @timeit
    def solve(self, tabu_duration=None):
        """Solve"""
        if tabu_duration:
            self.tabu_duration = tabu_duration

        self.solution = self.first_solution[:]
        _tabu_solution = self.first_solution[:]
        _tabu_cost = self.__get_cost(solution=_tabu_solution)
        self.__init_matrix()

        solutions = []
        for _ in range(self.iter_num):
            tmp_best_cost = self.__get_better_change()
            self.__swap_positions(pos_1=self.pos_1, pos_2=self.pos_2)
            solutions.append((tmp_best_cost, self.solution[:]))
            if tmp_best_cost < _tabu_cost:
                _tabu_solution = self.solution[:]
                _tabu_cost = self.__get_cost(solution=_tabu_solution)
            self.__update_tabu_matrix()
        solutions.sort()
        return (
            self.__get_cost(solution=_tabu_solution),
            _tabu_solution, solutions[0],
            self.__get_cost(solution=solutions[0][1])
        )

    def __get_better_change(self):
        """better change"""
        best_cost = 1e999
        for pos_1 in range(self.size - 1):
            for pos_2 in range(pos_1 + 1, self.size):
                self.__swap_positions(pos_1=pos_1, pos_2=pos_2)
                tmp_sol = self.__get_cost(solution=self.solution)
                if (
                    tmp_sol < best_cost and
                    self.tabu_matrix[pos_1][pos_2] == 0 and
                    self.tabu_matrix[pos_2][pos_1] < self.tabu_duration * 3
                ):
                    best_cost = tmp_sol
                    self.pos_1 = pos_1
                    self.pos_2 = pos_2
                self.__swap_positions(pos_1=pos_1, pos_2=pos_2)
        return best_cost

    def __swap_positions(self, pos_1, pos_2):
        self.solution[pos_1], self.solution[pos_2] = (
            self.solution[pos_2],
            self.solution[pos_1]
        )

    def __update_tabu_matrix(self):
        # substract 1 in tabu list
        for pos_1 in range(self.size - 1):
            for pos_2 in range(pos_1 + 1, self.size):
                if self.tabu_matrix[pos_1][pos_2] > 0:
                    self.tabu_matrix[pos_1][pos_2] -= 1
                    if self.tabu_matrix[pos_1][pos_2] == 0:
                        self.tabu_matrix[pos_2][pos_1] += 1
        # register swap city_1 and city_2 in tabu list
        self.tabu_matrix[self.pos_1][self.pos_2] = self.tabu_duration

    def __get_cost(self, solution):
        _cost = 0
        for index, current_item in enumerate(solution):
            if not index:
                init_item = prev_item = current_item
                continue
            _cost += self.distances[prev_item][current_item]
            prev_item = current_item
            if index == len(solution) - 1:
                _cost += self.distances[current_item][init_item]
        return _cost

    def __set_first_solution(self, first_solution):
        self.first_solution = (
            first_solution
            if first_solution else
            list(range(self.size))
        )
        print(
            'fist_solution: ',
            self.__get_cost(solution=self.first_solution),
            self.first_solution
        )

    def __init_matrix(self):
        self.tabu_matrix = [
            [0 for _ in range(self.size)] for _ in range(self.size)
        ]
