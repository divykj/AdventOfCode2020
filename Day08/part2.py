import sys


def parse_insruction(instruction, current_i, acc):
    if instruction[0] == "acc":
        return current_i + 1, acc + instruction[1]

    if instruction[0] == "jmp":
        return current_i + instruction[1], acc

    return current_i + 1, acc


def run_loop(instructions):
    acc = 0
    current_i = 0
    visited = set()
    jumps = []
    noops = []

    while True:
        visited.add(current_i)
        current_instruction = instructions[current_i]
        if current_instruction[0] == "jmp":
            jumps.append(current_i)
        elif current_instruction[0] == "nop":
            noops.append(current_i)
        current_i, acc = parse_insruction(current_instruction, current_i, acc)

        if current_i == len(instructions):
            return True, acc

        if current_i in visited:
            return False, jumps, noops


def find_correct_acc_out(instructions):
    _, jumps, noops = run_loop(instructions)

    for jump in jumps:
        new_instructions = instructions[:]
        new_instructions[jump] = ("nop", instructions[jump][1])
        successful, *result = run_loop(new_instructions)
        if successful:
            return "JUMP", jump, result[0]

    for noop in noops:
        new_instructions = instructions[:]
        new_instructions[noop] = ("jmp", instructions[noop][1])
        successful, *result = run_loop(new_instructions)
        if successful:
            return "NOOP", noop, result[0]


def main():
    with open(sys.argv[1], "r") as input_file:
        instructions = []
        for instruction in input_file:
            intruction_parts = instruction.split(" ")
            instruction = intruction_parts[0].lower()
            value = int(intruction_parts[1])
            instructions.append((instruction, value))

        print(find_correct_acc_out(instructions))


if __name__ == "__main__":
    main()
