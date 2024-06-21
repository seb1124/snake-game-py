from turtle import Turtle
import random


class Food(Turtle):     # food class inherits from turtle class

    def __init__(self):
        super().__init__()      # must call the init of the super() class whenever inheriting from another class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = random.randint(-280, 280)    # setting random x coordinate
        random_y = random.randint(-280, 265)    # setting random y coordinate
        self.goto(random_x, random_y)              # sets position food at random x, y coordinates
        self.refresh()

    # refresh func refreshes position of food to a random location
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 265)
        self.goto(random_x, random_y)
