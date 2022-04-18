from turtle import *
import time

from draw_triangle import draw_triangle
from draw_dot import draw_dot

first_run = True

hideturtle()
penup()
speed('fastest')
title("The Chaos Game")
setup(1.0, 1.0)
setposition(-500, -450)
draw_triangle()

time.sleep(1)

while True:
    draw_dot(first_run)
    if first_run:
        first_run = False
