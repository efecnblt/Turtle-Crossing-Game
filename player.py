from turtle import Turtle
START_POSITION = (0, -280)
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.shapesize(1)
        self.goto_start()

    def move_forward(self):
        new_y_cor = self.ycor() + 16
        self.goto(self.xcor(), new_y_cor)

    #def move_back(self):
        #new_y_cor = self.ycor() - 16
        #self.goto(self.xcor(), new_y_cor),

    #def move_left(self):
        #new_x_cor = self.xcor() - 16
        #self.goto(new_x_cor, self.ycor())

    #def move_right(self):
        #new_x_cor = self.xcor() + 16
        #self.goto(new_x_cor, self.ycor())

    def at_finish(self):
        if self.ycor() > 280:
            return True
    def goto_start(self):
        self.goto(START_POSITION)