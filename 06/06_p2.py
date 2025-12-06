from math import prod
from functools import reduce


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


def prepare_grid(data):
    max_len = 0
    for line in data:
        max_len = max(max_len, len(line))
    new_data = []
    for line in data:
        new_line = []
        for char in line:
            if char == " ":
                new_line.append("p")
            else:
                new_line.append(char)
        dx = max_len - len(new_line)
        new_line += ["p"] * dx
        new_data.append(new_line)

    # print("new_data")
    # for x in new_data:
    #     print(x)

    grid = transpose(new_data)
    # print("grid")
    # for x in grid:
    #     print(x)
    return grid


def calculate(group):
    """
    ['1', 'p', 'p', '*']
    ['2', '4', 'p', 'p']
    ['3', '5', '6', 'p']
    """

    op = group[0][-1]
    nums = []
    for line in group:
        digits = [s for s in line if s.isdigit()]
        n = int("".join(digits))
        nums.append(n)
    print(f"{nums=}")
    if op == "+":
        return sum(nums)
    return reduce(lambda acc, x: acc * x, nums, 1)


def get_answer(grid):
    groups = []
    new_group = []
    for row in grid:
        if set(row) == {"p"}:
            groups.append(new_group)
            new_group = []
        else:
            new_group.append(row)
    groups.append(new_group)

    res = 0
    for g in groups:
        a = calculate(g)
        print(f"{a=}")
        res += a

    return res


def main():
    file = "input.txt"
    data = get_data(file)
    grid = prepare_grid(data)
    print(get_answer(grid))


if __name__ == "__main__":
    main()
