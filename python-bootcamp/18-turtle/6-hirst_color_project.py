# import colorgram
import turtle
import random

# Fisrt part of project extract color from jpg image
# Extract 33 colors from an image.
# colors = colorgram.extract('hirst-color_dot.jpg', 33)

# color_list = list()
# for color in colors:
#     first_color = tuple()
#     first_color = (color.rgb.r,color.rgb.g,color.rgb.b)
#     color_list.append(first_color)


# from color create turtle drawing
color_list = [(23, 16, 94), (232, 43, 6), (153, 14, 30), (41, 181, 158), (127, 253, 206), (237, 71, 166), (209, 179, 208), (246, 218, 21), (40, 133, 242), (244, 247, 253), (246, 218, 5), (207, 148, 178), (126, 155, 204), (106, 189, 174), (224, 134, 117), (81, 87, 136), (150, 64, 75), (209, 87, 66), (49, 44, 100), (244, 168, 154), (175, 184, 222), (111, 9, 23), (179, 30, 10)]
print(len(color_list))

tim = turtle.Turtle()
tam = turtle.colormode(255)
screen = turtle.Screen()

y = -200.00


for _ in range(10):
    tim.penup()
    tim.setpos(-200.00,y)
    for _ in range(10):
        tim.dot(20,random.choice(color_list))
        tim.fd(40)
    y += 40.0
    print(tim.pos())
screen.exitonclick()

    
