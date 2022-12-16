from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "blue", "green", "purple", "pink"]
MOVE_INCREMENT = 5
STARTING_MOVE_DISTANCE = 5

class Rectangles:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_segment(self):
        chance = random.randint(1, 6)
        if chance == 1:
            turtle = Turtle(shape="square")
            turtle.penup()
            turtle.color(random.choice(COLORS))
            turtle.shapesize(stretch_len=2, stretch_wid=1)
            turtle.goto(300, random.randint(-250, 250))
            self.all_cars.append(turtle)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT