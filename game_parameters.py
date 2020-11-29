from turtle import Screen
from math import sqrt


# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

FINISH_LINE_Y = 280

CAR_LENGTH = 40
CAR_WIDTH = 20


# Variables
limit_x = int(WINDOW_WIDTH/2)
car_collision_limit = sqrt((CAR_LENGTH/2)**2 + CAR_WIDTH**2)


# Functions
def game_screen():
    screen = Screen()
    screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    screen.title("Turtle Crossing")
    screen.tracer(0)

    return screen
