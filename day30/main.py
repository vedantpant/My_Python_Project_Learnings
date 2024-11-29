# file not found error
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"there is a key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file wss closed")
#     raise TypeError("this is the error made up by me.")
# key error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existing key"]

# index error
# fruit_list = ["apple", "oranges", "banana"]
# fruit = fruit_list[3]

# data error
# text = "abc"
# print(text + 5)

height = float(input("enter the height?"))
weight = float(input("enter the weight?"))

if height > 3:
    raise ValueError("HUMAN HEIGHT SHOULD NOT BE MORE THAN 3 METRES")
bmi = weight / (height * height)
print(bmi)
