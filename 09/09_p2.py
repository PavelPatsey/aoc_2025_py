from itertools import combinations
from operator import itemgetter


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [tuple([int(x) for x in line.split(",")]) for line in data]


def show_grid(grid):
    for row in grid:
        print(row)
    print()


def make_grid(points):
    max_col = max(points, key=itemgetter(0))[0]
    max_row = max(points, key=itemgetter(1))[1]
    # print(f"{max_col,max_row=}")
    return [["." for _ in range(max_col + 2)] for _ in range(max_row + 2)]


def make_loop(points, grid):
    extended_points = points + [points[0]]
    for p1, p2 in zip(extended_points, extended_points[1:]):
        c1, r1 = p1
        c2, r2 = p2
        grid[r1][c1] = "#"
        grid[r2][c2] = "#"
        if c1 == c2:
            r1, r2 = sorted([r1, r2])
            for r in range(r1 + 1, r2):
                grid[r][c1] = "X"
        else:
            c1, c2 = sorted([c1, c2])
            for c in range(c1 + 1, c2):
                grid[r1][c] = "X"
    show_grid(grid)


def fill_loop(grid):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        # print(grid[r])
        cs = []
        c = 0
        while c < cols and grid[r][c] == ".":
            c += 1
        if c == cols:
            continue
        while c < cols and grid[r][c] in {"#", "X"}:
            c += 1
        cs.append(c)
        while c < cols and grid[r][c] == ".":
            c += 1
        if c == cols:
            continue
        cs.append(c)
        # print(f"{cs=}")
        c1, c2 = cs
        for nc in range(c1, c2):
            grid[r][nc] = "X"


def get_answer_2(points):
    print(points)
    grid = make_grid(points)
    # show_grid(grid)
    make_loop(points, grid)
    fill_loop(grid)
    show_grid(grid)


def main():
    file = "test_input.txt"
    points = get_data(file)
    print(get_answer_2(points))


if __name__ == "__main__":
    main()
