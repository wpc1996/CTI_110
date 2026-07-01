# William Littlefield
# July 1 2026
# P4LAB1
# Looping while using a for and while loop to make a house

# Import the turtle module
import turtle

# Create the window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()
turtle.Screen().bgcolor("black")

#Turtle options
pen.pensize (3)
pen.pencolor("teal")
pen.shape ("turtle")


# Code to draw square
for side in range(4):
    pen.forward(200)
    pen.right(90)

# Code to draw triangle
side = 3
while side > 0:
    pen.forward(200)
    pen.left(120)
    side = side - 1




# Wait for user to close window
win.mainloop()

