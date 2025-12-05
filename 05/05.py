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


def get_answer(ranges, nums):
    sorted_ranges = sorted(ranges)
    sorted_nums = sorted(nums)
    counter = 0
    for n in sorted_nums:
        for a, b in sorted_ranges:
            if a <= n <= b:
                counter += 1
                break
    return counter


def main():
    file = "input.txt"
    ranges, nums = get_data(file)
    print(get_answer(ranges, nums))


if __name__ == "__main__":
    main()
