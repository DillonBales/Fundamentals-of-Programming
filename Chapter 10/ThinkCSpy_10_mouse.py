import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)
tess.shape("circle")

def h1(x, y):
   wn.title("Got click at coords {0}, {1}".format(x, y))
   tess.goto(x, y)

def h2(x,y):
   tess.clear()



wn.onclick(h1, 1)  # Wire up a click on the window.
wn.onclick(h2, 3)
wn.mainloop()