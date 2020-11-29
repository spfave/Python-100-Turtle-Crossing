from turtle import Turtle
from random import choice, randint


# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
VEHICLE_YLIMITS = (-250, 250)
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# Classes
class Car(Turtle):
    """  """

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.start_position()

    def start_position(self):
        # asterisks ahead of tuple/list reduces to values
        y = randint(*VEHICLE_YLIMITS)
        self.goto(300, y)

    def move(self, move_increment):
        x = self.xcor()
        y = self.ycor()+move_increment
        self.goto(x, y)


class CarManager:
    """  """

    def __init__(self):
        pass
