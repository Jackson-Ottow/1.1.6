#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
legs = 6
leg_length = 90
leg_angle = 140 / legs
ladybug.pensize(5)
remaining = 3
#draw legs
while (remaining < legs):
  ladybug.goto(0,-30)
  ladybug.setheading(leg_angle*remaining-90)
  ladybug.forward(leg_length)
  remaining = remaining + 1
remaining = 3

while (remaining < legs):
  ladybug.goto(0,-30)
  ladybug.setheading(leg_angle*remaining-270)
  ladybug.forward(leg_length)
  remaining = remaining + 1
# and body
ladybug.penup()
ladybug.setheading(0)
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1



ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()