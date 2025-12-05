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


def normalize(merged: list) -> list:
    if len(merged) < 2:
        return merged
    while len(merged) >= 2:
        a1, b1 = merged.pop()
        a2, b2 = merged.pop()
        if a1 <= b2:
            min_a = min(a1, a2)
            max_b = max(b1, b2)
            merged.append((min_a, max_b))
        else:
            merged.append((a2, b2))
            merged.append((a1, b1))
            break
    return merged


def get_answer_2(ranges):
    ranges = sorted(ranges, key=itemgetter(1))
    print(ranges)
    merged = []
    for a, b in ranges:
        merged.append((a, b))
        merged = normalize(merged)
    print(merged)

    res = 0
    for a, b in merged:
        res += b - a + 1
    return res


def main():
    file = "input.txt"
    ranges, nums = get_data(file)
    print(get_answer(ranges, nums))
    print(get_answer_2(ranges))


if __name__ == "__main__":
    main()
