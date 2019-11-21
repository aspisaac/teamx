from turtle import *
x = Turtle()
colormode(255)

def reminder():
  # by Mr. Riley
  # don't forget to put a comment with your name at the top of each function you make
  # this will help to keep track of who created each function
  return True
  
def drawRainbow():
    #made by Eric
    x.pendown()
    x.pensize(25)
    x.pencolor("red")
    x.left(90)
    for i in  range (90):
        x.forward(10)
        x.left(2)
    x.penup()
    x.left(90)
    x.forward(25)
    x.pencolor("orange")
    x.pendown()
    x.left(90)
    for i in  range (90):
        x.forward(9)
        x.right(2)
    x.penup()
    x.right(90)
    x.forward(25)
    x.pencolor("yellow")
    x.pendown()
    x.right(90)
    for i in  range (90):
        x.forward(8)
        x.left(2)
    x.penup()
    x.left(90)
    x.forward(25)
    x.pencolor("green")
    x.pendown()
    x.left(90)
    for i in  range (90):
        x.forward(7)
        x.right(2)
    x.penup()
    x.right(90)
    x.forward(25)
    x.pencolor("blue")
    x.pendown()
    x.right(90)
    for i in  range (90):
        x.forward(6)
        x.left(2)
    x.penup()
    x.left(90)
    x.forward(25)
    x.pencolor("purple")
    x.pendown()
    x.left(90)
    for i in  range (90):
        x.forward(5)
        x.right(2)


def drawBus():
  #made by isaac
  x.fillcolor("yellow")
  x.begin_fill()
  for i in range(2):
    x.forward(150)
    x.left(90)
    x.forward(70)
    x.left(90)
  x.end_fill()
  x.fd(20)
  x.fillcolor("silver")
  x.begin_fill()
  for i in range(360):
    x.forward(.3)
    x.right(1)
  x.end_fill()
  x.forward(130)
  x.begin_fill()
  for i in range(360):
    x.forward(.3)
    x.right(1)
  x.end_fill()
  x.fillcolor("yellow")
  x.begin_fill()
  for i in range(4):
    x.forward(30)
    x.left(90)
  x.end_fill()
  x.bk(20)
  x.lt(90)
  x.fillcolor("darkkhaki")
  x.begin_fill()
  for i in range(2):
    x.fd(50)
    x.lt(90)
    x.fd(20)
    x.lt(90)
  x.end_fill()
  x.fd(50)
  x.lt(90)
  x.penup()
  x.fd(40)
  x.pendown()
  x.begin_fill()
  for i in range(4):
    x.fd(20)
    x.left(90)
  x.end_fill()
  x.penup()
  x.fd(50)
  x.pendown()
  x.begin_fill()
  for i in range(4):
    x.fd(20)
    x.left(90)
  x.end_fill()
  x.hideturtle()

def Skyscraper():
    # by Matthew A.
    x.fillcolor('grey')
    x.begin_fill()
    x.forward(100)
    x.left(90)
    x.forward(300)
    x.left(90)
    x.forward(25)
    x.right(90)
    x.forward(35)
    x.left(90)
    x.forward(12.5)
    x.right(80)
    x.forward(75)
    x.left(160)
    x.forward(75)
    x.right(80)
    x.forward(12.5)
    x.left(90)
    x.forward(35)
    x.right(90)
    x.forward(25)
    x.left(90)
    x.forward(300)
    x.left(90)
    x.end_fill()
   
def drawCar():
    #By Caleb
    #outline of car
    x.begin_fill()
    x.fillcolor("red")
    x.forward(275)
    #grill
    for i in range(330):
        x.forward(.1)
        x.left(.5)
    x.forward(50)
    x.right(40)
    x.forward(45)
    x.left(55)
    x.forward(175)
    x.left(55)
    x.forward(35)
    x.right(40)
    x.forward(25)
    x.left(75)
    x.forward(37)
    x.left(90)
    x.forward(10)
    x.forward(35)
    x.right(90)
    x.end_fill()

def drawWheels():
    #left wheel
    x.begin_fill()
    x.fillcolor("black")
    for i in range(720):
        x.forward(.1)
        x.left(.25)
    x.left(90)
    x.forward(45)
    x.left(90)
    for i in range(720):
        x.forward(.1)
        x.left(.25)
    x.end_fill()
    #middle bottom
    x.right(90)
    x.forward(125)
    x.right(90)
    #right wheel
    x.begin_fill()
    x.fillcolor("black")
    for i in range(720):
        x.forward(.1)
        x.left(.25)
    x.end_fill()


update()
