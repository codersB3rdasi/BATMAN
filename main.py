import turtle

#initialize method
batman = turtle.Turtle()

#size of pointer and pen
batman.turtlesize(2, 2, 2)
batman.pensize(5)

#screen info
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("BATMAN by CodersB3rdasi")

#color
batman.color("yellow", "red")

#begin filling color
batman.begin_fill()

#turn1
batman.left(90)
batman.circle(50, 85)
batman.circle(15, 110)
batman.right(180)

#turn 2
batman.circle(30, 150)
batman.right(5)
batman.forward(10)

#turn 3
batman.right(90)
batman.circle(-70, 140)
batman.forward(40)
batman.right(110)

#turn 4
batman.circle(100, 30)
batman.circle(30, 100)
batman.left(50)
batman.forward(50)
batman.right(145)

#turn5
batman.forward(30)
batman.left(55)
batman.forward(10)

#reverse

#turn 5
batman.forward(10)
batman.left(55)
batman.forward(30)

#turn 4

batman.right(145)
batman.forward(50)
batman.left(50)
batman.circle(30, 100)
batman.circle(100, 30)

#turn 3
batman.right(90)
batman.right(20)
batman.forward(40)
batman.circle(-70, 140)

#turn 2
batman.right(90)
batman.forward(10)
batman.right(5)
batman.circle(30, 150)

#turn 1
batman.left(180)
batman.circle(15, 110)
batman.circle(50, 85)

#end color filling
batman.end_fill()

#write Batman Return
batman.color('white')
batman.penup()
batman.goto(0, 35)
batman.write("BATMAN",
             align='center',
          font='papyrus 35 normal')
batman.goto(0,-75)
batman.write("RETURN",
             align='center',
          font='papyrus 55 normal')
batman.goto(0,-100)
batman.write("By",
             align='center',
        font='papyrus 15 normal')
batman.color('red')
batman.goto(0,-175)
batman.write("CodersB3rdasi",
             align='center',
        font='papyrus 35 normal')

#end the turtle method
turtle.done()
