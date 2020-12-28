import os

script_dir = os.path.dirname(__file__)


def solve(numbers):
    n_sorted = sorted(numbers)
    prev = 0
    c1 = 0
    c3 = 1
    for n in n_sorted:
        diff = n - prev
        if diff == 1:
            c1 += 1
        elif diff == 3:
            c3 += 1
        prev = n
    return c1 * c3


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    numbers = [int(x) for x in reader.read().splitlines()]
    print(solve(numbers))
