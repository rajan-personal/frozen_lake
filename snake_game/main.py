import time
from helper import *

# init
init_length = 2
frame_width = 10
frame_height = 10

snake = Snake(frame_width, frame_height, init_length)
snake.start_position()
# # snake.move(MoveDirection.FORWARD)
# snake.move(MoveDirection.RIGHT)
# # snake.move(MoveDirection.FORWARD)
# print(snake.field)
# print(snake.snake)
# snake.move(MoveDirection.RIGHT)
# print(snake.field)
# print(snake.snake)
# snake.move(MoveDirection.FORWARD)
# print(snake.field)
# print(snake.snake)
# snake.move(MoveDirection.RIGHT)
# print(snake.field)
# print(snake.snake)
# snake.move(MoveDirection.RIGHT)
# print(snake.field)
# print(snake.snake)
# snake.move(MoveDirection.FORWARD)
# print(snake.field)
# print(snake.snake)


# game loop
temp = True
while temp:
    direction = np.random.choice([MoveDirection.LEFT, MoveDirection.RIGHT, MoveDirection.FORWARD])
    temp = snake.move(direction)
    print(snake.snake)
    print(snake.field)
    # time.sleep(1)
    print("-------------------------------------------------")








        




