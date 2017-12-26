import sys
import numpy as np
from src.sudoku import Sudoku


class SudokuSolver(object):
    def __init__(self, puzzle_filename, init_temp=1, cooldown=.9999, iterations=100000):
        """SudokuSolver constructor

        Attributes:
            filename    - path to file with sudoku puzzle
            init_temp   - base temperature
            cooldown    - temperature reduction coefficient
            iterations  - maximum number of simulated annealing algorithm
                          iterations
        """
        self.temperature = init_temp
        self.cooldown = cooldown
        self.iterations = iterations
        self.current_puzzle = Sudoku(self.load_data_from_file(puzzle_filename))
        self.display_solution()
        # self.simulated_annealing()

    def load_data_from_file(self, puzzle_filename):
        """Loads puzzle data from file"""
        with open(puzzle_filename) as f:
            data = np.fromfile(f, dtype=int, sep=" ")
        data = np.reshape(data, (9, 9))
        return data

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
        pass

    def display_solution(self):
        """Displays current solution"""
        for rows in self.current_puzzle.data:
            for elem in rows:
                print(elem, end=" ")
            print()


if __name__ == "__main__":
    SudokuSolver("../resources/puzzle1.txt")
    """
    if len(sys.argv) > 1:
        SudokuSolver(sys.argv[1])
    else:
        filename = input("Podaj nazwe pliku")
        SudokuSolver(filename)
        """
