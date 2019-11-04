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
def triangular(x,y,size,color,angle):
  #TODO:(Anna)
  pass
def parallelogramm(x,y,size,colot,angle):
  #TODO:(Sofya)
  pass



