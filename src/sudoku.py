class Sudoku(object):
    def __init__(self, data):
        """
        data - 9x9 array with numbers from sudoku puzzle, 0 means empty squares
        """
        self.data = data
        self.initial_numbers = []

    def generate_initial_solution(self):
        """
        Fill empty squares with random numbers
        """

    def generate_neighbor_solution(self):
        """
        Generate new solution by swapping digits in two initially empty squares
        """

    def evaluate_solution(self):
        """
        Calculates how far current solution is from solved puzzle
        by counting digit repetitions in columns, rows and subsquares.
        Each mistake increases score by 1.
        :return: score for current solution stored in data
        """
        score = 0
        return score


