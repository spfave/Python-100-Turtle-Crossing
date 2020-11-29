import time
import game_parameters as gp
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

    if car_count == 0:
        carmanager.add_car()
        car_count += 1
    elif car_count == 5:
        car_count = 0
    else:
        car_count += 1
    carmanager.move_cars()

screen.exitonclick()
