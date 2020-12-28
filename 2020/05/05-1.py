import os
import math

script_dir = os.path.dirname(__file__)


def decode(code, low, hi):
    for c in code:
        value = -1
        if c == "F" or c == "L":
            hi = math.floor((low + hi) / 2)
            value = hi
        else:
            low = math.ceil((low + hi) / 2)
            value = low
    return value


def solve(seat):
    row = decode(seat[:7], 0, 127)
    col = decode(seat[-3:], 0, 7)
    return (row * 8) + col


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    seats = reader.read().split()
    highest = 0
    for seat in seats:
        seat_id = solve(seat)
        if seat_id > highest:
            highest = seat_id
    print(highest)
