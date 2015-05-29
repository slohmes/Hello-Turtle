# drawing out a hello world with the python turtle library!

import turtle

wn = turtle.Screen()
h = turtle.Turtle()
r = 30 # radius value: use to easily adjust word size


# TODO make it so it will run through a string and draw it out


# all drawLetter functions need to start and end facing right.


# function to move to next letter
def nextLetter():
	h.penup()
	h.forward(r)
	h.pendown()


def drawH():
	h.left(90)
	h.forward(2*r)
	h.forward(-1*r)
	h.right(90)
	h.forward(r)
	h.right(90)
	h.forward(r)
	h.left(90)
	nextLetter()


def drawE():
	h.penup()
	h.left(90)
	h.forward(r/2)
	h.right(90)
	h.pendown()
	
	h.forward(r)
	h.left(90)
	h.forward(r/2)
	h.left(90)
	h.forward(r)
	h.left(90)
	h.forward(r)
	h.left(90)
	h.forward(r)
	nextLetter()


def drawL():
	h.left(90)
	h.forward(2*r)
	h.forward(-2*r)
	h.right(90)
	nextLetter()


def drawO():
	i=0
	while i<=4:
		h.forward(r)
		h.left(90)
		i+=1
	h.right(90)
	nextLetter()


def drawW():
	h.penup()
	h.left(90)
	h.forward(r)
	h.left(180)
	h.pendown()
	
	h.forward(r)
	h.left(90)
	h.forward(r)
	h.left(90)
	h.forward(r)
	h.forward(-1*r)
	h.right(90)
	h.forward(r)
	h.left(90)
	h.forward(r)
	h.forward(-1*r)
	h.right(90)	
	nextLetter()


def drawR():
	h.left(90)
	h.forward(r)
	h.right(90)
	h.forward(r)
	
	h.penup()
	h.right(90)
	h.forward(r)
	h.left(90)
	nextLetter()

def drawD():
	h.penup()
	h.forward(r)
	h.left(90)
	h.forward(r)
	h.left(90)
	h.pendown()
	
	i = 1
	while i<4:
		h.forward(r)
		h.left(90)
		i+=1
	h.forward(2*r)
	h.forward(-2*r)
	h.right(90)
	nextLetter()






# main

h.penup()
h.forward(-270) # get the turtle to the right start place!
h.pendown()

drawH()
drawE()
drawL()
drawL()
drawO()
nextLetter()
drawW()
drawO()
drawR()
drawL()
drawD()

wn.exitonclick()