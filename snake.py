from turtle import Turtle
import time

# constants
X_POS = [0]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # create_snake func (creates the initial snake using add_segment func)
    def create_snake(self):
        for position in range(0, 3):
            self.add_segment()

    # move function
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):  # for loop changes pos of every segment to pos of one in front of it
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # change direction functions
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # add segment function (adds a segment to snake)
    def add_segment(self):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.setpos(X_POS[0], 0)
        X_POS[0] -= 20
        self.segments.append(segment)

    # extend function (extends snake using add_segment func)
    def extend(self):
        self.add_segment()

