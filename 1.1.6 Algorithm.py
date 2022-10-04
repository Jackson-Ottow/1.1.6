#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
#create a spider body
spider.speed(-1)
spider.pensize(40)
spider.circle(20)
#configure legs
legs = 8
circle_length = 120
circle_arc = 100
leg_angle = 140 / legs
spider.pensize(5)
remaining = 4
#draw legs
while (remaining < legs):
  spider.penup()
  spider.goto(0,20)
  spider.pendown()
  spider.setheading(leg_angle*remaining)
  spider.circle(circle_arc,circle_length)
  remaining = remaining + 1
remaining = 4
circle_length= -100
while (remaining < legs):
  spider.penup()
  spider.goto(0,20)
  spider.pendown()
  spider.setheading(leg_angle*remaining-270)
  spider.circle(circle_arc,circle_length)
  remaining = remaining + 1

spider.penup()
spider.goto(6,45)
spider.pensize(2)
spider.pendown()
spider.setheading(320)
eyes = 8
eye_size=3
space=10
spider.pencolor("red")
remain=4
while (remain < eyes):
  spider.pendown()
  spider.begin_fill()
  spider.fillcolor("white")
  spider.circle(eye_size)
  spider.end_fill()
  spider.penup()
  spider.forward(space)
  remain = remain + 1 
remain=4
spider.goto(0,37)
while (remain < eyes):
  spider.pendown()
  spider.begin_fill()
  spider.fillcolor("white")
  spider.circle(eye_size)
  spider.end_fill()
  spider.penup()
  spider.forward(space)
  remain = remain + 1 


spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()