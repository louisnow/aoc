import os
import re
from typing import List, Tuple

script_dir = os.path.dirname(__file__)


def get_masks(mask: str) -> Tuple[int, int]:
    or_mask = ["0" if c == "X" or c == "0" else "1" for c in mask]
    and_mask = ["1" if c == "X" or c == "1" else "0" for c in mask]
    return (int("".join(or_mask), 2), int("".join(and_mask), 2))


def solve(lines: List[str]) -> int:
    memory = {}
    or_mask, and_mask = 0, 1
    for line in lines:
        if line.startswith("mask"):
            match = re.match("mask\s=\s([X10]*)", line)
            if not match:
                raise ValueError("Invalid mask")
            or_mask, and_mask = get_masks(match.group(1))
        else:
            match = re.match("mem\[([\d]*)\]\s=\s([\d]*)", line)
            if not match:
                raise ValueError("Invalid memory address")
            address = int(match.group(1))
            value = int(match.group(2))
            memory[address] = (value | or_mask) & and_mask
    return sum(memory.values())


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    lines = reader.read().splitlines()
    print(solve(lines))
