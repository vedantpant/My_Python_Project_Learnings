import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_state = []

while len(guessed_state) < 50:
    state = screen.textinput(f"{len(guessed_state)}/50 States Correct", prompt="what's another state name?")
    state = state.title()
    state_data = pandas.read_csv("50_states.csv")
    states_name = state_data.state.tolist()

    for states in states_name:
        if states == state:
            guessed_state.append(state)
            loc = turtle.Turtle()
            loc.penup()
            loc.hideturtle()
            answer_check = state_data[state_data.state == state]
            x_cor = answer_check.x.values[0]
            y_cor = answer_check.y.values[0]
            loc.goto(x_cor, y_cor)
            loc.write(state)

    if state == "Exit":
        missing_state = [state for state in states_name if state not in guessed_state]
        missing_data = {"missing_states": missing_state}
        missing_data = pandas.DataFrame(missing_data)
        missing_data.to_csv("missing_data.csv")
        break
