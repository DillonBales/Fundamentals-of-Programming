import turtle
wn = turtle.Screen() 
leo = turtle.Turtle()
don = turtle.Turtle()

#Letter D
leo.color("blue") #Styling
leo.pensize(10)
leo.forward(50) #Botom Line

for i in range(6): #Curve
    leo.left(15)
    leo.forward(5)

leo.forward(75) #Right Line

for i in range(6): #Curve
    leo.left(15)
    leo.forward(5)

leo.forward(50)
leo.left(90)
leo.forward(113)
leo.left(90)
leo.forward(10)
leo.penup()
leo.forward(200) #Set up for next letter
leo.pendown()



#Letter B
leo.color("red") #Style
leo.shape("turtle")
leo.penup()

for i in range(2): #Bottom Line
    leo.forward(25)
    leo.stamp()

for i in range(3): #Curve
    leo.left(15)
    leo.forward(5)

leo.stamp()

for i in range(3):
    leo.left(15)
    leo.forward(5)

for i in range(3): #Right Line
    leo.stamp()
    leo.forward(25)

for i in range(3): #Curve
    leo.left(15)
    leo.forward(5)

leo.stamp()

for i in range(3):
    leo.left(15)
    leo.forward(5)

for i in range(2): #Top Line
    leo.stamp()
    leo.forward(25)

leo.left(90)
leo.stamp()

for i in range(4): #Left Line
    leo.forward(28)
    leo.stamp()

leo.left(90) #Positioning
leo.forward(51)

for i in range(6):
    leo.left(15)
    leo.forward(5)

leo.forward(37)
leo.left(90)


for i in range(3): #Middle line
    leo.forward(21)
    leo.stamp()

leo.left(90)
leo.forward(60)
leo.left(90)

#Letter J
don.shape("triangle") #Style
don.color("purple")
don.penup()
don.left(90) #Positioning 
don.forward(113)
don.right(90)
don.forward(100)

for i in range(3): #Top line
    don.stamp()
    don.forward(23)

don.stamp() #Positioning   
don.left(180)
don.forward(20)
don.left(90)

for i in range(10): #Middle Line
    don.forward(10)
    don.stamp()

for i in range(3): #Curve
    don.right(15)
    don.forward(5)

don.stamp()

for i in range(3):
    don.right(15)
    don.forward(5)

for i in range(2): #Bottom Line
    don.forward(5)
    don.stamp()

for i in range(3): #Curve
    don.right(15)
    don.forward(5)

don.stamp()

for i in range(3):
    don.right(15)
    don.forward(5)

wn.mainloop() 