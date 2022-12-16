from turtle import  Screen
from player import Player
from rectangles import Rectangles
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
scoreboard = Scoreboard()

player = Player()
rectangle = Rectangles()

screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.listen()

screen.onkeypress(player.move_forward, "Up")
#screen.onkeypress(orientation.move_back, "Down")
#screen.onkeypress(orientation.move_left, "Left")
#screen.onkeypress(orientation.move_right, "Right")


scoreboard.scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    rectangle.create_segment()
    rectangle.move_cars()
    for car in rectangle.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    if player.at_finish():
        player.goto_start()
        rectangle.level_up()
        scoreboard.increase_score()
screen.exitonclick()