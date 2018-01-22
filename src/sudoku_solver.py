import numpy as np
from copy import deepcopy
from random import random
from math import exp
from src.sudoku import Sudoku


class SudokuSolver(object):
    def __init__(self, puzzle_filename, init_temp=1, cooldown=.9999, minTemp = 0.01):
        """SudokuSolver constructor

        Attributes:
            filename    - path to file with sudoku puzzle
            init_temp   - base temperature
            cooldown    - temperature reduction coefficient
            iterations  - maximum number of simulated annealing algorithm
                          iterations
        """
        self.temperature = init_temp
        self.minTemp = minTemp
        self.cooldown = cooldown
        self.current_solution = Sudoku(self.load_data_from_file(puzzle_filename))

    def load_data_from_file(self, puzzle_filename):
        """Loads puzzle data from file"""
        with open(puzzle_filename) as f:
            data = np.fromfile(f, dtype=int, sep=" ")
        data = np.reshape(data, (9, 9))
        return data

    def display_solution(self):
        """Displays current solution"""
        def notzero(s):
            if s != 0: return str(s)
            if s == 0: return "_"
        solution = ""
        for i, row in enumerate(self.current_solution.data):
            if i%3 == 0:
                solution += "-"*25+'\n'
            solution += "| " + " | ".join([" ".join(notzero(s) for s in row[3*(k-1):3*k]) for k in range(1,4)]) + " |\n"
        solution += "-" * 25 + '\n'
        print(solution)

    def simulated_annealing(self):
        """Tries to solve the sudoku puzzle with simulated annealing process

        At each step, algorithm generates new solution and then compares
        values of fitness function for both new and current solution.
        The new solution is assigned as current when its fitness is better.
        If it's worse, discard it with certain probability based on temperature
        and difference in scores. After each step decrease temperature by
        small amount.

        Algorithm goes on until correct solution is found or maximum number
        of iterations is exceeded.
        """
        print("\nINITIAL PUZZLE:")
        self.display_solution()

        self.current_solution.generate_initial_solution()
        i = 0
        while (self.temperature > self.minTemp):
            next_solution = deepcopy(self.current_solution)
            next_solution.generate_neighbor_solution()
            current_score = self.current_solution.evaluate_solution()
            candidate_score = next_solution.evaluate_solution()
            if candidate_score < current_score:
                self.current_solution = next_solution
            elif exp((float(current_score - candidate_score) / self.temperature)) - random() > 0:
                self.current_solution = next_solution
            if candidate_score == 0:
                print("\nPUZZLE SOLVED")
                print("Solution:")
                print("Iteration %s,    Current Score: %s,  Temperature: %.5f"%(i, current_score, self.temperature))
                self.display_solution()
                return True
            self.temperature = self.temperature * self.cooldown
            i += 1
            if i % 1000 == 0:
                print("Iteration %s,    Current Score: %s,  Temperature: %.5f"%(i, current_score, self.temperature))
        print("PUZZLE NOT SOLVED")
        print("Numbers of errors in solution:", self.current_solution.evaluate_solution())
        print("Last solution:")
        self.display_solution()
        return False

if __name__ == "__main__":
    def get_puzzle_filename():
        print("\n Choose sudoku level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        level = input()
        return {
            '1': "easy",
            '2': "medium",
            '3': "hard"
        }.get(level, "s10a")


    def is_number(s):
        try:
            float(s)  # for int, long and float
        except ValueError:
            try:
                complex(s)  # for complex
            except ValueError:
                return False
        return True

    init_temp = 1
    min_temp = 0.01
    cooldown = 0.9999

    while(1):
        sudoku_file_name = "../resources/" + get_puzzle_filename() + ".txt"
        nr_of_tests = int(input("Number of tests: "))
        init_temp_input = input("Initial temperature: ")
        mini_temp_input = input("Minimal temperature: ")
        cooldown_input = input("Cooldown: ")
        if init_temp_input.isdigit():
            init_temp = int(init_temp_input)
        if is_number(mini_temp_input):
            min_temp = float(mini_temp_input)
        if is_number(cooldown_input):
            cooldown = float(cooldown_input)
        nr_of_correct_solutions = 0
        for i in range(nr_of_tests):
            solver = SudokuSolver(sudoku_file_name, init_temp, cooldown, min_temp)
            if solver.simulated_annealing():
                nr_of_correct_solutions += 1
        print("Nr of solved puzzles:" + str(nr_of_correct_solutions))
