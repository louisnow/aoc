import os

script_dir = os.path.dirname(__file__)


def solve(data):
    for i, n1 in enumerate(data):
        for j, n2 in enumerate(data):
            if i == j:
                continue
            if n1 + n2 == 2020:
                return n1 * n2


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    inp = [int(x) for x in reader.read().split()]
    print(solve(inp))
