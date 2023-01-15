from turtle import Turtle
class SocreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score1=0
        self.score2=0
        self.penup()
        self.initializescore1()
        self.initializescore2()

    def initializescore1(self):
        self.setpos(-50,300)
        self.clear()
        self.write(f"{self.score1}", font=('Arial', 30, 'normal'))

    def initializescore2(self):
        self.setpos(30,300)
        self.write(f"{self.score2}", font=('Arial', 30, 'normal'))

    def gameover(self):
        self.color("blue")
        self.setpos(-10,0)
        self.write("Game Over", align="center", font=('Arial', 30, 'normal'))
