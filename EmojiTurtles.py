import turtle
Andy = turtle.Turtle()
Andy.shape("turtle")
Andy.fillcolor("Old Lace")
Andy.penup()
Andy.goto(0,300)
Andy.pendown()
Andy.pensize(5)
Milly = turtle.Turtle()
Milly.shape("turtle")
Milly.color("blue")
Milly.fillcolor("Black")
Milly.left(90)
Milly.pensize(25)
Milly.pendown()
Billy = turtle.Turtle()
Billy.shape("turtle")
Billy.color("Red")
Billy.penup()
Billy.goto(225,250)
Billy.pendown()
Billy.pensize(7)
Roger = turtle.Turtle()
Roger.shape("turtle")
Roger.color("Red")
Roger.penup()
Roger.goto(-225,250)
Roger.pendown()
Roger.pensize(10)
Andy.shape("turtle")
Milly.shape("turtle")
Billy.shape("turtle")
Roger.shape("turtle")
Andy.speed(900)
Milly.speed(5)
Billy.speed(900)
Roger.speed(900)

def Hair():
    for i in range(20):
        Roger.begin_fill()
        Roger.circle(i*2)
        Roger.right(70)
        Roger.forward(10)
        Roger.end_fill()
def Hair2():
    for i in range(20):
        Billy.begin_fill()
        Billy.circle(i*2)
        Billy.right(70)
        Billy.forward(10)
        Billy.end_fill()
def EyesandMouth():
    for i in range(1):
        Milly.penup()
        Milly.goto(150, 90)
        Milly.pendown()
        Milly.begin_fill()
        Milly.circle(30)
        Milly.end_fill()
        Milly.penup()
        Milly.goto(-130, 90)
        Milly.pendown()
        Milly.begin_fill()
        Milly.circle(30)
        Milly.end_fill()
        Milly.penup()
        Milly.goto(10,-20)
        Milly.pendown()
        Milly.color("red")
        Milly.fillcolor("red")
        Milly.begin_fill()
        Milly.circle(30)
        Milly.end_fill()
        Milly.penup()
        Milly.goto(50,-150)
        Milly.pendown()
        Milly.left(180)
        for x in range(180):
            Milly.forward(1)
            Milly.right(1)
        Milly.right(90)
        Milly.forward(115)
        Milly.penup()
        Milly.goto(190,-20)
        Milly.pendown()
        Milly.begin_fill()
        Milly.circle(30)
        Milly.end_fill()
        Milly.penup()
        Milly.goto(-200, -20)
        Milly.pendown()
        Milly.begin_fill()
        Milly.circle(30)
        Milly.end_fill()



Andy.begin_fill()
Andy.circle(-300)
Andy.end_fill()
Hair()
Hair2()
EyesandMouth()


turtle.exitonclick()