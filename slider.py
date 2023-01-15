from turtle import Turtle

class Slider(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.speed(0)
        self.setpos(x,y)
        self.x=x
        self.y=y    
    def move_down(self):
        if self.y>=-240:
            self.y-=40
            self.setpos(self.x,self.y)

    def move_up(self):
        if self.y<=240:
            self.y+=40
            self.setpos(self.x,self.y)