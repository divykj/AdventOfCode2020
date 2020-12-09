import sys
from itertools import combinations


def find_pair_sum(sequence, target):
    bag = set(sequence)

    for num1, num2 in combinations(bag, r=2):
        if num1 != num2 and num1 + num2 == target:
            return True

    return False


def find_first_stantdout(sequence, preamble=25):
    for i, current_number in enumerate(sequence[preamble:]):
        if not find_pair_sum(sequence[i : preamble + i], current_number):
            return current_number


def main():
    with open(sys.argv[1], "r") as input_file:
        sequence = [int(line.strip()) for line in input_file]

        print(find_first_stantdout(sequence))


if __name__ == "__main__":
    main()
