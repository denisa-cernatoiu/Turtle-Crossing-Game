from turtle import Turtle
from random import randint


class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x=310, y=randint(-240,250))
        self.movement = 10

    def go(self):
        rand_dist = randint(0,self.movement)
        self.backward(rand_dist)

    def increase_speed(self):
        self.movement += 5
