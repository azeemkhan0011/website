from turtle import *
speed(10)
color('cyan')
bgcolor('black')
penup()
goto(220,-30)
pendown()
b= 200
while b>0:
    right(b)
    forward(b * 3)
    b = b-1
mainloop()