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


def main():
    file = "input.txt"
    data = get_data(file)
    print(get_answer(data))


if __name__ == "__main__":
    main()
