from random import shuffle

class Sudoku(object):
    def __init__(self, data):
        """Sudoku constructor

        Attributes
            data    - 9x9 array with numbers from sudoku puzzle, 0 means empty squares
        """
        self.data = data
        self.blank_spots_indices = []
        self.determine_initial_number_positions()

    def determine_initial_number_positions(self):
        """Saves indices of numbers given in puzzle at start

        Those indices are later used to determine which numbers to swap"""
        self.blank_spots_indices = \
            [[index for index, elem in enumerate(row) if elem == 0] for row in self.data]

    def generate_initial_solution(self):
        """Fills empty squares with random numbers"""
        digits = set(range(1, 10))
        for i, _ in enumerate(self.data):
            digits_to_insert = list(digits - set(self.data[i]))  # list of missing digits
            shuffle(digits_to_insert)
            self.data[i, self.blank_spots_indices[i]] = digits_to_insert
        pass

    def generate_neighbor_solution(self):
        """Generates new solution by swapping digits in two initially empty squares"""
        pass

    def evaluate_solution(self):
        """Calculates and returns value of fitness function

        Returned value tells how far is current solution from
        a correct one by counting digit repetitions in each
        row, column and 3x3 subsquare
        """
        pass


