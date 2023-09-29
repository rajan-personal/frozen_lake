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

class TileValue(Enum):
    EMPTY = 0.0
    SNAKE = 1.1
    SNAKE_HEAD = 1.2
    WALL = -1.0
    FOOD = 2.0


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
        field = np.full((length, breadth), TileValue.EMPTY.value)
        field = np.insert(field, 0, TileValue.WALL.value, axis=0)
        field = np.insert(field, length+1, TileValue.WALL.value, axis=0)
        field = np.insert(field, 0, TileValue.WALL.value, axis=1)
        field = np.insert(field, breadth+1, TileValue.WALL.value, axis=1)
        self.field = field
        self.directions = np.array([])

    def start_position(self):
        x, y = 6, 3
        head_position = np.array([x, y, Orientation.RIGHT, MoveDirection.FORWARD])
        tail_position = np.array([x-self.snake_size+1, y, Orientation.RIGHT, MoveDirection.FORWARD])
        self.field[y][x] = TileValue.SNAKE.value
        self.field[y][x-self.snake_size+1] = TileValue.SNAKE.value
        for i in range(1, self.snake_size):
            self.field[y][x-i] = TileValue.SNAKE.value
        self.snake = np.array([head_position, tail_position])

    def move(self, parent_move_dirr=MoveDirection.FORWARD):
        if len(self.snake) == 0:
            return False
        self.directions = np.append(self.directions, parent_move_dirr)
        print(parent_move_dirr)
        # move the snake
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
        self.field[last_block[1]][last_block[0]] = TileValue.EMPTY.value



        # add new head
        first_block = np.copy(self.snake[0])
        self.field[first_block[1]][first_block[0]] = TileValue.SNAKE.value
        dirr = first_block[2]
        # move_dirr = first_block[3]
        move_dirr = parent_move_dirr
        direction = calculate_next_direction(dirr, move_dirr)
        direction_value = direction.value
        new_head = np.array([first_block[0] + direction_value[0], first_block[1] + direction_value[1], direction, move_dirr])
        # check if new head is in snake body or wall
        if self.field[new_head[1]][new_head[0]] in [TileValue.SNAKE.value, TileValue.WALL.value, TileValue.SNAKE_HEAD.value]:
            self.field = np.zeros((self.length, self.breadth))
            self.snake = np.array([])
            return False
        if move_dirr == MoveDirection.FORWARD and len(self.snake) > 1:
            self.snake[0] = new_head
        else:
            self.snake = np.insert(self.snake, 0, new_head, axis=0)
            self.snake[1][3] = parent_move_dirr
        self.field[new_head[1]][new_head[0]] = TileValue.SNAKE_HEAD.value
        
        return True



