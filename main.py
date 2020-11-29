import time
import game_parameters as gp
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Main --------------------------------------------------------------
# Game setup
screen = gp.game_screen()

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_forward)

# Run game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
