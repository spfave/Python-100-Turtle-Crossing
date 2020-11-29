from turtle import Turtle
from random import choice, randint
from game_parameters import WINDOW_WIDTH, CAR_LENGTH


# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
VEHICLE_XLIMIT = WINDOW_WIDTH/2+CAR_LENGTH/2
VEHICLE_YLIMIT = 240
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
        y = randint(-VEHICLE_YLIMIT, VEHICLE_YLIMIT)
        self.goto(VEHICLE_XLIMIT, y)

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
        """ Add car to car manager list """
        new_car = Car()
        self.cars.append(new_car)

    def filter_car_removal(self):
        """ Remove cars that have exited window """
        [car for car in self.cars if car.xcor() < -VEHICLE_XLIMIT]

    def randomly_add_car(self):
        """ Add car to cars with propability of 1 out of 6 """
        if randint(1, 6) == 1:
            self.add_car()

    def move_cars(self):
        """ Move cars forward """
        for car in self.cars:
            car.move(self.cars_speed)
        self.filter_car_removal()

    def increase_speed(self):
        """ Increase speed of cars """
        self.cars_speed += MOVE_INCREMENT
