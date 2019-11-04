#Case1

import turtle
def square(x,y,size,color,angle,to_angle):
  turtle.penup()
  turtle.goto(x,y)
  turtle.setheading(to_angle)
  turtle.color(color)
  turtle.begin_fill()
  turtle.right(angle)
  turtle.pendown()
  for i in range(4):
    turtle.forward(size)
    turtle.right(angle)
  turtle.end_fill()
  return()
  #TODO:(Kate)
def triangular(x,y,size1,size2,color,angle1,angle2,to_angle):
  turtle.penup()
  turtle.goto(x,y)
  turtle.setheading(to_angle1)
  turtle.color(color)
  turtle.begin_fill()
  turtle.right(angle1)
  turtle.pendown()
  turtle.forward(size1)
  turtle.right(angle1)
  turtle.forward(size2)
  turtle.right(angle1)
  turtle.forward(size2)
  turtle.right(angle2)
  turtle.end_fill()
  return()
  #TODO:(Anna)

def parallelogramm(x,y,size1,size2,color,angle1,angle2,to_angle):
  turtle.penup()
  turtle.goto(x, y)
  turtle.setheading(to_angle1)
  turtle.color(color)
  turtle.begin_fill()
  turtle.right(angle1)
  turtle.pendown()
  for i in range(2):
    turtle.forward(size1)
    turtle.right(angle1)
    turtle.forward(size2)
    turtle.right(angle2)
  turtle.end_fill()
  return()
  #TODO:(Sofya)





