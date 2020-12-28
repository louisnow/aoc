import os

script_dir = os.path.dirname(__file__)


def count_adjacent_occupied(area, i, j):
    # clockwise from top
    moves = [
        [i - 1, j],
        [i - 1, j + 1],
        [i, j + 1],
        [i + 1, j + 1],
        [i + 1, j],
        [i + 1, j - 1],
        [i, j - 1],
        [i - 1, j - 1],
    ]
    rows = len(area)
    cols = len(area[0])
    count = 0
    for move in moves:
        r, c = move
        if r >= 0 and r < rows and c >= 0 and c < cols:
            if "#" == area[r][c]:
                count += 1
    return count


def transform(area, bench):
    rows = len(area)
    cols = len(area[0])
    changed = False
    for i in range(rows):
        for j in range(cols):
            value = area[i][j]
            if value == ".":
                continue
            occupied = count_adjacent_occupied(area, i, j)
            if value == "L" and occupied == 0:
                bench[i][j] = "#"
            elif value == "#" and occupied >= 4:
                bench[i][j] = "L"
            else:
                bench[i][j] = value
            if value != bench[i][j]:
                changed = True
    return changed


def count_occupied(arr):
    count = 0
    for row in arr:
        for value in row:
            if value == "#":
                count += 1
    return count


def solve(area):
    rows = len(area)
    cols = len(area[0])
    bench = [["." for c in range(cols)] for r in range(rows)]

    while True:
        changed = transform(area, bench)
        if not changed:
            return count_occupied(area)
        area, bench = bench, area


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    area = [[x for x in l] for l in reader.read().splitlines()]
    print(solve(area))
