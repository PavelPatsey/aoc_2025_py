from math import prod


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [line.split() for line in data]


def calculate(nums: list, op: str) -> int:
    if op == "+":
        return sum(nums)
    return prod(nums)


def get_answer(grid):
    rows = len(grid)
    cols = len(grid[0])
    res = 0
    for c in range(cols):
        nums = []
        for r in range(rows):
            char = grid[r][c]
            if char in {"+", "*"}:
                res += calculate(nums, char)
            else:
                nums.append(int(char))
    return res


def main():
    file = "input.txt"
    data = get_data(file)
    print(get_answer(data))


if __name__ == "__main__":
    main()
