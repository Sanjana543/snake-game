import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

#set up screen
wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)#turns off screen updates

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)

snakebody = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0",align ="center",font=("Courier",24,"normal"))

#functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")
   
#main game loop
while True:
    wn.update()
    #border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide the snakebody
        for body in snakebody:
           body.goto(1000,1000)

        #clear the list
        snakebody.clear()

        #reset the score
        score = 0
        
        #reset the delay
        delay = 0.1

       #update the score display
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),align="center",font=("Courier",24,"normal"))

    #eating food
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        
    #add body
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("blue")
        body.penup()
        snakebody.append(body)

    #shorten the delay
        delay -= 0.001
    #increase score
        score +=10
        if score >high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),align="center",font=("Courier",24,"normal"))

    #move the end body piece first in reverse order
    for index in range(len(snakebody)-1,0,-1):
            x = snakebody[index-1].xcor()
            y = snakebody[index-1].ycor()
            snakebody[index].goto(x,y)

    #move body with head
    if len(snakebody) > 0:
            x = head.xcor()
            y = head.ycor()
            snakebody[0].goto(x,y)
        
    move()

    #body collision
    for body in snakebody:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            #hide the snakebody
            for body in snakebody:
                body.goto(1000,1000)

            #reset the score
                score = 0

            #clear the list
            snakebody.clear()
         
            #reset the delay
            delay = 0.1

            #update the score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score),align="center",font=("Courier",24,"normal"))

    time.sleep(delay)
    
wn.mainloop()

