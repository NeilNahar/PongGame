from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.ball_speed=0.05
        self.xcordinate=randint(1,15)
        self.ycordinate=randint(1,10)
        print(self.xcordinate, self.ycordinate)
        self.setpos(0,0)

    def move(self):
        self.newxcordinate=self.pos()[0]+self.xcordinate
        self.newycordinate=self.pos()[1]+self.ycordinate

        self.goto(self.newxcordinate,self.newycordinate)
    
    def bounce1(self):
        self.ycordinate=-randint(0,15)
    def bounce2(self):
        self.ycordinate=randint(0,10)
    def bounce3(self):
        self.xcordinate=randint(0,10)
    def bounce4(self):
        self.xcordinate=-randint(0,10)

    def ball_start(self):
        self.xcordinate=randint(-15,15)
        self.ycordinate=randint(-10,10)
        self.newxcordinate=0
        self.newycordinate=0
        self.setpos(0,0)
