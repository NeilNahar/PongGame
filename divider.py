from turtle import Turtle
import time

class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.divderlist=[]
        self.initialize()

    
    def initialize(self):
        for i in range(335,-340,-30):
            t=Turtle()
            t.speed(0)
            t.shape("square")
            t.color("white")
            t.penup()
            t.goto(0,i)
            t.shapesize(1,0.3)
            self.divderlist.append(t)
        