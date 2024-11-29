# from flask import Flask
#
# app = Flask(__name__)
#
# print(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# if __name__ == "__main__":
#     app.run()

# def add(first, second):
#     return first + second
#
#
# def calculate(calc_func, first, second):
#     return calc_func(first, second)
#
#
# result = calculate(add, 5, 10)
# print(result)


def outer_func():
    print("I'm a outer function.")

    def nested_func():
        print("I'm a nested function.")

    return nested_func


inner_func = outer_func()
inner_func()