from prettytable import PrettyTable


table = PrettyTable()



table.add_column("Pokemon Name", ["Pikachu", "Squirtle","Charmondor"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)