# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for each_day_data in data:
#         if each_day_data[1] != "temp":
#             temperature.append(int(each_day_data[1]))
#
# print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# # csv data to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# csv data to list
# temp_list = data["temp"].to_list()
# print(temp_list)

# method 1: traditional method
# average_temperature = round(sum(temp_list) / len(temp_list), 2)

# # method 2: using pandas
# average_temperature = round(data["temp"].mean(), 2)
# print(f"Average of temperature list: {average_temperature}")

# # max temperature
# max_temp = data["temp"].max()
# print(f"Maximum temperature: {max_temp}")

# # get access of column
# print(data["condition"])
# print(data.condition)

# # get access of rows
# print(data[data["condition"] == "Sunny"])
# print(data[data.condition == "Sunny"])

# # max temperature day row
# max_temp = data["temp"].max()
# max_temp_day = data[data["temp"] == max_temp]
# print(f"Maximum temperature Day: {max_temp_day}")

# # get access of particular row's data
# monday = data[data["day"] == "Monday"]
# print(monday.condition)
# print(monday["temp"])

# # exercise: convert monday's temperature from Celsius to Fahrenheit
monday = data[data["day"] == "Monday"]
Fahrenheit = (monday.temp[0] * 9 / 5) + 32
print(f"Monday's temperature is: {Fahrenheit}")

tuesday = data[data["day"] == "Tuesday"]
Fahrenheit = (tuesday.temp[1] * 9 / 5) + 32
print(f"Monday's temperature is: {Fahrenheit}")


# # create a dataframe from a scratch using pandas
# data_dict = {
#     "students": ["Tom", "Jerry", "Jack"],
#     "marks": [70, 80, 90]
# }
# student_data = pandas.DataFrame(data_dict)
# print(student_data)
# # create a csv file from the dictionary
# student_data.to_csv("student_data.csv")


squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240423.csv")

# # method 1
# raw_primary_colors = squirrel_data["Primary Fur Color"].unique()
# primary_colors = []
# for primary_color in raw_primary_colors[1:]:
#     primary_colors.append(primary_color)
# # print(primary_colors)
#
# gray_squirrels = 0
# cinnamon_squirrels = 0
# black_squirrels = 0
#
# for squirrel_color in squirrel_data["Primary Fur Color"]:
#     if squirrel_color == "Gray":
#         gray_squirrels += 1
#     elif squirrel_color == "Cinnamon":
#         cinnamon_squirrels += 1
#     elif squirrel_color == "Black":
#         black_squirrels += 1
#
# # print(f"gray_squirrels = {gray_squirrels}")
# # print(f"cinnamon_squirrels = {cinnamon_squirrels}")
# # print(f"black_squirrels = {black_squirrels}")
#
# number_of_squirrels = [gray_squirrels, cinnamon_squirrels, black_squirrels]
#
# squirrel_data_dict = {
#     "Fur Color": primary_colors,
#     "Count": number_of_squirrels
# }
# print(squirrel_data_dict)
#
# squirrel_count_csv = pandas.DataFrame(squirrel_data_dict)
# squirrel_count_csv.to_csv("squirrel_count.csv")

# method 2
gray_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}
# print(squirrel_data_dict)

squirrel_count_csv = pandas.DataFrame(squirrel_data_dict)
squirrel_count_csv.to_csv("squirrel_count.csv")
