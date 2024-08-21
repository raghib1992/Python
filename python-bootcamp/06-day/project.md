# Link https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
## code 
```py
def jump():
    turn_left()
    move()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear() and not right_is_clear():
        move()
    else:
        turn_left()
```