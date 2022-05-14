from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# TODO 2: Create a Player class.
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("olive")
        self.penup()
        self.seth(90)
        self.setpos(STARTING_POSITION)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def next_lvl(self):
        self.setpos(STARTING_POSITION)

