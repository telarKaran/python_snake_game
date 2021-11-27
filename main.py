from turtle import Screen, Turtle
def func():
    screen.bgcolor("pink")

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("purple")
screen.onkey( func ,"W")
screen.title("Snake_Game")



screen.exitonclick()