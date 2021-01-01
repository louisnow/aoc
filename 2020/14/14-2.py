import os
import re
from typing import List, Dict

script_dir = os.path.dirname(__file__)


def get_masked_address(mask: str, address: int) -> str:
    address_mask = "{:0{}b}".format(address, len(mask))
    or_mask = []
    for i in range(len(mask)):
        m = mask[i]
        a = address_mask[i]
        if m == "X" or m == "0":
            or_mask.append(a)
        else:
            or_mask.append("1")
    return "".join(or_mask)


def apply_address(memory: Dict[int, int], mask: str, address: int, value: int) -> None:
    floating_positions = []
    max_combination_binary = ""
    for index, m in enumerate(list(mask)):
        if m != "X":
            continue
        max_combination_binary += "1"
        floating_positions.append(index)

    address_mask = get_masked_address(mask, address)
    max_combinations = int(max_combination_binary, 2) + 1

    for combination in range(0, max_combinations):
        combination_binary = "{:0{}b}".format(combination, len(max_combination_binary))
        new_mask = list(address_mask)
        for index, c in enumerate(combination_binary):
            x_index = floating_positions[index]
            new_mask[x_index] = c

        new_address = int("".join(new_mask), 2)
        memory[new_address] = value


def solve(lines: List[str]) -> int:
    memory: Dict[int, int] = {}
    mask = "0"
    for line in lines:
        if line.startswith("mask"):
            match = re.match("mask\s=\s([X10]*)", line)
            if not match:
                raise ValueError("Invalid mask")
            mask = match.group(1)
        else:
            match = re.match("mem\[([\d]*)\]\s=\s([\d]*)", line)
            if not match:
                raise ValueError("Invalid memory address")
            apply_address(memory, mask, int(match.group(1)), int(match.group(2)))
    return sum(memory.values())


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    lines = reader.read().splitlines()
    print(solve(lines))
