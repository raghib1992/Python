#Global Scope
player_health = 10

def drink_potion():
    potion_strenght = 2
    print(potion_strenght)

drink_potion()
print(player_health)

# There is no Block Scope
game_leve = 3
enemies = ["Skeleton", "Alien", "Zombie"]

if game_leve <5 :
    new_enemy = enemies[0]

print(new_enemy)

# MOdifying Global Scope
enemies = "skeleton"

def increase_enemies():
    global enemies
    enemies = "Zombie"
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

enemies = 2

def modify_enemies():
    print(f" Enemies inside function: {enemies}")
    return enemies + 1

enemies = modify_enemies()
print(f"Enemies outside function: {enemies}")

# Python Constant
PI = 3.14159

def cal():
    print(PI)