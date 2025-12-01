import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        dt = end - start
        print(f"'{func.__name__}': {dt:.6f} sec")
        return result

    return wrapper


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


@timer
def get_answer_2_naive(data):
    x = 50
    res = 0
    for command in data:
        if command[0] == "L":
            sign = -1
        else:
            sign = 1
        for i in range(command[1]):
            x = x + sign
            x = x % 100
            if x == 0:
                res += 1
    return res


@timer
def get_answer_2_fast(data):
    x = 50
    res = 0
    for direction, value in data:
        div = value // 100
        mod = value % 100
        res += div
        sign = -1 if direction == "L" else 1
        new_x = x + sign * mod
        if x != 0 and (new_x <= 0 or new_x >= 100):
            res += 1
        x = new_x % 100
    return res


def main():
    file = "input.txt"
    data = get_data(file)
    print(get_answer(data))
    ans2_naive = get_answer_2_naive(data)
    ans2_fast = get_answer_2_fast(data)
    assert ans2_fast == ans2_naive
    print(ans2_fast)


if __name__ == "__main__":
    main()
