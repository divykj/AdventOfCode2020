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


def find_first_sum_subsequence(sequence, standout):
    running_sums = []

    for i, number in enumerate(sequence):
        running_sums = [
            (start, running_sum + number)
            for start, running_sum in running_sums
            if running_sum + number <= standout
        ]
        running_sums.append((i, number))

        if start := next(
            (start for start, running_sum in running_sums if running_sum == standout),
            False,
        ):
            return sequence[start : i + 1]


def main():
    with open(sys.argv[1], "r") as input_file:
        sequence = [int(line.strip()) for line in input_file]

        standout = find_first_stantdout(sequence)
        print(standout)
        subsequence = find_first_sum_subsequence(sequence, standout)

        print(min(subsequence) + max(subsequence))


if __name__ == "__main__":
    main()
