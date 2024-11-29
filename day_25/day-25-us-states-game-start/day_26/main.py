import pandas

# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)
#
# new_number = [2 * number for number in range(1, 5)]
# print(new_number)
#
# new_item = [2 * number for number in numbers if number % 2 == 0]
# print(new_item)

student_dict = {
    "student": ["vedant", "shaurya", "bhavay"],
    "score": [56, 78, 87]
}

# for (key, value) in student_dict.items():
#     print(value)

student_score_dataframe = pandas.DataFrame(student_dict)

# for (key, value) in student_score_dataframe.items():
#     print(value)
#     print(key)

for (index, row) in student_score_dataframe.iterrows():
    if row.student == "vedant":
        print(row.score)


