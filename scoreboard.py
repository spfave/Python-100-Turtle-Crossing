from turtle import Turtle


# Constants
TEXT_ALIGNMENT_LEVEL = "left"
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
        """ Write level to screen """
        self.clear()
        self.write(f"Level: {self.level}",
                   align=TEXT_ALIGNMENT_LEVEL, font=TEXT_FONT)

    def level_up(self):
        """ Increase level """
        self.level += 1
        self.write_level()

    def game_over(self):
        """ Indicate game over """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=TEXT_FONT)
