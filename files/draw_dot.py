from turtle import *
import random

from draw_triangle import triangle_points, size


def draw_dot(first_run):
    if first_run:
        random_x = random.randint(triangle_points[0][0], triangle_points[1][0])
        random_y = random.randint(triangle_points[0][1], round(triangle_points[2][1]))

        while not is_inside(triangle_points[0][0], triangle_points[0][1],
                            triangle_points[1][0], triangle_points[1][1],
                            triangle_points[2][0], triangle_points[2][1],
                            random_x, random_y):
            random_x = random.randint(triangle_points[0][0], triangle_points[1][0])
            random_y = random.randint(triangle_points[0][1], round(triangle_points[2][1]))

        setposition(random_x, random_y)
        dot()

    draw_dot_halfway()


def draw_dot_halfway():
    random_index = random.randint(0, len(triangle_points) - 1)
    triangle_dot = triangle_points[random_index]

    x = 0
    y = 0

    # point 1 - bottom left
    if random_index == 0:
        x = triangle_dot[0] - ((triangle_dot[0] - (pos()[0])) / 2)
        y = triangle_dot[1] - ((triangle_dot[1] - (pos()[1])) / 2)

    # point 2 - bottom right
    elif random_index == 1:
        x = pos()[0] + (((pos()[0] - triangle_dot[0]) * -1) / 2)
        y = pos()[1] - (((triangle_dot[1] * -1) + pos()[1]) / 2)

    # point 3 - top
    elif random_index == 2:
        x = pos()[0] / 2
        y = (pos()[1] + triangle_dot[1]) / 2

    setposition(x, y)
    dot()


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


def is_inside(x1, y1, x2, y2, x3, y3, x, y):
    # Calculate area of triangle ABC
    a = area(x1, y1, x2, y2, x3, y3)

    # Calculate area of triangle PBC
    a1 = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PAC
    a2 = area(x1, y1, x, y, x3, y3)

    # Calculate area of triangle PAB
    a3 = area(x1, y1, x2, y2, x, y)

    # Check if sum of A1, A2 and A3
    # is same as A
    return a == a1 + a2 + a3
