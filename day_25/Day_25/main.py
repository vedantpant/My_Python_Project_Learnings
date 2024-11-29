# # with open("weather_data.csv", 'r') as data:
# #     data = data.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         for column in data:
# #             temperature.append(int(column[1]))
# #         print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].tolist()
# #
# # print(data['temp'].mean())
# # print(data['temp'].max())
# #
# # print(data["condition"])
# # print(data.condition)
# #
# # # Get data in the row
# # print(data[data.day == "Monday"])
# #
# # # Get max temp from the row
# # print(data[data.temp == data["temp"].max()])
#
# # monday = data[data.day == "Monday"]
# # print((monday.temp[0] * (9/5)) + 32)
#
# # convert dataframe from scratch
#
# data_dict = {
#     "students": ["amy", "michael", "scott"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

fur_color_data = {"fur color": ["gray", "red", "black"],
                  "count": [gray_fur_count, red_fur_count, black_fur_count]
                  }

fur_data = pandas.DataFrame(fur_color_data)
fur_data.to_csv("fur_data.csv")












