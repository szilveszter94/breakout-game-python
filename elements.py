from turtle import Turtle
import random

# ----------------------------------------------- SET CONSTANTS --------------------------------------------------- #
colors = ['#FF6B6B', '#FFD93D', '#6BCB77', '#4D96FF']
SHAPE = "square"


# draw all square elements
def draw_elements():
    e_list = []
    for y in range(50, 171, 30):
        for i in range(-300, 301, 50):
            elements = Elements(i, y)
            e_list.append(elements)
    return e_list


# ----------------------------------------------- SET ELEMENTS CLASS ------------------------------------------------ #
class Elements(Turtle):
    def __init__(self, xcor, ycor):
        # config square elements
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(1, 2)
        color = random.choice(colors)
        self.color(color)
        self.penup()
        self.speed("fastest")
        self.goto(xcor, ycor)
