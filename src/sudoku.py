class Sudoku(object):
    def __init__(self, data):
        """Sudoku constructor

        Attributes
            data    - 9x9 array with numbers from sudoku puzzle, 0 means empty squares
        """
        self.data = data
        self.initial_numbers = []

    def generate_initial_solution(self):
        """Fills empty squares with random numbers"""
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


