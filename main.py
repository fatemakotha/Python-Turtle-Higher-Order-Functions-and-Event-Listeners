import turtle
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
#You can use the tim.left() method
def turn_left():
    tim.left(10)
#.........OR you can use the tim.setheading() method
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)



screen.listen() #starts listening
screen.onkey(key="w", fun=move_forwards) #calls the move_forward function when w is hit
screen.onkey(key="s", fun=move_backwards) #calls the move_backwards function when s is hit
screen.onkey(key="a", fun=turn_left) #calls the counter_clockwise function when a is hit
screen.onkey(key="d", fun=turn_right) #calls the clockwise function when d is hit





screen.exitonclick()