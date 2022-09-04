from turtle import Turtle

# ----------------------------------------------- SET CONSTANTS --------------------------------------------------- #
SPEED = 20
XCOR = 0
YCOR = -250
COLOR = '#30AADD'
SHAPE = 'square'


# ---------------------------------------------- SET THE PADDLE CLASS --------------------------------------------- #
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        # config the paddle
        self.shape(SHAPE)
        self.shapesize(1, 10)
        self.color(COLOR)
        self.penup()
        self.speed("fastest")
        self.goto(XCOR, YCOR)

    # set the move right function
    def move_right(self):
        x_cor = self.xcor() + SPEED
        if x_cor < 270:
            self.goto(x_cor, self.ycor())

    # set the move left function
    def move_left(self):
        x_cor = self.xcor() - SPEED
        if x_cor > -270:
            self.goto(x_cor, self.ycor())
