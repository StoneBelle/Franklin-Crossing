from turtle import Turtle

FONT = ("Courier", 14, "normal")


# TODO 4: Create a class to show users a screen message.
class Message(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-230, 260)
        self.level = 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def end_game(self, text1, text2):
        self.setpos(0, 20)
        self.write(text1, align="center", font=FONT)
        self.setpos(0, -10)
        self.write(text2, align="center", font=FONT)