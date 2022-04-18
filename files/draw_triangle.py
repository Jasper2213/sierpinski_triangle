from turtle import *

size = 1000
triangle_points = []


def draw_triangle():
    dot()
    triangle_points.append(pos())
    forward(size)
    dot()
    triangle_points.append(pos())
    left(120)
    forward(size)
    dot()
    triangle_points.append(pos())
