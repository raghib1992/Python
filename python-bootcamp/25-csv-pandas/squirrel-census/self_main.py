import pandas

squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = squirrel["Primary Fur Color"].dropna()
new_colors = list(set(colors.tolist()))
# print(new_colors)

squirrel_data = dict()

counts = list()
for color in new_colors:
    count_data = int(squirrel["Primary Fur Color"].value_counts()[color])
    counts.append(count_data)

squirrel_data["Fur Color"] = new_colors
squirrel_data["Count"] = counts

print(squirrel_data)


squirrel_count = pandas.DataFrame(squirrel_data)
squirrel_count.to_csv("new_squirrel_count.csv")