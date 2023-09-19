import random
import matplotlib.pyplot as plt
import numpy as np

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
        # add 0.1 to each element which has 1 as neighbor
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
        # pass directly via column and remove all blocked columns
        col_list = [i for i in  range(len(self.matrix[0]))]
        for i in range(len(self.matrix[0])):
            for row in range(len(self.matrix)):
                if self.matrix[row][i] != 0:
                    col_list.remove(i)
                    break
        return col_list
    
    def train2(self):
        # pass via column and return when blocked
        col_list = []
        for i in range(len(self.matrix[0])):
            col, blocked, start_row, row = Helper(self.matrix).stopped_at(i)
            col_list.append([col, blocked, start_row, row])
        Helper(self.matrix).train_matrix()
        return col_list

class Helper:
    def __init__(self, matrix):
        self.matrix = matrix

    def stopped_at(self, col, start_row=0):
        # returns the row where the blockage starts
        for row in range(start_row, len(self.matrix)):
            if self.matrix[row][col] != 0:
                return col, False, start_row, row
        return col, True, start_row, len(self.matrix)

    def train_matrix(self):
        self.trained_matrix = np.array(self.matrix, dtype=float)
        self.trained_matrix[self.trained_matrix == 1] = -1
        inc = 1/(len(self.trained_matrix)*len(self.trained_matrix[0]))
        # update the last row
        for col in range(len(self.trained_matrix[0])):
            if self.trained_matrix[-1][col] == 0:
                self.trained_matrix[-1][col] = inc
        # update rest of the rows only row back
        for row in range(len(self.trained_matrix)-2, -1, -1):
            for col in range(len(self.trained_matrix[0])):
                if self.trained_matrix[row+1][col] > 0 and self.trained_matrix[row][col] != -1:
                    self.trained_matrix[row][col] = self.trained_matrix[row+1][col] + inc
            # update sideways
            temp_arr = np.concatenate(([-1], self.trained_matrix[row], [-1]))
            for i in range(len(temp_arr)):
                if temp_arr[i] != 0:
                    continue
                move_left = True
                move_right = True
                left_index = i-1
                right_index = i+1
                left_val = 0
                right_val = 0
                count = 0
                temp_left_val = 0
                temp_right_val = 0
                while move_left or move_right:
                    count += 1
                    if move_left:
                        if temp_arr[left_index] == -1:
                            move_left = False
                        elif temp_arr[left_index] > 0:
                            temp_left_val = count*inc + temp_arr[left_index]
                        if move_left:
                            left_val = min_positive(left_val, temp_left_val)  
                        left_index -= 1

                    if move_right:
                        if temp_arr[right_index] == -1:
                            move_right = False
                        elif temp_arr[right_index] > 0:
                            temp_right_val = count*inc + temp_arr[right_index]
                        if move_right:
                            right_val = min_positive(right_val, temp_right_val)
                        right_index += 1

                self.trained_matrix[row][i-1] = min_positive(left_val, right_val) or -1
        print(self.trained_matrix)


def min_positive(a, b):
    positives = min([num for num in [a, b] if num > 0], default=0)
    return positives
