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



update()
