def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [(line[0], int(line[1:])) for line in data]


def get_answer(data):
    x = 50
    res = 0
    for command in data:
        if command[0] == "L":
            x = (x - command[1]) % 100
        else:
            x = (x + command[1]) % 100
        if x == 0:
            res += 1
    return res


def get_answer_2(data):
    x = 50
    res = 0
    div = 0
    for command in data:
        if command[0] == "L":
            x = x - command[1]
        else:
            x = x + command[1]
        new_div = x // 100
        res += abs(new_div - div)
        x = x % 100
        div = x // 100
        # print(x, div)
    return res


def main():
    file = "test_input.txt"
    data = get_data(file)
    print(data)
    # print(get_answer(data))
    print(get_answer_2(data))


if __name__ == "__main__":
    main()
