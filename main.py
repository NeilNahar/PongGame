from turtle import Screen
from divider import Divider
from scoreboard import SocreBoard
from slider import Slider
from ball import Ball
import time

s=Screen()
s.bgcolor("black")
s.title("Pong Game")
s.setup(1200,700)
game_on=True

s.tracer(0)
divider_1=Divider()

score_board=SocreBoard()

slider_1=Slider(-500,280)
slider_2=Slider(500,280)

ball_1=Ball()

def slider1_down():
    slider_1.move_down()
def slider1_up():
    slider_1.move_up()

def slider2_down():
    slider_2.move_down()
def slider2_up():
    slider_2.move_up()

while game_on:
    s.update()

    time.sleep(ball_1.ball_speed)
    ball_1.move()

    if ball_1.pos()[1]>335:
       ball_1.bounce1()
    elif ball_1.pos()[1]<-335:
        ball_1.bounce2()

    if abs(slider_1.xcor()-ball_1.xcor())<15 and abs(slider_1.ycor()-ball_1.ycor())<=55:
        ball_1.bounce3()
    elif abs(ball_1.xcor()-slider_2.xcor())<15 and abs(slider_2.ycor()-ball_1.ycor())<=55:
        ball_1.bounce4()
       
    print(ball_1.ball_speed)
    
    if ball_1.xcor()>=600:
        score_board.score1+=1
        score_board.initializescore1()
        score_board.initializescore2()
        if ball_1.ball_speed>=0.01:
            ball_1.ball_speed-=0.01
        ball_1.ball_start()
    elif ball_1.xcor()<=-600:
        score_board.score2+=1
        score_board.initializescore1()
        score_board.initializescore2()
        ball_1.ball_start()
        if ball_1.ball_speed>=0.01:
            ball_1.ball_speed-=0.01
    
    if score_board.score1==11 or score_board.score2==11:
        score_board.gameover()
        game_on=False

    s.listen()
    s.onkey(slider1_down,"s")
    s.onkey(slider1_up,"w")
    s.onkey(slider2_down,"Down")
    s.onkey(slider2_up,"Up")
    
s.exitonclick()