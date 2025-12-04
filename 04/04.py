from itertools import product

DIRS8 = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def get_data(input_file):
    with open(input_file, "r") as file:
        return [list(line) for line in file.read().splitlines()]


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def is_valid(r, c, grid) -> bool:
    if grid[r][c] == ".":
        return False
    count = 0
    for dr, dc in DIRS8:
        if in_grid(r + dr, c + dc, grid) and grid[r + dr][c + dc] == "@":
            count += 1
    return count < 4


def get_answer(grid):
    res = 0
    rows = len(grid)
    cols = len(grid[0])
    for r, c in product(range(rows), range(cols)):
        if is_valid(r, c, grid):
            res += 1
    return res


def find_valid_points(grid):
    points = []
    rows = len(grid)
    cols = len(grid[0])
    for r, c in product(range(rows), range(cols)):
        if is_valid(r, c, grid):
            points.append((r, c))
    return points


def get_answer_2(grid):
    points = find_valid_points(grid)
    res = 0
    while len(points) > 0:
        res += len(points)
        for r, c in points:
            grid[r][c] = "."
        points = find_valid_points(grid)
    return res


def main():
    file = "input.txt"
    data = get_data(file)
    print(get_answer(data))
    print(get_answer_2(data))


if __name__ == "__main__":
    main()
