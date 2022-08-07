import turtle

import colorgram

# Extract 6 colors from an image.
# import colorgram.colorgram
#
# colors = colorgram.extract('image.jpeg', 10)
# rgb_colors = []
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
import random
color_list = [(189, 147, 125), (139, 89, 63), (239, 230, 223), (83, 85, 130), (149, 157, 179), (59, 32, 19), (170, 149, 160), (48, 54, 100), (32, 38, 61), (208, 210, 216)]


tim = turtle.Turtle()
screen = turtle.Screen()
tim.hideturtle()
tim.shape('turtle')
tim.speed(0)
tim.penup()
screen.colormode(255)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)



num_of_dots = 100
for dot_count in range(1, num_of_dots+1):
    random_color = random.choice(color_list)
    tim.dot(20, random_color)
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen.exitonclick()