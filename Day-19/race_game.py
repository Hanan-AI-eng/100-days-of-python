from turtle import Turtle , Screen
from random import  randint

is_race_on= False
screen = Screen()
screen.setup(width=500, height=400)
user_pet=screen.textinput(title="Make your bet",prompt="What is your color you want?")
colors=["red","orange","yellow","green","blue","purple"]
y_place=[-100,-70,-40,0,40,80]
all_turtles=[]
screen.bgcolor("pink")

for turtle in range(0,6):
    new_turtle= Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.up()
    new_turtle.goto(x=-235, y=y_place[turtle])
    all_turtles.append(new_turtle)

if user_pet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_pet:
                print(f" You' ve won! {winning_color} turtle wins!")
            else:
                print(f" You' don't win {winning_color} turtle dose!")
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()
