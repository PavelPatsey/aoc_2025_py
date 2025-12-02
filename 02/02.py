def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    return [tuple((int(y) for y in x.split("-"))) for x in data.split(",")]


def find_invalid_ids(n: int) -> list[int]:
    pass


def get_answer(data):
    res = 0
    for start, end in data:
        for i in range(start, end + 1):
            invalid_ids = find_invalid_ids(i)
            res += invalid_ids
    return res


def main():
    file = "test_input.txt"
    data = get_data(file)
    print(data)
    print(get_answer(data))


if __name__ == "__main__":
    main()
