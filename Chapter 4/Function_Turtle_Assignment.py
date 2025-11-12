import turtle
wn = turtle.Screen() 
leo = turtle.Turtle()
don = turtle.Turtle()

#Letter D
def letterD(color, t):
    t.color(color) #Styling
    t.pensize(10)
    
    t.forward(50) #Botom Line

    for i in range(6): #Curve
        t.left(15)
        t.forward(5)

    t.forward(75) #Right Line

    for i in range(6): #Curve
        t.left(15)
        t.forward(5)

    t.forward(50)
    t.left(90)
    t.forward(113)
    t.left(90)
    t.forward(10)
    t.penup()
    t.forward(200) #Set up for next letter
    t.pendown()



#Letter B
def letterB(color, shape, t):
    t.color(color) #Style
    t.shape(shape)
    t.penup()

    for i in range(2): #Bottom Line
        t.forward(25)
        t.stamp()

    for i in range(3): #Curve
        t.left(15)
        t.forward(5)

    t.stamp()

    for i in range(3):
        t.left(15)
        t.forward(5)

    for i in range(3): #Right Line
        t.stamp()
        t.forward(25)

    for i in range(3): #Curve
        t.left(15)
        t.forward(5)

    t.stamp()

    for i in range(3):
        t.left(15)
        t.forward(5)

    for i in range(2): #Top Line
        t.stamp()
        t.forward(25)

    t.left(90)
    t.stamp()

    for i in range(4): #Left Line
        t.forward(28)
        t.stamp()

    t.left(90) #Positioning
    t.forward(51)

    for i in range(6):
        t.left(15)
        t.forward(5)

    t.forward(37)
    t.left(90)


    for i in range(3): #Middle line
        t.forward(21)
        t.stamp()

    t.left(90)
    t.forward(60)
    t.left(90)

#Letter J
def letterJ(color, shape, t):
    t.shape(shape) #Style
    t.color(color)
    t.penup()
    t.left(90) #Positioning 
    t.forward(113)
    t.right(90)
    t.forward(100)

    for i in range(3): #Top line
        t.stamp()
        t.forward(23)

    t.stamp() #Positioning   
    t.left(180)
    t.forward(20)
    t.left(90)

    for i in range(10): #Middle Line
        t.forward(10)
        t.stamp()

    for i in range(3): #Curve
        t.right(15)
        t.forward(5)

    t.stamp()

    for i in range(3):
        t.right(15)
        t.forward(5)

    for i in range(2): #Bottom Line
        t.forward(5)
        t.stamp()

    for i in range(3): #Curve
        t.right(15)
        t.forward(5)

    t.stamp()

    for i in range(3):
        t.right(15)
        t.forward(5)

def draw_square(t, size, color):
    t.color(color)
    for i in range(4):
        t.forward(size)
        t.left(90)



def draw_initials():
    letterD("blue", leo)
    letterB("red", "turtle", leo)
    letterJ("purple", "triangle", don)

draw_initials()

leo.right(90)
leo.forward(100)
leo.right(90)
leo.forward(200)
leo.left(180)
leo.pendown()

for i in range(5):
    draw_square(leo, 20, "black")
    leo.penup()
    leo.forward(60)
    leo.pendown()


wn.mainloop() 