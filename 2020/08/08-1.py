import os

script_dir = os.path.dirname(__file__)


def get_instruction(ins):
    x, y = ins.split()
    return x, int(y)


def solve(instructions):
    operation = {}
    line = 0
    max_len = len(instructions)
    acc = 0
    while line not in operation and line >= 0 and line < max_len:
        ins = instructions[line]
        operation[line] = True
        operator, value = get_instruction(ins)
        if operator == "nop":
            line += 1
        elif operator == "acc":
            acc += value
            line += 1
        elif operator == "jmp":
            line += value

    return acc


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    instructions = reader.read().splitlines()
    print(solve(instructions))
