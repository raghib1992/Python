travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
# Do NOT change the code above

# Write the function that will allow new countries
# To be added to the travel_log. 👇

def add_new_country(new_country,new_visits,new_cities):
    new_add = {}
    new_add["country"] = new_country
    new_add["visits"]  = new_visits
    new_add["cities"]  = new_cities
    travel_log.append(new_add)

new_country = input("Name the county: ")
new_visits = input("Number of time visits: ")
new_cities_x = input("Which cities visits: ")
new_cities_list = new_cities_x.split(",")
add_new_country(new_country,new_visits,new_cities=new_cities_list)
print(travel_log)travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇


def add_new_country(country,visits,cities):
    new_dict = {}
    new_dict["country"] = country
    new_dict["visits"] = visits
    new_dict["cities"] = cities
    travel_log.append(new_dict)
    print(new_dict)
    return

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

