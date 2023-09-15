import random
import matplotlib.pyplot as plt

class ML:
    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        temp = [[0 for i in range(cols)] for j in range(rows)]
        self.matrix = temp
        self.update_self(matrix)
        
    def printt(self):
        plt.imshow(self.matrix, cmap='hot', interpolation='nearest')
        plt.colorbar()  # adds a color bar to the right
        plt.show()

    def update_val(self, row, col, val):
        self.matrix[row][col] = min(self.matrix[row][col] + val, 1)

    def update_self(self, matrix):
        """
        add 0.1 to each element which has 1 as neighbor
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] != 0:
                    self.update_val(row, col, matrix[row][col])
                    inc = 0.05
                    if row > 0:
                        self.update_val(row-1, col, inc)
                    if row < len(matrix)-1:
                        self.update_val(row+1, col, inc)
                    if col > 0:
                        self.update_val(row, col-1, inc)
                    if col < len(matrix[0])-1:
                        self.update_val(row, col+1, inc)


class Training:
    def __init__(self, matrix, model):
        self.matrix = matrix

    def train1(self):
        """
        pass directly via column and remove all blocked columns
        """
        col_list = [i for i in  range(len(self.matrix[0]))]
        for i in range(len(self.matrix[0])):
            for row in range(len(self.matrix)):
                if self.matrix[row][i] != 0:
                    col_list.remove(i)
                    break
        return col_list
