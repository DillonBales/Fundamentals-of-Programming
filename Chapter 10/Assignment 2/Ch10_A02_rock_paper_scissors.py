import turtle
import random

screen = turtle.Screen()

screen.bgcolor("lightblue")

rock = "Rock.gif"
paper = "Paper.gif"
scissors = "Scissors.gif"

screen.addshape(rock)
screen.addshape(paper)
screen.addshape(scissors)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
score_writer = turtle.Turtle()

score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0,200)

t1.shape(rock)
t2.shape(paper)
t3.shape(scissors)

t1.penup()
t2.penup()
t3.penup()

t1.backward(250)
t3.forward(250)

user_choice = 0
computer_choice = 0
computer_score = 0
user_score = 0


#You may want to take a look at this method
# print(random.randint(3, 9))

def choose_rock():
    global user_choice
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t1.clearstamps()
    t2.clearstamps()
    t3.clearstamps()
    t1.speed(0)
    t1.goto(0,0)
    t1.showturtle()
    t1.speed(1)
    t1.forward(200)
    t1.stamp()
    screen.ontimer(show_computer_choice, 1000)
    user_choice = 1 


def choose_paper():
    global user_choice
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t1.clearstamps()
    t2.clearstamps()
    t3.clearstamps()
    t2.speed(0)
    t2.goto(0,0)
    t2.showturtle()
    t2.speed(1)
    t2.forward(200)
    t2.stamp()
    screen.ontimer(show_computer_choice, 1000)
    user_choice = 2  


def choose_scissors():
    global user_choice 
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t1.clearstamps()
    t2.clearstamps()
    t3.clearstamps()
    t3.speed(0)
    t3.goto(0,0)
    t3.showturtle()
    t3.speed(1)
    t3.forward(200) 
    t3.stamp()
    screen.ontimer(show_computer_choice, 1000)
    user_choice = 3



def show_computer_choice():
    global computer_choice, user_score, computer_score
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        t1.hideturtle()
        t2.hideturtle()
        t3.hideturtle()
        t1.speed(0)
        t1.goto(0,0)
        t1.backward(200)
        t1.showturtle()
    elif computer_choice == 2:
        t1.hideturtle()
        t2.hideturtle()
        t3.hideturtle()
        t2.speed(0)
        t2.goto(0,0)
        t2.backward(200)
        t2.showturtle()
    else:
        t1.hideturtle()
        t2.hideturtle()
        t3.hideturtle()
        t3.speed(0)
        t3.goto(0,0)
        t3.backward(200)
        t3.showturtle()
    
    if user_choice == computer_choice:
        pass
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        user_score = user_score + 1
    else:
        computer_score = computer_score + 1
    
    update_scores()

def update_scores():
    score_writer.clear()
    score_writer.write(f"Player: {user_score}  Computer: {computer_score}", align="center", font=("Arial", 20, "bold"))


screen.onkey(choose_rock, "r")
screen.onkey(choose_paper, "p")
screen.onkey(choose_scissors, "s")

screen.listen()
screen.mainloop() # Wait for user to close window

