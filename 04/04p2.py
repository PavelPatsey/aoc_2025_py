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
        data = file.read().splitlines()
    return [list(line) for line in data]


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


def get_coordinates(grid):
    res = []
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if is_valid(r, c, grid):
                p = r, c
                res.append(p)
    return res


def get_answer(grid):
    points = get_coordinates(grid)
    res = len(points)
    while len(points) > 0:
        for r, c in points:
            grid[r][c] = "."
        points = get_coordinates(grid)
        res += len(points)
    return res


def main():
    file = "input.txt"
    data = get_data(file)
    print(get_answer(data))


if __name__ == "__main__":
    main()
