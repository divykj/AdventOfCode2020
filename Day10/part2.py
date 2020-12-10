import sys


def find_distinct_adapter_sequences(adapters):
    bag = set(adapters)

    max_joltage = max(bag)
    my_adapter_joltage = max_joltage + 3
    bag.add(my_adapter_joltage)

    dp = {}

    dp[1] = int(1 in bag)
    dp[2] = int(2 in bag) * (1 + dp[1])
    dp[3] = int(3 in bag) * (1 + dp[1] + dp[2])

    for i in range(4, my_adapter_joltage + 1):
        dp[i] = int(i in bag) * (dp[i - 1] + dp[i - 2] + dp[i - 3])

    return dp[my_adapter_joltage]


def main():
    with open(sys.argv[1], "r") as input_file:
        adapters = [int(line.strip()) for line in input_file]

        print(find_distinct_adapter_sequences(adapters))


if __name__ == "__main__":
    main()
