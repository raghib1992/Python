from prettytable import PrettyTable


table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]

table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

print(table)


#------------------
new_table=PrettyTable()
new_table.add_column("Pokemon Name", ["Raichu", "Charmeleon", "Golbat"])
new_table.add_column("Type", ["Fire", "Water", "Poison"])
print(new_table)