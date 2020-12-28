import os

script_dir = os.path.dirname(__file__)


def get_instruction(ins):
    x, y = ins.split()
    return x, int(y)


def run_program(instructions, operation={}, acc=0, line=0):
    max_len = len(instructions)
    stack = []
    while line not in operation and line >= 0 and line < max_len:
        operator, value = instructions[line]
        operation[line] = True
        stack.append(line)
        if operator == "nop":
            line += 1
        elif operator == "acc":
            acc += value
            line += 1
        elif operator == "jmp":
            line += value
    return stack, operation, acc, line


def solve(instructions):
    max_len = len(instructions)
    stack, operation, acc, line = run_program(instructions)

    while True:
        while len(stack) > 0:
            line = stack.pop()
            operator, value = instructions[line]
            if line in operation:
                del operation[line]
            if operator == "acc":
                acc -= value
                line -= 1
            elif operator == "nop":
                instructions[line][0] = "jmp"
                break
            elif operator == "jmp":
                instructions[line][0] = "nop"
                break

        _, _, new_acc, new_line = run_program(instructions, {**operation}, acc, line)

        if new_line >= 0 and new_line < max_len:
            instructions[line][0] = operator
        else:
            return new_acc


with open(os.path.join(script_dir, "in.txt"), "r") as reader:
    instructions = [[*(get_instruction(ins))] for ins in reader.read().splitlines()]
    print(solve(instructions))
