### Basic Pong game using Python (by Carlo Alamani)
### Version 1.0 started 25 July 2021
    ## Version 1.0 (July 25, 2021)
        # basic framework of the game pong using turtle module; mainly following the guide of https://www.youtube.com/watch?v=XGf2GcyHPhc with minor modifications to aesthetics and code
        # includes basic mechanics in paddle-ball collision, screen borders, bouncing, sound effects, and keyboard functionality
    ## Version 1.1 (July 25, 2021)
        # changed screen design to look like official ping pong tabletops
        # simplified counter to only show number
        # changed x-cor of each paddles to be farther back
    ## Version 1.2 (July 26, 2021)
        # modified ball.dx to speed up a bit after every scored point



import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Carlo Alamani")
wn.bgcolor("#2741b3")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

## Table Designs

top = turtle.Turtle()
top.speed(0)                                   
top.shape("square")
top.shapesize(stretch_wid=.5, stretch_len=40)
top.color("white")           
top.penup()                    
top.goto(0,295)

bottom = turtle.Turtle()
bottom.speed(0)                                   
bottom.shape("square")
bottom.shapesize(stretch_wid=.5, stretch_len=40)
bottom.color("white")           
bottom.penup()                    
bottom.goto(0,-295)

left = turtle.Turtle()
left.speed(0)                                   
left.shape("square")
left.shapesize(stretch_wid=30, stretch_len=.5)
left.color("white")           
left.penup()                    
left.goto(-395,0)

right = turtle.Turtle()
right.speed(0)                                   
right.shape("square")
right.shapesize(stretch_wid=30, stretch_len=.5)
right.color("white")           
right.penup()                    
right.goto(395,0)

center = turtle.Turtle()
center.speed(0)                                   
center.shape("square")
center.shapesize(stretch_wid=30, stretch_len=.5)
center.color("white")           
center.penup()                    
center.goto(0,0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)                                   # sets the speed of the paddle to maximum
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("red")
paddle_a.penup()                                    # disables writing line over movement path
paddle_a.goto(-370,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)                                   
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("black")
paddle_b.penup()                                   
paddle_b.goto(370,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)                                   
ball.shape("circle")
ball.color("orange")
ball.penup()                                    
ball.goto(0,0)
ball.dx = 0.3                                    # change in x and y direction is +-0.3px
ball.dy = -0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,245)
pen.write(" 0    0", align = "center", font = ("Impact", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()                        # assigning variable 'y' to y coordinate of paddle a
    y += 20                                    # adds 20 to y coordinate per iteration
    paddle_a.sety(y)                           # sets y of paddle to new y coordinate

def paddle_a_down():
    y = paddle_a.ycor()                        # assigning variable 'y' to y coordinate of paddle a
    y -= 20                                    # subtract 20 to y coordinate per iteration
    paddle_a.sety(y)                           # sets y of paddle to new y coordinate

def paddle_b_up():
    y = paddle_b.ycor()                        # assigning variable 'y' to y coordinate of paddle a
    y += 20                                    # adds 20 to y coordinate per iteration
    paddle_b.sety(y)                           # sets y of paddle to new y coordinate

def paddle_b_down():
    y = paddle_b.ycor()                        # assigning variable 'y' to y coordinate of paddle a
    y -= 20                                    # subtract 10 to y coordinate per iteration
    paddle_b.sety(y)                           # sets y of paddle to new y coordinate


# Keyboard binds
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)            # moves the ball in x direction (loop)
    ball.sety(ball.ycor() + ball.dy)            # moves the ball in y direction (loop)

    # Border checking
    if ball.ycor() > 290:                       # if ball touches the screen border, it reverses
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)          # if ball touches the top and bottom walls, wall.wav will play 
    
    if ball.ycor() < -290:                       
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("wall.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 410:                       # if ball goes out the side, it goes back to center
        ball.goto(0,0)
        ball.dx *= -1.03                           # once it returns to center, it reverses
        score_a += 1
        pen.clear()
        pen.write(" {}    {}".format(score_a, score_b), align = "center", font = ("Impact", 24, "normal"))      # score counter
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)                                                     # if ball goes out of bounds, point.wav will play

    if ball.xcor() < -410:
        ball.goto(0,0)
        ball.dx *= -1.03
        score_b += 1
        pen.clear()
        pen.write(" {}    {}".format(score_a, score_b), align = "center", font = ("Impact", 24, "normal"))
        winsound.PlaySound("point.wav", winsound.SND_ASYNC)
    
    # Collisions
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(360)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)                                                                           # if ball collides with paddle, paddle.wav will play
    
    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-360)
        ball.dx *= -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)