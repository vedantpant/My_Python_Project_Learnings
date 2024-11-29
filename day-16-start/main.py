# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# sandra = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
#
# print(sandra)
# sandra.color("green")
# sandra.shape("turtle")
# sandra.backward(500)
#
# timmy.forward(100)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


table.add_column("pokemon_name", ["Pikachu", "Bulbasaur", "Charizard"])
table.add_column("type", ["electric", "grass", "fire"])

table.align = 'c'
print(table)
