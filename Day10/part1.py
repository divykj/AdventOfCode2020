import sys


def find_adapter_sequence(adapters):
    bag = set(adapters)
    current_joltage = 0
    one_jolts = 0
    three_jolts = 0

    max_joltage = max(bag)

    while current_joltage != max_joltage:
        for i in range(1, 4):
            if (current_joltage + i) in bag:
                current_joltage += i
                if i == 1:
                    one_jolts += 1
                elif i == 3:
                    three_jolts += 1
                break

    return one_jolts * (three_jolts + 1)


def main():
    with open(sys.argv[1], "r") as input_file:
        adapters = [int(line.strip()) for line in input_file]

        print(find_adapter_sequence(adapters))


if __name__ == "__main__":
    main()
