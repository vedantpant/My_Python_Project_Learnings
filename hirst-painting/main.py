# import colorgram
import turtle
from turtle import Turtle, Screen
import random

# colors = colorgram.extract('image.jpg', 6)
# list_of_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     list_of_colors.append(new_color)
#
#
# print(list_of_colors)

color_list = [(201, 158, 123), (240, 228, 232), (85, 162, 213)]

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.seth(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.seth(90)
        tim.forward(50)
        tim.seth(180)
        tim.forward(500)
        tim.seth(0)

screen = Screen()
screen.exitonclick()
