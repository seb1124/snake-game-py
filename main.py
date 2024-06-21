from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# initializing and setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    # does not trace animation


snake = Snake()     # initialize snake object
food = Food()       # initialize food object
scoreboard = Scoreboard()       # initialize scoreboard object


# key input functions
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True   # boolean used in while loop
screen.update()     # refreshes screen to display snake body


while game_is_on:       # while game is running:
    screen.update()     # update screen every iteration
    time.sleep(0.1)     # delay for 0.1 seconds

    snake.move()        # snake moves

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:  # uses list slicing to make for loop start at 2nd element of list so that the head does not need to be skipped
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
