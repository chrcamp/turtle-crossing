from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.at_finish_line = False
        self.reset_position()

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.at_finish_line = False

    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() >= FINISH_LINE_Y:
            self.at_finish_line = True
