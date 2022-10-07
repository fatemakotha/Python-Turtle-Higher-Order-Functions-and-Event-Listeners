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
    pass




screen.listen() #starts listening
screen.onkey(key="w", fun=move_forwards) #calls the move forward function when spacebar is hit
screen.onkey(key="s", fun=move_backwards) #calls the move forward function when spacebar is hit
screen.onkey(key="a", fun=counter_clockwise) #calls the move forward function when spacebar is hit






screen.exitonclick()