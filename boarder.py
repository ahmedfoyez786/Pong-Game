from turtle import Turtle


class Boarder:
    def __init__(self):
        self.y = -280
        for i in range(14):
            self.line = Turtle()
            self.line.color("white")
            self.line.shape('square')
            self.line.penup()
            self.line.shapesize(stretch_len=.1, stretch_wid=.5)
            self.line.goto(0, self.y)
            self.y += 50
