# with open("weather_data.csv") as file:
#     weather_data = file.readlines()

# print(weather_data)

# import csv


# with open("weather_data.csv") as file:
#     csv_data = csv.reader(file)
#     temperature = []

#     for row in csv_data:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(row[1])

#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

# data_list = data["temp"].to_list()
# print(data_list)

# temp_avg = sum(data_list)/len(data_list)
# print(round(temp_avg,3)) 


# print(data["temp"].mean())


# print(f"max temp {data["temp"].max()}")

# print(data.day)


# print(data[data.day == "Monday"])


# Print the column for max temp
# print(data[data.temp == data.temp.max()])

monday_temp = (data[data.day == "Monday"].temp * 9/5) + 32
print(monday_temp)


# Create dataframe from scratch
data_dict = {
    "student": ["Any", "James", "Angela"],
    "scores": [76,54,32]
}

data= pandas.DataFrame(data_dict)

data.to_csv("new.csv")