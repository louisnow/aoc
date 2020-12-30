import os
import math

script_dir = os.path.dirname(__file__)


def move_along_axis(x, y, operation, value):
    if operation == "N":
        y += value
    elif operation == "S":
        y -= value
    elif operation == "E":
        x += value
    elif operation == "W":
        x -= value
    return [x, y]


def rotate(w_pos, angle):
    r_angle = math.radians(angle)
    rotate_matrix = [
        [math.cos(r_angle), -math.sin(r_angle)],
        [math.sin(r_angle), math.cos(r_angle)],
    ]
    x, y = w_pos
    pos_matrix = dot_product(
        rotate_matrix,
        [[x], [y]],
    )
    x = round(pos_matrix[0][0])
    y = round(pos_matrix[1][0])
    return [x, y]


def dot_product(m1, m2):
    if len(m1[0]) != len(m2):
        raise ArithmeticError("Matrix multiplication not possible")
    matrix = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]

    for m in range(len(m1)):
        for n in range(len(m2[0])):
            for index in range(len(m1[0])):
                matrix[m][n] += m1[m][index] * m2[index][n]

    return matrix


def move(s_pos, w_pos, instruction):
    operation, value = instruction
    s_x, s_y = s_pos
    w_x, w_y = w_pos
    if operation == "L":
        w_pos = rotate(w_pos, value)
    elif operation == "R":
        w_pos = rotate(w_pos, -value)
    elif operation == "F":
        s_pos = [s_x + (value * w_x), s_y + (value * w_y)]
    else:
        w_pos = move_along_axis(w_x, w_y, operation, value)

    return s_pos, w_pos


def solve(instructions):
    s_pos = [0, 0]
    w_pos = [10, 1]
    for instruction in instructions:
        s_pos, w_pos = move(s_pos, w_pos, instruction)
    return abs(s_pos[0]) + abs(s_pos[1])


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    instructions = [[l[0], int(l[1:])] for l in reader.read().splitlines()]
    print(solve(instructions))
