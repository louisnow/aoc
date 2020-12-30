import os

script_dir = os.path.dirname(__file__)


def move(pos, angle, instruction):
    DIR_OP = {0: "E", 90: "S", 180: "W", 270: "N"}
    operation, value = instruction
    x, y = pos
    if operation == "L":
        angle = (angle - value) % 360
    elif operation == "R":
        angle = (angle + value) % 360

    if operation == "F":
        operation = DIR_OP[angle]

    if operation == "N":
        y += value
    elif operation == "S":
        y -= value
    elif operation == "E":
        x += value
    elif operation == "W":
        x -= value

    return [x, y], angle


def solve(instructions):
    angle = 0
    pos = [0, 0]

    for instruction in instructions:
        pos, angle = move(pos, angle, instruction)

    return abs(pos[0]) + abs(pos[1])


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    instructions = [[l[0], int(l[1:])] for l in reader.read().splitlines()]
    print(solve(instructions))
