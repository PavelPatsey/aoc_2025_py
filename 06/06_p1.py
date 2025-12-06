from functools import reduce
from math import prod


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [
        [int(x) if x not in {"*", "+"} else x for x in line.split()] for line in data
    ]


def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


def get_answer(grid):
    rows = len(grid)
    cols = len(grid[0])
    res = 0
    for row in grid:
        print(row)
        if row[-1] == "+":
            # a = sum(row[: rows - 1])
            numbers = [x for x in row if isinstance(x, int)]
            a = sum(numbers)
            res += a
        else:

            # b = reduce(lambda acc, x: acc * x, row[: rows - 1], 1)
            numbers = [x for x in row if isinstance(x, int)]
            b = reduce(lambda acc, x: acc * x, numbers, 1)
            res += b
    return res


def main():
    file = "input.txt"
    data = get_data(file)
    print(data)
    grid = transpose(data)
    print(grid)
    print(get_answer(grid))


if __name__ == "__main__":
    main()
