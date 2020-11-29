from game_parameters import car_collision_limit


# Functions
def detect_car_collision(player, cars):
    """ Evaluate if a car has collided with the player """

    for car in cars:
        if player.distance(car.position()) <= car_collision_limit:
            return True
