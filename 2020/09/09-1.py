import os

script_dir = os.path.dirname(__file__)


def isValid(num, preamble, preamble_map):
    for n in preamble:
        if n <= num:
            to_find_num = num - n
            if to_find_num in preamble_map:
                return True


def solve(numbers, preamble_length=25):
    index = preamble_length
    preamble = numbers[0:preamble_length]
    preamble_map = {n: True for n in preamble}
    while index < len(numbers):
        num = numbers[index]
        if not isValid(num, preamble, preamble_map):
            return num
        del preamble_map[preamble.pop(0)]
        preamble.append(num)
        preamble_map[num] = True
        index += 1


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    numbers = [int(x) for x in reader.read().splitlines()]
    print(solve(numbers))
