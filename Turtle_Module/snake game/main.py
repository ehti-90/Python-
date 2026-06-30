from turtle import Turtle, Screen
from snake import Snake
from food import Food
import random
import time



screen = Screen()

screen.bgcolor("black")
screen.setup(800,800)
screen.tracer(0)    # off the automatic screen update: if instead of 0 theer was 10 it would have been--
screen.title("Snake Game")  # updated after 10 turtle movement

snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

# tim.shape("square")
# tim.shapesize(1,1)
    # tim.shearfactor(-0.5)     # slants the shape
    # print(tim.shapetransform())
    # (tim.tiltangle(45)) # as name suggest

# pos = 0
# all_turtles = []
    
game_on = True

while game_on:
    
    screen.update() #   after the ops in loop is made update now
    time.sleep(0.1) # add o.2 sec delay after screen update
    
    # for seg in range(len(all_turtles) - 1, 0, -1):   # start at lastend at 0 and take -1 steps at atime
    #     new_x = all_turtles[seg - 1].xcor()
    #     new_y = all_turtles[seg - 1].ycor()
    #     all_turtles[seg].setposition(new_x, new_y)
    
    # all_turtles[0].forward(20)  # we made the logic in loop such that only doing anything--
    # all_turtles[0].left(40)     # to the first object the restt follows the first
    snake.move()
    
    if snake.head.distance(food) < 15:  # this .distance check distance between snake ob and food object
        food.new_location()              # when they get this close the  food must goto another rand place


screen.mainloop()