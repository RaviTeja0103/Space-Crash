import turtle as tu
import random
st=0

#screen
ws=tu.Screen()
ws.tracer(4)
tu.title("Space Crash")
ws.setup(width=800,height=800)
ws.bgpic("bg.gif")
ws.register_shape("a.gif")
ws.register_shape("s.gif")

#border
ol=tu.Turtle()
ol.speed(0)
ol.penup()
ol.setposition(-350,-350)
ol.pendown()
for i in range(4):
    ol.forward(700)
    ol.left(90)
ol.hideturtle()

#Ame
ame=[]
for i in range(7):
    ame.append(tu.Turtle())
    ame[i].penup()
    ame[i].speed(0)
    ame[i].shape("a.gif")
    a=random.randint(-190,190)
    b=random.randint(-190,190)
    ame[i].right(random.randint(0,360))
    ame[i].setposition(a,b)
    
#player
t=tu.Turtle()
t.color("black")
t.shape("s.gif")
t.pensize(6)
t.speed(0)
t.penup()

flag=0
scr=0

def turnl():
    t.settiltangle(180)
    t.setheading(180)
def turnr():
    t.settiltangle(0)
    t.setheading(0)
def turnu():
    t.settiltangle(90)
    t.setheading(90)
def turnd():
    t.settiltangle(270)
    t.setheading(270)
def stop():
    if(st==0):
        st=1
    else:
        st=0

#score
ol.penup()
ol.setposition(-340,350)
ol.hideturtle()
ol.write("Scroe:",False,align="left",font=("Arial",14,"normal"))

tu.listen()
tu.onkey(turnl,"Left")
tu.onkey(turnr,"Right")
tu.onkey(turnu,"Up")
tu.onkey(turnd,"Down")
tu.onkey(stop,"space")

while True:
    t.forward(1+scr/10000)

    scr +=1
    
    ol.setposition(-280,350)
    ol.write(scr,False,align="left",font=("Arial",14,"normal"))
    ol.undo()
    
    if t.xcor()>350 or t.xcor()<-350 or t.ycor()>350 or t.ycor()<-350:
        t.left(180)
    for i in range(7):
        ame[i].forward(1+scr/10000)
        if ame[i].xcor()>340 or ame[i].xcor()<-340 or ame[i].ycor()>340 or ame[i].ycor()<-340:
            ame[i].right(60)
        if t.xcor()<=ame[i].xcor()+10 and t.xcor()>=ame[i].xcor()-10 and t.ycor()<=ame[i].ycor()+10 and t.ycor()>=ame[i].ycor()-10:
            flag=1
            break
    if flag==1:
        break

hs=open("hscore.txt","r")
hscr=hs.read()
hscr=int(hscr)
hs.close()
if scr>hscr:
    hscr=scr
    hs=open("hscore.txt","w")
    hs.write(str(scr))
    hs.close()
t.hideturtle()
t.goto(0,0)
t.pencolor("yellow")
t.write("GAME OVER",False,align="center",font=("Arial",40,"bold"))
t.goto(0,-40)
t.write("Ur Score:"+str(scr),False,align="center",font=("Arial",30,"bold"))
t.goto(0,-80)
t.write("High Score:"+str(hscr),False,align="center",font=("Arial",30,"bold"))
ws.mainloop()

