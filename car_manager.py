import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        ran = random.randint(1, 6)
        if ran == 1:
            turtle = Turtle()
            turtle.penup()
            turtle.shape("square")
            turtle.shapesize(stretch_wid=1, stretch_len=2)
            turtle.color(COLORS[random.randrange(0, len(COLORS))])
            turtle.goto(280, random.randrange(-250, 250))
            self.all_cars.append(turtle)

    def move_forword(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

