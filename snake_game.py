import turtle
import time
import random

delay=0.1
score=0
highest_score=0

win=turtle.Screen()
win.title("Snake Game")
win.bgcolor("blue")

win.setup(width=600,height=600)
win.tracer(0)

head=turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction="Stop"

target=turtle.Turtle()
colors=random.choice(['red','green','yellow'])
shapes=random.choice(['square','circle','triangle'])
target.speed(0)
target.shape(shapes)
target.color(colors)
target.penup()
target.goto(0,100)

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score:0 High Score:0",align="center",font=("candara",24,"bold"))

#directions
def goup():
    if head.direction!="down":
        head.direction="up"

def godown():
    if head.direction!="up":
        head.direction="down"

def goleft():
    if head.direction!="right":
        head.direction="left"

def goright():
    if head.direction!="left":
        head.direction="right"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.sety(x-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

win.listen()
win.onkeypress(goup,"w")
win.onkeypress(godown,"s")
win.onkeypress(goleft,"a")
win.onkeypress(goright,"d") 


segments=[]


#Main Gameplay
while True:
    win.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="Stop"
        colors=random.choice(['blue','green','yellow'])
        shapes=random.choice(['square','circle'])
        for segment in segments:
            segment.goto(1000,1000)
            segments.clear()
            score=0
            delay=0.1
            pen.clear()
            pen.write("Score:{} High Score:{}".format(
                score,highest_score),align="center",font=("candara",24,"bold"))
    if head.distance(target)<20:
        x=random.randint(-250,250)
        y=random.randint(-250,250)
        target.goto(x,y)
#adding new segment
    new_segment=turtle.Turtle()
    new_segment.speed(0) 
    new_segment.shape("circle")
    new_segment.color("red")
    new_segment.penup()
    segments.append(new_segment)
    delay-=0.005
    score+=15
    if score>highest_score:
        highest_score=score
    pen.clear()
    pen.write("Score:{} High Score:{}".format(
                score,highest_score),align="center",font=("candara",24,"bold"))
    
#check for head and tail collisions
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="Stop"
            colors=random.choice(['red','green','yellow'])
            shapes=random.choice(['circle','square'])
            for segment in segments:
                segment.goto(1000,1000)
                segments.clear()

                score=0
                delay=0.1
                pen.clear()
                pen.write("Score:{} High Score:{}".format(score,highest_score),align="center",font=("candara",24,"bold"))
                time.sleep(delay)
win.mainloop()

        




