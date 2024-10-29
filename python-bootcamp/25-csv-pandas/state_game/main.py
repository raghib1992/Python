import turtle
import pandas


screen = turtle.Screen()
screen.title("US State Game")
screen.setup(width=800, height=600)
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# To get cursor co-ordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)


# Read us state csv file
us_data = pandas.read_csv('50_states.csv')
# print(state_data)





game_on = True
correct_guess = 0
guessed_state = []
while game_on:
    answer_state = turtle.textinput(title=f"{correct_guess}/50 Guess the state", prompt="What's another state name?")
    if answer_state in us_data.state.values and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        state_data = us_data[us_data.state == answer_state.title()]
        co_ord = (int(state_data.x), int(state_data.y))
        tom = turtle.Turtle()
        tom.penup()
        tom.goto(co_ord)
        tom.write(f"{answer_state}", align="center", font=('Arial',12,'normal'))
        tom.hideturtle()
        correct_guess += 1
        if  correct_guess == 50:
            game_on = False
    else:
        pass





# while game_on:
# answer_state = turtle.textinput(title=f"{correct_guess}/25 Guess the state", prompt="What's another state name?")
# if answer_state in  
    # print(answer_state)
    # 
    # state_data = us_data[us_data.state.str.lower() == answer_state.lower()]
    # if state_data is not None:
    #     guessed_state.append(answer_state)
    #     correct_guess += 1
    #     x_coord = int(state_data.x)
    #     y_coord = int(state_data.y)
    #     co_ord = (x_coord,y_coord)
    #     print(co_ord)

        
    #     if correct_guess == 25:
    #         game_on = False
    # else:
    #     pass
screen.exitonclick()