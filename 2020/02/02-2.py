import os

script_dir = os.path.dirname(__file__)


def solve(line):
    data = line.split(" ")
    lo, hi = [int(x) for x in data[0].split("-")]
    letter = data[1][0]
    password = data[2]
    return (
        password[lo - 1] == letter
        and password[hi - 1] != letter
        or (password[lo - 1] != letter and password[hi - 1] == letter)
    )


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    inp = reader.read().split("\n")
    p = 0
    for line in inp:
        if solve(line):
            p += 1
    print(p)
