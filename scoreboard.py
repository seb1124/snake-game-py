from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
GAME_OVER_FONT = ("Courier", 35, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0      # score displayed on scoreboard
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 280)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1             # increment score
        self.clear()                # clear writing from screen
        self.setpos(0, 280)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
