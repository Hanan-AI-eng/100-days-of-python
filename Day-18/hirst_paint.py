import random
import turtle
from turtle import *
from random import choice
import turtle as t

# import colorgram
#
# rgb_colors=[]
# colors=colorgram.extract("image.jpd.jpg", 30)
# for color in colors:
#      r=color.rgb.r
#      g=color.rgb.g
#      b=color.rgb.b
#      new_rgb_color=(r,g,b)
#      rgb_colors.append(new_rgb_color)
#
# print(rgb_colors)
color_list = [(245, 246, 250), (252, 251, 247), (188, 74, 20), (56, 34, 13), (237, 226, 77), (24, 31, 60),
              (113, 167, 210), (45, 85, 143), (227, 243, 238), (217, 154, 82), (34, 50, 124), (191, 144, 25),
              (26, 51, 29), (201, 93, 126), (242, 214, 6), (250, 244, 249), (119, 35, 51), (120, 187, 149),
              (55, 129, 74), (70, 82, 17), (36, 84, 40), (142, 51, 58), (74, 128, 200), (205, 86, 62), (82, 31, 44),
              (104, 180, 70), (148, 204, 223), (197, 120, 162), (23, 77, 100)]

lamay = Turtle()
t.colormode(255)

lamay.shape("arrow")

color = choice(color_list)

def line_color():
    for i in range(10):
        color = choice(color_list)

        lamay.color(color)
        lamay.begin_fill()
        lamay.up()
        lamay.circle(20)
        lamay.down()
        lamay.end_fill()
        lamay.up()
        lamay.forward(50)
        lamay.down()


def next_line():
    for l in range(1):
        lamay.up()
        lamay.goto(l, 10)
        lamay.left(90)
        lamay.forward(50)
        lamay.right(90)
        lamay.down()


line_color()
next_line()
line_color()
lamay.left(180)
lamay.up()
lamay.forward(500)
lamay.right(90)
lamay.forward(50)
lamay.right(90)

lamay.down()
line_color()
lamay.left(180)
lamay.up()
lamay.forward(500)
lamay.right(90)
lamay.forward(50)
lamay.right(90)
line_color()
lamay.left(180)
lamay.up()
lamay.forward(500)
lamay.right(90)
lamay.forward(50)
lamay.right(90)
line_color()
lamay.left(180)
lamay.up()
lamay.forward(500)
lamay.right(90)
lamay.forward(50)
lamay.right(90)
line_color()
lamay.left(180)
lamay.up()
lamay.forward(500)
lamay.right(90)
lamay.forward(50)
lamay.right(90)
line_color()
lamay.left(180)
lamay.up()
lamay.forward(500)
lamay.right(90)
lamay.forward(50)
lamay.right(90)
line_color()




screen = Screen()
screen.exitonclick()
