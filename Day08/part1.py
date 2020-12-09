import sys


def parse_insruction(instructions, current_i, acc):
    current_instruction = instructions[current_i]

    if current_instruction[0] == "acc":
        return current_i + 1, acc + current_instruction[1]
    if current_instruction[0] == "jmp":
        return current_i + current_instruction[1], acc

    return current_i + 1, acc


def find_loop_acc(instructions):
    acc = 0
    current_i = 0
    visited = set()

    while True:
        visited.add(current_i)
        current_i, acc = parse_insruction(instructions, current_i, acc)

        if current_i in visited:
            return acc


def main():
    with open(sys.argv[1], "r") as input_file:
        instructions = []
        for instruction in input_file:
            intruction_parts = instruction.split(" ")
            instruction = intruction_parts[0].lower()
            value = int(intruction_parts[1])
            instructions.append((instruction, value))

        print(find_loop_acc(instructions))


if __name__ == "__main__":
    main()
