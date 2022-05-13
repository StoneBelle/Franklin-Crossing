import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from messages import Messages

#Screen SetUp
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#Game Objects & Variables
franklin = Player()\
car_manager = CarManager()
user_sees = Messages()

#Key Binds
screen.onkeypress(franklin.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.make_car()
    car.move()
    # TODO: If Franklin reaches end of road, reset his position back to the start, and update level on screen.
    if franklin.ycor() > 280:
        user_sees.level += 1
        franklin.next_lvl()
        
        car.up_car_spd()

    # else:
    #     for car in car.cars:
    #         if car.distance(franklin) < 20:
    #             game_is_on = False
    #             user_sees.end_game("Game Over. Franklin got hit by a car.")

    # if user_sees.level == 2:
    #     game_is_on = False
    #     user_sees.end_game("Congrats! You helped Franklin cross the road.")
    #     # TODO: Detect collision with car.

screen.mainloop()
