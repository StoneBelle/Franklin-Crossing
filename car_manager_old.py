from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_spd = STARTING_MOVE_DISTANCE

    def make_cars(self):
        for car in range(random.randint(2, 9)):
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.setpos(random.randrange(280, 450, 70), random.randrange(-250, 250, 50))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.bk(self.car_spd)
        if car.xcor() < 170:
            self.make_cars()

    def up_car_spd(self):
        self.car_spd += MOVE_INCREMENT

