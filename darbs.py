from tkinter import *
from Ball import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"white") 
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow") 
basketball_ball = Ball(canvas,0,0,125,8,7,"orange")
weight_ball = Ball(canvas,0,0,150,1,1,"white") 




while True:
    volley_ball.move()
    tennis_ball.move()
    basketball_ball.move()
    weight_ball.move()
    window.update()
    


window.mainloop()