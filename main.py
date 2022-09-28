import time
from turtle import Screen
from player import Player
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()

screen.onkey(player.move_forword, "Up")
car = CarManager()
game_is_on = True
myList = []

while game_is_on:
    car.create_car()
    car.move_forword()
    if player.ycor() + 10 == 280:
        car.level_up()
    time.sleep(0.1)
    screen.update()
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
