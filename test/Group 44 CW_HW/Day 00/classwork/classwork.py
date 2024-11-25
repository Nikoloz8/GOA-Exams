from turtle import * 

#we want to paint a house

#step 1: draw a square
speed(99)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

#drawing a first window

penup()
goto(10, 70)
pendown()

color("blue")

left(120)
forward(50)

left(90)
forward(80)

left(90)
forward(50)

left(90)
forward(80)

penup()
goto(35, 70)
pendown()

right(180)
forward(80)

penup()
goto(10, 110)
pendown()

right(90)
forward(50)

#drawing a second window

penup()
goto(140, 70)
pendown()

left(90)
forward(80)

right(90)
forward(50)

right(90)
forward(80)

right(90)
forward(50)

penup()
goto(165, 70)
pendown()

right(90)
forward(80)

penup()
goto(140, 110)
pendown()

right(90)
forward(50)

exitonclick()