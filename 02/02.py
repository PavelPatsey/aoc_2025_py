def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    return [tuple((int(y) for y in x.split("-"))) for x in data.split(",")]


def is_invalid(n: int) -> bool:
    s = str(n)
    if s.startswith("0"):
        return False
    n = len(s)
    if n % 2 != 0:
        return False
    a = s[0 : n // 2]
    b = s[n // 2 :]
    return a == b


def get_answer(data):
    res = 0
    for start, end in data:
        for i in range(start, end + 1):
            if is_invalid(i):
                res += i
    return res


def main():
    file = "input.txt"
    data = get_data(file)
    print(get_answer(data))


if __name__ == "__main__":
    main()

    # assert is_invalid(11) == True
    # assert is_invalid(22) == True
    # assert is_invalid(1188511885) == True
    assert is_invalid(1010) == True

    assert is_invalid(123) == False
    assert is_invalid(12) == False
    assert is_invalid(100) == False
    assert is_invalid(101) == False
