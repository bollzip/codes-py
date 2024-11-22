import turtle

screen = turtle.screen()
screen.bgcolor ("white")
t = turtle.Turtle()
t.setup (500, 500)

t.penup()
t.goto(-200, 100)
t.pendown()
for i in range (3):
    t.forward (100)
    t.left (120)

t.penup()
t.goto(50,100)
t.pendown()
for i in range (4):
    t.forward (100)
    t.left (90)

t.penup()
t.goto (200, 0)
t.pendown()
t.circle(50)

t.hiderturtle()
screen.mainloop()
t.done()