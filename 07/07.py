from itertools import product
from functools import lru_cache

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


def get_answer_2(grid):
    rows = len(grid)
    sr, sc = 0, grid[0].index("S")
    res = 0

    # @lru_cache
    def dfs(r, c):
        if r >= rows:
            nonlocal res
            res += 1
            print(r, c)
            return
        if grid[r][c] == ".":
            dfs(r + 1, c)
            return
        if grid[r][c] == "^":
            for dr, dc in [(1, -1), (1, 1)]:
                nr, nc = r + dr, c + dc
                if in_grid(nr, nc, grid):
                    dfs(nr, nc)
        return

    dfs(sr + 1, sc)
    return res


def main():
    file = "test_input.txt"
    grid = get_data(file)
    # print(get_answer(deepcopy(grid)))
    print(get_answer_2(grid))


if __name__ == "__main__":
    main()
