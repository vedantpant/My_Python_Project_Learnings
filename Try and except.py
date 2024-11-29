'''
check program for breaking error
and avoid those errors here
'''

try:
    answer = 10/0
    number = int(input("enter a number here: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
