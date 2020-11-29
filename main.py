import time
import game_parameters as gp
import game_engine as ge
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Main --------------------------------------------------------------
# Game setup
screen = gp.game_screen()

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_forward)

# Run game
game_is_on = True
car_count = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)

    carmanager.randomly_add_car()
    carmanager.move_cars()

    if ge.detect_car_collision(player, carmanager.cars):
        game_is_on = False

screen.exitonclick()
