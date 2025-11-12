import turtle # Allows us to use turtles

backgroundColor = input("Enter background Color: ")
penColor1 = input("Enter pen color: ")
penWidth1 = int(float(input("Enter pen width (1-10): ")))
penColor2 = input("Enter pen color: ")
penWidth2 = int(float(input("Enter pen width (1-10): ")))
penColor3 = input("Enter pen color: ") 
penWidth3 = int(float(input("Enter pen width (1-10): ")))

wn = turtle.Screen() # Creates a playground for turtles
wn.bgcolor(backgroundColor) # Set the window background color
wn.title("Hello, Tess!") # Set the window title

tess = turtle.Turtle()
tess.color(penColor1) # Tell tess to change her color
tess.pensize(penWidth1) # Tell tess to set her pen width

tess.forward(50)
tess.pensize(penWidth2)
tess.color(penColor2)
tess.left(120)
tess.forward(50)
tess.left(120)
tess.pensize(penWidth3)
tess.color(penColor3)
tess.forward(50)

wn.mainloop()