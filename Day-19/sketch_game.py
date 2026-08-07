from turtle import Turtle , Screen

tim= Turtle()
screen = Screen()

def move_forwards():
    tim.forward(20)

def move_back():
    tim.backward(20)

def counter_clock():
    tim.left(10)

def clock():
    tim.right(10)
def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="q", fun=clear)
screen.exitonclick()
