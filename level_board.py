from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 18, 'bold')

class LevelBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(x = -240, y = 260)
        self.color("purple4")
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-240,260)
        self.write(f"LEVEL {self.level}", align= ALIGNMENT, font = FONT)

    def next_level(self):
        self.level +=1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align= ALIGNMENT, font= FONT)