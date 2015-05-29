# drawing out a hello world with the python turtle library!
# extension: different modules for each turtle so letter color, etc. can be easily changed.

# TODO: fix angle errors, draw the rest of the letters

import turtle
wn = turtle.Screen()
h = turtle.Turtle()

# move module to the left side of the screen
h.penup()
h.forward(-240)
h.pendown()


# draw the H
h.left(90)
h.forward(120)
h.penup()
h.forward(-60)
h.right(90)
h.pendown()

i = 0
while (i<90):
	h.forward(1)
	h.right(2)
	i+=2

h.right(1)
h.forward(30)


#draw the E

h.penup()
h.left(90)
h.forward(15)
h.left(90)
h.forward(30)
h.right(90)
h.pendown()

h.forward(60)
h.left(90)

i=0
while (i<315):
	h.forward(1)
	h.left(2)
	i+=2



wn.exitonclick()