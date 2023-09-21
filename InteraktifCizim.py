import turtle

arayuz = turtle.Screen()
arayuz.bgcolor("light blue")
arayuz.title("Python Turtle")
imlec = turtle.Turtle()

def turtle_forward():
    imlec.forward(100)

def rotate_angle_right():
    imlec.setheading(imlec.heading()-100)

def rotate_angle_left():
    imlec.setheading(imlec.heading()+100)

def clear_screen():
    imlec.clear()

def turtle_pen_up():
    imlec.penup()

def turtle_pen_down():
    imlec.pendown()

def merkezeDonme():
    imlec.home()

arayuz.listen()
arayuz.onkey(key="space",fun=turtle_forward)
arayuz.onkey(key="Down",fun=rotate_angle_right)
arayuz.onkey(key="Up",fun=rotate_angle_left)
arayuz.onkey(key="c",fun=clear_screen)
arayuz.onkey(key="q",fun=turtle_pen_up)
arayuz.onkey(key="w",fun=turtle_pen_down)
arayuz.onkey(key="h",fun=merkezeDonme)

arayuz.exitonclick()
#turtle.done()