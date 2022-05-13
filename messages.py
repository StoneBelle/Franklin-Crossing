from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Messages(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-230, 260)
        self.level = 1
        self.display_text(f"Level: {self.level}")

    def display_text(self, text):
        self.write(text, align="center", font=FONT)

    def update_text(self):
        self.clear()
        self.display_text(f"Level: {self.level}")

    def end_game(self, text):
        self.setpos(0, 0)
        self.display_text(text)
