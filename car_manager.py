from turtle import Turtle
from random import choice, randint
from game_parameters import limit_x


# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
VEHICLE_YLIMITS = (-240, 240)
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


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
        """ Place car at random start position on right side """
        # asterisks ahead of tuple/list reduces to values
        y = randint(*VEHICLE_YLIMITS)
        self.goto(limit_x, y)

    def move(self, move_increment):
        """ Move car forward """
        x = self.xcor()-move_increment
        self.setx(x)


class CarManager:
    """  """

    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        new_car = Car()
        self.cars.append(new_car)

    def randomly_add_car(self):
        if randint(1, 6) == 1:
            self.add_car()

    def move_cars(self):
        for car in self.cars:
            car.move(self.cars_speed)

    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT
