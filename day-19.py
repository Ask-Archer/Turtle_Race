from turtle import Turtle, Screen

import random

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win? Enter a color: ")


colors = ["red","orange", "yellow", "green", "blue", "purple"]

y_list = [-70, -40, -10, 20, 50, 80]

all_turtles= []

for turtle_index in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(x=-230, y=y_list[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
              print(f"You've won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You lost. The {winning_color} turtle is the winner. ")
        rand_distance = random.randint(0, 10)
        turtle.forwards(rand_distance)

screen.exitonclick()
