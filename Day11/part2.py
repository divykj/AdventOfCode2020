import sys
from copy import deepcopy

neighbour_deltas = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def get_neighbours(layout, x, y):
    max_x = len(layout[0]) - 1
    max_y = len(layout) - 1
    for dx, dy in neighbour_deltas:
        neighbour_state = "."
        n_x, n_y = x, y
        while neighbour_state == ".":
            n_x += dx
            n_y += dy
            if not 0 <= n_x <= max_x or not 0 <= n_y <= max_y:
                break
            neighbour_state = layout[n_y][n_x]
        else:
            yield neighbour_state


def get_next_state(layout, x, y):
    neighbours = list(get_neighbours(layout, x, y))

    current_state = layout[y][x]

    if current_state == ".":
        return "."

    if all(neighbour != "#" for neighbour in neighbours):
        return "#"

    if sum(neighbour == "#" for neighbour in neighbours) > 4:
        return "L"

    return current_state


def game_of_seats(layout):
    prev_layout = []
    while "".join(layout) != "".join(prev_layout):
        prev_layout = deepcopy(layout)
        layout = [
            "".join(get_next_state(layout, x, y) for x in range(len(layout[0])))
            for y in range(len(layout))
        ]

    return sum(seat == "#" for seat in "".join(layout))


def main():
    with open(sys.argv[1], "r") as input_file:
        layout = [line.strip() for line in input_file]

        print(game_of_seats(layout))


if __name__ == "__main__":
    main()
