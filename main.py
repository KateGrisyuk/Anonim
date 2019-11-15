#Case1

import turtle
def square(x,y,size,color,angle,to_angle):
  turtle.penup()
  turtle.goto(x,y)
  turtle.setheading(to_angle)
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.right(angle)
  turtle.pendown()
  for i in range(4):
    turtle.forward(size)
    turtle.right(angle)
  turtle.end_fill()
  return()
  #TODO:(Kate)

def triangle(x,y,size1,size2,color,angle1,angle2,to_angle):
  turtle.penup()
  turtle.goto(x,y)
  turtle.setheading(to_angle)
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.right(angle1)
  turtle.pendown()
  turtle.forward(size1)
  turtle.right(angle2)
  turtle.forward(size1)
  turtle.right(angle1)
  turtle.forward(size2)
  turtle.end_fill()
  return()
  #TODO:(Anna)

def parallelogramm(x,y,size1,size2,color,angle1,angle2,to_angle):
  turtle.penup()
  turtle.goto(x, y)
  turtle.setheading(to_angle)
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

#Picture1 "A wolf"
parallelogramm(-150,110,30,70,'grey',90,90,180)
square(-160,160,23,'grey',90,45)
triangle(-160,160,10,10,'grey',90,135,88)
triangle(-150,155,10,10,'grey',90,135,88)
parallelogramm(-65,160,10,25,'grey',90,90,45)
parallelogramm(-140,80,30,15,'grey',90,90,180)
parallelogramm(-110,80,30,15,'grey',90,90,180)
#TODO:(Kate)

#Picture2 "A ship"
parallelogramm(120,80,80,40,'green',60,120,240)
parallelogramm(60,113,80,40,'green',120,60,120)
parallelogramm(130,135,20,100,'blue',90,90,360)
parallelogramm(100,145,10,40,'red',90,90,360)
turtle.goto(80,145)
turtle.color('black')
turtle.goto(80,165)
triangle(80,165,10,10,'black',90,135,180)
parallelogramm(70,100,10,20,'white',90,90,360)
parallelogramm(110,100,10,20,'white',90,90,360)
#TODO:(Kate)

# Picture3 "A fish"
x0, y0 = (-130, 0)
square(x0, y0, 50, 'lawn green', 90, 45)
square(x0 + 17, y0 - 55, 23, 'deep pink', 90, 45)
parallelogramm(x0 + 50, y0 - 35, 15, 25, 'red', 135, 45, 315)
triangle(x0 + 21, y0 - 21, 30, 30, 'blue', 135, 90, 270)
triangle(x0 + 35, y0 - 35, 15, 15, 'yellow', 135, 90, 135)
triangle(x0 + 65, y0 - 50, 15, 15, 'orange', 135, 90, 315)
#TODO:(Sofya)

# Picture4 "A horse"
x0, y0 = (60, 0)
triangle(x0 , y0 , 31, 31, 'salmon', 135, 90, 180)
square(x0 + 43, y0, 21, 'lawn green', 90, 0)
triangle(x0, y0 - 21 , 43, 43, 'royal blue', 135, 90, 135)
triangle(x0 - 12, y0 - 32, 16, 16, 'maroon', 135, 90, 180)
triangle(x0 + 43, y0 - 21, 43, 43, 'orange', 135, 90, 90)
triangle(x0 + 43, y0 - 70, 16, 16, 'red', 135, 90, 45)
parallelogramm(x0 + 87, y0 - 73, 15, 25, 'yellow', 135, 45, 30)
#TODO:(Sofya)

#Picture5 "A house"
square(-80,-150,50,'brown',90,90)
triangle(-80,-150,38,50,'red',135,90,180)
square(-65,-165,20,'yellow',90,90)
#TODO:(Anna)

#Picture6 "A fox"
triangle(20,-110,13,20,'orange',135,90,90)
triangle(40,-129,13,20,'orange',135,90,270)
square(30,-120,13,'orange',90,45)
triangle(20,-150,29,40,'orange',135,90,180)
triangle(785,-138,23,30,'orange',135,90,360)
triangle(56,-155,32,50,'orange',135,90,180)
square(26,-125,2,'black',90,45)
square(34,-125,2,'black',90,45)
#TODO:(Anna)










