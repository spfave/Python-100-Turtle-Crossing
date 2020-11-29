from game_parameters import FINISH_LINE_Y


# Functions
def detect_car_collision(player, cars):
    """ Evaluate if a car has collided with the player """

    for car in cars:
        if player.distance(car) < 20:
            return True
    return False


def detect_road_crossing(player_yposition):
    """ Evaluate if the player crossed the road """
    if player_yposition > FINISH_LINE_Y:
        return True
    return False
