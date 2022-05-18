import time
from turtle import Screen
from franklin import Player
from car_manager import CarManager
from messages import Message

# Screen SetUp
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("oldlace")
screen.tracer(0)

# Game Objects
message = Message()
franklin = Player()
car = CarManager()
car.make_cars()

# Key Binds
screen.listen()
screen.onkeypress(franklin.move, "Up")
# TODO 2.1: Control player object with "Up" key.
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()

    # TODO 3: Detect if player comes into collision with car.
    for zoom in car.cars:
        if zoom.distance(franklin) < 20:
            game_is_on = False
            message.end_game("GAMEOVER.", "Franklin got hit by a car.")

    # TODO 4.1: If player successfully crosses road, reset their position and update level on screen.
    if franklin.ycor() > 280:
        message.level += 1
        message.update_text()
        franklin.next_lvl()
        car.up_car_spd()

    if message.level == 6:
        game_is_on = False
        message.end_game("CONGRATS!", "You helped Franklin cross the road.")

screen.exitonclick()
