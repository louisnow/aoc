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


def get_seat_id(seat):
    row = decode(seat[:7], 0, 127)
    col = decode(seat[-3:], 0, 7)
    return (row * 8) + col


def solve(data):
    """
    Arguably faster but with twice the memory
    """
    seats = []
    low = None
    for d in data:
        seat_id = get_seat_id(d)
        seats.append(seat_id)
        if low is None or seat_id < low:
            low = seat_id

    sorted_seats = [None for x in range(len(seats) + 1)]
    for seat in seats:
        sorted_seats[seat - low] = seat
    for index, seat in enumerate(sorted_seats):
        if seat is None:
            return index + low


def solve_readably(data):
    seats = []
    for d in data:
        seats.append(get_seat_id(d))

    sorted_seats = sorted(seats)

    for index, seat in enumerate(sorted_seats):
        if index == 0:
            continue
        if sorted_seats[index - 1] != seat - 1:
            return seat - 1


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    seats = reader.read().split()
    print(solve_readably(seats))
