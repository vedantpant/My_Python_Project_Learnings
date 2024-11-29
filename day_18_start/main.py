import turtle
from turtle import Turtle, Screen
import random
# from typing import List

# import heroes

# import turtle as t
# tim = t.Turtle()

timmy = Turtle()

# print(heroes.gen())

# timmy.shape("turtle")

colors = ["dark green", "dark salmon", "peru", "midnight blue", "yellow", "orange", "antique white", "maroon",
          "slate blue", "dark orange"]


# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for i in range(3, 11):
#     timmy.pencolor(random.choice(colors))
#     draw_shapes(i)

# random walk

keep_drawing = True
direction = [0, 90, 180, 270]
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


# while keep_drawing:
#     timmy.pensize(5)
#     timmy.color(random_color())
#     timmy.speed("fast")
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))

# draw a spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.speed("fastest")
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
