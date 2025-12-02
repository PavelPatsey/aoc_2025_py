from itertools import chain

from utils import timer


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip()
    return [tuple((int(y) for y in x.split("-"))) for x in data.split(",")]


def is_invalid(n: int) -> bool:
    s = str(n)
    if s.startswith("0"):
        return False
    length = len(s)
    if length % 2 != 0:
        return False
    return s[0 : length // 2] == s[length // 2 :]


@timer
def get_answer(data):
    res = 0
    for start, end in data:
        for i in range(start, end + 1):
            if is_invalid(i):
                res += i
    return res


def is_invalid_2(n: int) -> bool:
    s = str(n)
    if s.startswith("0"):
        return False
    length = len(s)
    for i in range(2, length + 1):
        if length % i != 0:
            continue
        a = s[0 : length // i]
        if a * i == s:
            return True
    return False


@timer
def get_answer_2(data):
    res = 0
    for start, end in data:
        for i in range(start, end + 1):
            if is_invalid_2(i):
                res += i
    return res


@timer
def get_answer_2_func(data):
    mapped = map(lambda x: range(x[0], x[1] + 1), data)
    chained = chain.from_iterable(mapped)
    filtered = filter(is_invalid_2, chained)
    return sum(filtered)


def generate_invalid_nums(max_num: int) -> set[int]:
    invalid_nums = set()
    for i in range(2, len(str(max_num)) + 1):
        j = 1
        n = int(str(j) * i)
        while n <= max_num:
            invalid_nums.add(n)
            j += 1
            n = int(str(j) * i)
    return invalid_nums


@timer
def get_answer_2_fast(data):
    ranges = sorted(data)
    max_end = ranges[-1][-1]
    invalid_nums = generate_invalid_nums(max_end)
    nums = sorted(invalid_nums)

    total = 0
    for n in nums:
        for left, right in ranges:
            if left <= n <= right:
                total += n
                break
    return total


def main():
    file = "input.txt"
    data = get_data(file)
    print(get_answer(data))
    print(get_answer_2(data))
    print(get_answer_2_func(data))
    print(get_answer_2_fast(data))


def test():
    assert is_invalid(11) == True
    assert is_invalid(22) == True
    assert is_invalid(1188511885) == True
    assert is_invalid(1010) == True

    assert is_invalid(123) == False
    assert is_invalid(12) == False
    assert is_invalid(100) == False
    assert is_invalid(101) == False

    assert is_invalid_2(11) == True
    assert is_invalid_2(22) == True
    assert is_invalid_2(2121212121) == True
    assert is_invalid_2(999) == True
    assert is_invalid_2(1010) == True
    assert is_invalid_2(1188511885) == True

    assert is_invalid_2(1726462) == False


if __name__ == "__main__":
    test()
    main()
