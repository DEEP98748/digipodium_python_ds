'''from turtle import *

#DrawStaircase

bgcolor ('white')
pendown ()
pensize (5)
pencolor ('red')
x , y = 0 , 0

for i in range (5):
    goto (x,y)
    left (90)
    x =x + 100
    goto (x ,y)
    y = y +100
    right (90)

    exitonclick () '''

import turtle 
 
def draw_stairs (t, num_step , num_size):
    for i in range (num_step):
        t.forward('step_size')
        t.left (90)
        t.forward('step_size')
        t.right (90)

t = turtle.Turtle()    
t.speed (1)
draw_stairs (t , 5 ,50)
turtle.done()
    






