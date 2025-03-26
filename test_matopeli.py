import pytest
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

# Import the classes from the provided code
from matopeli import Snake, Food, CELL_SIZE, WIDTH, HEIGHT

@pytest.fixture
def snake():
    return Snake()

@pytest.fixture
def food():
    return Food()

def test_snake_initial_position(snake):
    assert snake.body == [(100, 100), (90, 100), (80, 100)]

def test_snake_move(snake):
    snake.move()
    assert snake.body == [(120, 100), (100, 100), (90, 100)]

def test_snake_grow(snake):
    snake.grow()
    assert len(snake.body) == 4

def test_snake_collision_with_wall(snake):
    snake.body[0] = (0, 0)
    snake.direction = (-CELL_SIZE, 0)
    snake.move()
    assert snake.check_collision() == True

def test_snake_collision_with_self(snake):
    snake.body = [(100, 100), (90, 100), (80, 100), (100, 100)]
    assert snake.check_collision() == True

def test_food_random_position(food):
    pos = food.random_position()
    assert pos[0] % CELL_SIZE == 0
    assert pos[1] % CELL_SIZE == 0
    assert 0 <= pos[0] < WIDTH
    assert 0 <= pos[1] < HEIGHT

def test_snake_eat_food(snake, food):
    food.position = snake.body[0]
    if snake.body[0] == food.position:
        snake.grow()
        food.position = food.random_position()
    assert len(snake.body) == 4