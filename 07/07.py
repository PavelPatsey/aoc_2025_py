from itertools import product

DIRS = [(0, -1), (0, 1)]


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[x for x in line] for line in data]


def in_grid(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= r < rows and 0 <= c < cols


def get_answer(grid):
    rows = len(grid)
    cols = len(grid[0])
    start = 0, grid[0].index("S")
    grid[1][start[1]] = "|"

    res = 0
    for r, c in product(range(2, rows), range(cols)):
        if grid[r][c] == "^" and grid[r - 1][c] == "|":
            split = False
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if in_grid(nr, nc, grid) and grid[nr][nc] != "^":
                    grid[nr][nc] = "|"
                    split = True
            if split:
                res += 1
        if grid[r][c] == "." and grid[r - 1][c] == "|":
            grid[r][c] = "|"
    return res


def main():
    file = "input.txt"
    grid = get_data(file)
    print(get_answer(grid))


if __name__ == "__main__":
    main()
