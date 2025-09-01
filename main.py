from turtle import Screen
from cars import Car
from my_turtle import MyTurtle
from level_board import LevelBoard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.colormode(255)

all_cars = []
for _ in range(9):
    new_car = Car()
    all_cars.append(new_car)

timi_the_racer = MyTurtle()
screen.listen()
screen.onkey(timi_the_racer.go_up, "Up")

level = LevelBoard()

car_counter = 0
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    # adding new cars
    car_counter += 1
    if car_counter % 6 == 0: 
        new_car = Car()
        all_cars.append(new_car)

    # detecting collision with cars
    for car in all_cars:
        car.go()
        if timi_the_racer.distance(car) < 25:
            level.game_over()
            game_on = False
    
    # detect going past the finish line and getting to next level
    if timi_the_racer.ycor() > 290:
        level.next_level()
        timi_the_racer.reset_pos()
        for car in all_cars:
            car.increase_speed()

    


screen.exitonclick()
