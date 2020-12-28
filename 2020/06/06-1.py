import os
import math

script_dir = os.path.dirname(__file__)


def solve(group):
    people = group.split()
    ans_map = {}
    count = 0
    for person in people:
        for ans in person:
            if ans not in ans_map:
                count += 1
                ans_map[ans] = True
    return count


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    groups = reader.read().split("\n\n")
    total_count = 0
    for group in groups:
        count = solve(group)
        total_count += count
    print(total_count)
