from turtle import Screen


# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


# Variables
limit_x = int(WINDOW_WIDTH/2)


# Functions
def game_screen():
    screen = Screen()
    screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    screen.title("Turtle Crossing")
    screen.tracer(0)

    return screen
