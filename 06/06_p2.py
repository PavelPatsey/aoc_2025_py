from functools import reduce


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def prepare_grid(data):
    max_len = 0
    for line in data:
        max_len = max(max_len, len(line))
    grid = []
    for row in data:
        new_row = list(row)
        new_row += [" "] * (max_len - len(new_row))
        grid.append(new_row)
    return grid


def calculate(nums: list, op: str) -> int:
    if op == "+":
        return sum(nums)
    return reduce(lambda acc, x: acc * x, nums, 1)


def get_answer(grid):
    res = 0
    rows = len(grid)
    cols = len(grid[0])
    nums = []
    for c in reversed(range(cols)):
        column = []
        for r in range(rows):
            column.append(grid[r][c])
        if set(column) == {" "}:
            nums = []
        elif column[-1] in {"+", "*"}:
            op = column[-1]
            n = int("".join([ch for ch in column if ch.isdigit()]))
            nums.append(n)
            res += calculate(nums, op)
        else:
            n = int("".join(column))
            nums.append(n)
    return res


def main():
    file = "input.txt"
    data = get_data(file)
    grid = prepare_grid(data)
    print(get_answer(grid))


if __name__ == "__main__":
    main()
