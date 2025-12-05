from operator import itemgetter


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


def merge(ranges: list) -> list:
    if len(ranges) < 2:
        return ranges
    is_merged = False
    while not is_merged and len(ranges) >= 2:
        a1, b1 = ranges[-1]
        a2, b2 = ranges[-2]
        if a1 <= b2:
            ranges.pop()
            ranges[-1] = min(a1, a2), b1
        else:
            is_merged = True
    return ranges


def get_answer_2(ranges):
    sorted_ranges = sorted(ranges, key=itemgetter(1))
    merged = []
    for a, b in sorted_ranges:
        merged.append((a, b))
        merged = merge(merged)
    return sum(map(lambda x: x[1] - x[0] + 1, merged))


def main():
    file = "input.txt"
    ranges, nums = get_data(file)
    print(get_answer(ranges, nums))
    print(get_answer_2(ranges))


if __name__ == "__main__":
    main()
