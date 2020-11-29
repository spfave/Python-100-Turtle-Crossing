from turtle import Turtle


# Constants
TEXT_ALIGNMENT = "left"
TEXT_FONT = ("Courier", 16, "normal")
SCOREBOARD_POSITION = (-285, 265)


# Classes
class Scoreboard(Turtle):
    """ Level indicator """

    def __init__(self):
        """  """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.level = 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level}",
                   align=TEXT_ALIGNMENT, font=TEXT_FONT)

    def increase_level(self):
        self.level += 1
