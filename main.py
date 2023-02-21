from turtle import Turtle,Screen


tim=Turtle()
screen=Screen()
tim.shape("turtle")
def clear():
    tim.setposition(0,0)
    tim.clear()
def turn_right():
    angle=tim.heading()
    tim.setheading(angle-10)
def turn_left():
    angle=tim.heading()
    tim.setheading(angle+10)
def go_forword():
    tim.forward(10)
def go_backword():
    tim.backward(10)
def draw_squar():
    for _ in range(0,4):
        tim.forward(100)
        tim.left(90.0)
def draw_circle():
    tim.circle(100)
def close_window():
    screen.bye()


screen.onkeypress(go_forword,"Up")
screen.onkeypress(turn_left,"Left")
screen.onkeypress(turn_right,"Right")
screen.onkeypress(go_backword,"Down")
screen.onkeypress(draw_squar,"s")
screen.onkeypress(tim.penup,"u")
screen.onkeypress(draw_circle,"c")
screen.onkeypress(clear,"x")
screen.onkeypress(tim.pendown,"d")
screen.onkeypress(close_window,"q")
screen.listen()




screen.exitonclick()