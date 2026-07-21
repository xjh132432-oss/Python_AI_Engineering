from turtle import *
speed(0)
pensize(1.5)
pencolor("red")
x=500
penup()
goto(0,-200)
pendown()
right(85)
fillcolor("yellow")
begin_fill()
for i in range(36):
    left(170)
    forward(x)
end_fill()
hideturtle()
#五角星


done()