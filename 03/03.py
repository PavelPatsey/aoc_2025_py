def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [int(line) for line in data]


def get_max_joltage(n: int) -> int:
    digits = [int(char) for char in str(n)]
    res = 0
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            a = int(digits[i] * 10 + digits[j])
            res = max(res, a)
    return res


def get_answer(data):
    res = 0
    for n in data:
        res += get_max_joltage(n)
    return res


def get_max_joltage_2(n: int) -> int:
    res = []
    digits = [int(char) for char in str(n)]
    left = 0
    right = len(digits) - 12
    while right < len(digits):
        max_tuple = left, digits[left]
        for i in range(left + 1, right + 1):
            if digits[i] > digits[max_tuple[0]]:
                max_tuple = i, digits[i]
        left = max_tuple[0]
        res.append(max_tuple[1])
        right += 1
        left += 1
    return int("".join(str(x) for x in res))


def get_answer_2(data):
    res = 0
    for n in data:
        a = get_max_joltage_2(n)
        res += a
    return res


def main():
    file = "input.txt"
    data = get_data(file)
    print(get_answer(data))
    print(get_answer_2(data))


def test():
    assert get_max_joltage_2(987654321111111) == 987654321111
    assert get_max_joltage_2(811111111111119) == 811111111119
    assert get_max_joltage_2(234234234234278) == 434234234278
    assert get_max_joltage_2(818181911112111) == 888911112111


if __name__ == "__main__":
    test()
    main()
