from copy import deepcopy
from itertools import product


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[x for x in line] for line in data]


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def get_answer(grid):
    grid = deepcopy(grid)
    rows = len(grid)
    cols = len(grid[0])
    grid[1][grid[0].index("S")] = "|"
    res = 0
    for r, c in product(range(2, rows), range(cols)):
        if grid[r][c] == "^" and grid[r - 1][c] == "|":
            for dr, dc in [(0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if in_grid(nr, nc, grid) and grid[nr][nc] != "^":
                    grid[nr][nc] = "|"
            res += 1
        if grid[r][c] == "." and grid[r - 1][c] == "|":
            grid[r][c] = "|"
    return res


def get_answer_2(grid):
    rows = len(grid)
    cols = len(grid[0])
    sr, sc = 0, grid[0].index("S")
    weights = [[0 for _ in range(cols)] for _ in range(rows)]
    weights[sr + 1][sc] = 1

    for r, c in product(range(2, rows), range(cols)):
        if grid[r][c] == "^":
            for dr, dc in [(0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if in_grid(nr, nc, grid):
                    weights[nr][nc] += weights[r - 1][c]
        else:
            weights[r][c] += weights[r - 1][c]
    return sum(weights[-1])


def main():
    file = "input.txt"
    grid = get_data(file)
    print(get_answer(grid))
    print(get_answer_2(grid))


if __name__ == "__main__":
    main()
