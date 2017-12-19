import sys
from src.sudoku import Sudoku


class SudokuSolver(object):
    def __init__(self, puzzle_filename, init_temp = 1, cooldown = .9999, iterations = 100000):
        """
        filename - path to file with sudoku puzzle
        init_temp - base temperature
        cooldown - temperature reduction coefficient
        iterations - maximum number of simulated annealing loop iterations
        """
        self.temperature = init_temp
        self.cooldown = cooldown
        self.iterations = iterations
        self.puzzle = Sudoku(self.load_data_from_file(puzzle_filename))
        self.simulated_annealing()

    def load_data_from_file(self, puzzle_filename):
        """
        Loads puzzle data from file
        """
        data = []
        return data

    def simulated_annealing(self):
        """
        Try to solve the puzzle by generating solutions deriving from current one.
        Every time new solution is created, both current and new solutions are being
        evaluated, and their scores compared.
        If new score is better, replace current solution with new one. Else discard it
        with certain probability based on temperature and difference between scores.
        Every iteration the temperature is decreased by small amount (muultiplied by
        cooldown coefficient).
        End if puzzle is solved or reached maximum iterations.
        """

    def display_solution(self):
        """
        Displays current solution
        """



if __name__ == "__main__":
    if len(sys.argv) > 1:
        SudokuSolver(sys.argv[1])
    else:
        filename = input("Podaj nazwe pliku")
        SudokuSolver(filename)