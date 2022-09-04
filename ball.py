from turtle import Turtle

# ---------------------------------------------- SET THE PADDLE CLASS --------------------------------------------- #
SPEED = -10
COLOR = '#826F66'
SHAPE = 'circle'
SIZE = 1.5


# ---------------------------------------------- SET THE PADDLE CLASS --------------------------------------------- #
class Ball(Turtle):
    def __init__(self, x_cor, y_cor):
        # config the ball
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(SIZE)
        self.color(COLOR)
        self.penup()
        self.speed("fastest")
        self.goto(x_cor, y_cor)
        self.y_move = SPEED
        self.x_move = SPEED

    # set the move forward function
    def move_forward(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    # manage the collision with the wall
    def collision_with_wall(self):
        if self.ycor() > 260:
            self.y_move *= -1
        if self.xcor() > 360 or self.xcor() < -360:
            self.x_move *= -1

    # manage bouncing
    def bouncing(self):
        self.y_move *= -1

    # manage left side collision
    def left_side_collision_with_paddle(self):
        self.y_move *= -1
        self.x_move = -10

    # manage right side collision
    def right_side_collision_with_paddle(self):
        self.y_move *= -1
        self.x_move = 10

    # manage middle collision
    def middle_collision_with_paddle(self):
        self.y_move *= -1
        self.x_move *= -0.1

    # reset the ball
    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(-200, 0)
        self.write(f'GAME OVER', font=('consolas', 60, 'bold'))
