import numpy as np
from enum import Enum

# movement
class MoveDirection(Enum):
    FORWARD = [0, 1]
    LEFT = [-1, 0]
    RIGHT = [1, 0]

class Orientation(Enum):
    UP = [0, -1]
    RIGHT = [1, 0]
    DOWN = [0, 1]
    LEFT = [-1, 0]

def calculate_next_direction(orientation, direction):
    direction_mapping = {
        (Orientation.UP, MoveDirection.LEFT): Orientation.LEFT,
        (Orientation.UP, MoveDirection.RIGHT): Orientation.RIGHT,
        (Orientation.RIGHT, MoveDirection.LEFT): Orientation.UP,
        (Orientation.RIGHT, MoveDirection.RIGHT): Orientation.DOWN,
        (Orientation.DOWN, MoveDirection.LEFT): Orientation.RIGHT,
        (Orientation.DOWN, MoveDirection.RIGHT): Orientation.LEFT,
        (Orientation.LEFT, MoveDirection.LEFT): Orientation.DOWN,
        (Orientation.LEFT, MoveDirection.RIGHT): Orientation.UP
    }

    return direction_mapping.get((orientation, direction), orientation)

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
        head_position = np.array([x, y, Orientation.RIGHT, MoveDirection.FORWARD])
        tail_position = np.array([x-self.snake_size+1, y, Orientation.RIGHT, MoveDirection.FORWARD])
        self.field[y][x] = 1
        self.field[y][x-self.snake_size+1] = 1
        for i in range(1, self.snake_size):
            self.field[y][x-i] = 1
        self.snake = np.array([head_position, tail_position])

    def move(self, parent_move_dirr=MoveDirection.FORWARD):
        # move the snake

        # add new head
        first_block = np.copy(self.snake[0])
        dirr = first_block[2]
        # move_dirr = first_block[3]
        move_dirr = parent_move_dirr
        direction = calculate_next_direction(dirr, move_dirr)
        direction_value = direction.value
        new_head = np.array([first_block[0] + direction_value[0], first_block[1] + direction_value[1], direction, move_dirr])
        # check if new head is in snake body or wall
        if self.field[new_head[1]][new_head[0]] in [-1, 1]:
            self.field = np.zeros((self.length, self.breadth))
            return False
        if move_dirr == MoveDirection.FORWARD:
            self.snake[0] = new_head
        else:
            self.snake = np.insert(self.snake, 0, new_head, axis=0)
        self.field[new_head[1]][new_head[0]] = 1


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
            
            direction = calculate_next_direction(dirr, move_dirr)
            direction_value = direction.value
            new_last_block = np.array([last_block[0] + direction_value[0], last_block[1] + direction_value[1]])
            self.snake[-1][0] = new_last_block[0]
            self.snake[-1][1] = new_last_block[1]
        # make last block 0
        self.field[last_block[1]][last_block[0]] = 0
        
        return True



