from turtle import Turtle, Screen
import random

is_race_on = False
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_pos = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.shape()
    new_turtle.goto(x=-230, y=y_pos[turtle])
    all_turtles.append(new_turtle)

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter the color: ")
print(user_bet)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won!!! The {winning_color} turtle is the winner!")
            else:
                print(f"you've lost!!! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
        