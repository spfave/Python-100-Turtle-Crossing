from turtle import Turtle


# Constants
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280
MOVE_DISTANCE = 10


# Classes
class Player(Turtle):
    """ Player """

    def __init__(self):
        """  """
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.reset()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)
