def add(*args):
    print(args[1])
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 3, 4, 5, 6, 7))


def calculate(n, **kwargs):
    print(kwargs["add"])
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seat = kwargs.get("seat")


my_car = Car(make="Nissan", model="gtr")
print(my_car.model)

