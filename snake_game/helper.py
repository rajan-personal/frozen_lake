import numpy as np
from enum import Enum

# movement
class MoveDirection(Enum):
    FORWARD = [0, 1]
    LEFT = [-1, 0]
    RIGHT = [1, 0]

class Direction(Enum):
    UP = [0, 1]
    RIGHT = [1, 0]
    DOWN = [0, -1]
    LEFT = [0, -1]


class Snake:
    def __init__(self, length, breadth, snake_size) -> None:
        self.length = length
        self.breadth = breadth
        self.snake_size = snake_size
        field = np.zeros((length, breadth))
        field = np.insert(field, 0, -1, axis=0)
        field = np.insert(field, length+1, -1, axis=0)
        field = np.insert(field, 0, -1, axis=1)
        field = np.insert(field, breadth+1, -1, axis=1)
        self.field = field

    def start_position(self):
        x, y = 6, 3
        head_position = np.array([x, y, Direction.RIGHT, MoveDirection.FORWARD])
        tail_position = np.array([x-self.snake_size+1, y, Direction.RIGHT, MoveDirection.FORWARD])
        self.field[y][x] = 1
        self.field[y][x-self.snake_size+1] = 1
        for i in range(1, self.snake_size):
            self.field[y][x-i] = 1
        self.snake = np.array([head_position, tail_position])

    def move(self):
        # move the snake

        # add new head
        first_block = np.copy(self.snake[0])
        dirr = first_block[2]
        move_dirr = first_block[3]
        direction = [dirr.value[0] * move_dirr.value[1], dirr.value[1] * move_dirr.value[0]]
        # remove direction after testing
        new_head = np.array([first_block[0] + direction[0], first_block[1] + direction[1], dirr, move_dirr])
        if move_dirr == MoveDirection.FORWARD:
            self.snake[0] = new_head
        else:
            self.snake = np.insert(self.snake, 0, new_head, axis=0)
        self.field[new_head[1]][new_head[0]] = 1

        # self.snake = np.insert(self.snake, 0, new_head, axis=0)


        # remove last snake block
        # if snake[-1] - snake[-2] == 1:
        #     remove snake[-1]
        #  else:
        #     update snake[-1]
        last_block = np.copy(self.snake[-1])
        second_last_block = np.copy(self.snake[-2])
        x_diff = last_block[0] - second_last_block[0]
        y_diff = last_block[1] - second_last_block[1]
        
        new_last_block = []
        diff = abs(x_diff) + abs(y_diff)
        if diff == 1:
            self.snake = np.delete(self.snake, -1, axis=0)
        else:
            dirr = last_block[2]
            move_dirr = last_block[3]
            
            direction = [dirr.value[0] * move_dirr.value[1], dirr.value[1] * move_dirr.value[0]]
            new_last_block = np.array([last_block[0] + direction[0], last_block[1] + direction[1]])
            self.snake[-1][0] = new_last_block[0]
            self.snake[-1][1] = new_last_block[1]
        # make last block 0
        self.field[last_block[1]][last_block[0]] = 0