from turtle import*
pensize(3)
speed(10)
y=50
i=0
colors=["red","orange","yellow","green","blue","violet","purple"]
for i in range(7):
     pencolor(colors[i])
     y+=10
     i+=1
     penup()
     goto(10, 10-y)
     pendown()
     circle(y)
done()