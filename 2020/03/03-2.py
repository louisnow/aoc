import os

script_dir = os.path.dirname(__file__)


def get_coords_function(right, down):
    def get_coords(x, y):
        return x + down, y + right

    return get_coords


def solve(data):
    height = len(data)
    width = len(data[0])
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    res = 1
    for down, right in slopes:
        count = 0
        get_coords = get_coords_function(down, right)
        x, y = get_coords(0, 0)
        while x < height:
            if data[x][y % width] == "#":
                count += 1
            x, y = get_coords(x, y)
        res *= count
    return res


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    inp = reader.read().split("\n")
    print(solve(inp))
