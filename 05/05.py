def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    ranges = []
    nums = []
    for line in data:
        if "-" in line:
            a, b = map(int, line.split("-"))
            ranges.append((a, b))
        elif line:
            nums.append(int(line))
        else:
            pass
    return ranges, nums


def get_answer(data):
    return


def main():
    file = "test_input.txt"
    ranges, nums = get_data(file)
    print(ranges)
    print(nums)
    # print(get_answer(data))


if __name__ == "__main__":
    main()
