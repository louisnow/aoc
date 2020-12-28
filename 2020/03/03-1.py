import os

script_dir = os.path.dirname(__file__)


def get_coords(x, y):
    return x + 1, y + 3


def solve(data):
    height = len(data)
    width = len(data[0])
    x, y = get_coords(0, 0)
    count = 0
    while x < height:
        if data[x][y % width] == "#":
            count += 1
        x, y = get_coords(x, y)
    return count


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    inp = reader.read().split("\n")
    print(solve(inp))
