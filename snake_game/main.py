import time
from helper import *

# init
init_length = 5
frame_width = 10
frame_height = 10

snake = Snake(frame_width, frame_height, init_length)
snake.start_position()
# snake.move(MoveDirection.FORWARD)
# snake.move(MoveDirection.RIGHT)
# snake.move(MoveDirection.RIGHT)
# snake.move(MoveDirection.FORWARD)
# print(snake.field)
# print(snake.snake)
# snake.move(MoveDirection.FORWARD)
# print(snake.field)
# print(snake.snake)
# snake.move(MoveDirection.FORWARD)
# print(snake.field)
# print(snake.snake)
# snake.move(MoveDirection.FORWARD)
# print(snake.field)
# print(snake.snake)
# snake.move(MoveDirection.LEFT)
# print(snake.field)
# print(snake.snake)
# snake.move(MoveDirection.FORWARD)
# print(snake.field)
# print(snake.snake)
# snake.move(MoveDirection.FORWARD)
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
move = True
while move:
    dir_list = np.array([MoveDirection.LEFT, MoveDirection.RIGHT, MoveDirection.FORWARD])
    temp = True
    while len(dir_list):
        direction = np.random.choice(dir_list)
        curr_field = np.copy(snake.field)
        curr_snake = np.copy(snake.snake)
        curr_directions = np.copy(snake.directions)
        temp = snake.move(direction)
        if not temp:
            snake.field = curr_field
            snake.snake = curr_snake
            snake.directions = curr_directions
            dir_list = np.delete(dir_list, np.where(dir_list == direction))
            continue
        else:
            break

    if len(dir_list) == 0:
        move = False

    # print(snake.snake)
    print(snake.field)
    time.sleep(0.5)
    print("-------------------------------------------------")

print(snake.directions)








        




