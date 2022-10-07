import turtle
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def counter_clockwise():
    tim.left(5)
def clockwise():
    tim.right(5)




screen.listen() #starts listening
screen.onkey(key="w", fun=move_forwards) #calls the move_forward function when w is hit
screen.onkey(key="s", fun=move_backwards) #calls the move_backwards function when s is hit
screen.onkey(key="a", fun=counter_clockwise) #calls the counter_clockwise function when a is hit
screen.onkey(key="d", fun=clockwise) #calls the clockwise function when d is hit





screen.exitonclick()