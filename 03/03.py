def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [int(line) for line in data]


def find_max_joltage(n: int, length: int) -> int:
    res = 0
    digits = [int(char) for char in str(n)]
    left = 0
    right = len(digits) - length
    while right < len(digits):
        max_tuple = left, digits[left]
        for i in range(left + 1, right + 1):
            if digits[i] > digits[max_tuple[0]]:
                max_tuple = i, digits[i]
        res = res * 10 + max_tuple[1]
        right += 1
        left = max_tuple[0] + 1
    return res


def main():
    file = "input.txt"
    data = get_data(file)
    ans1, ans2 = 0, 0
    for n in data:
        ans1 += find_max_joltage(n, 2)
        ans2 += find_max_joltage(n, 12)
    print(ans1, ans2, sep="\n")


def test():
    assert find_max_joltage(987654321111111, 2) == 98
    assert find_max_joltage(811111111111119, 2) == 89
    assert find_max_joltage(234234234234278, 2) == 78
    assert find_max_joltage(818181911112111, 2) == 92

    assert find_max_joltage(987654321111111, 12) == 987654321111
    assert find_max_joltage(811111111111119, 12) == 811111111119
    assert find_max_joltage(234234234234278, 12) == 434234234278
    assert find_max_joltage(818181911112111, 12) == 888911112111


if __name__ == "__main__":
    test()
    main()
