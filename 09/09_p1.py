from itertools import combinations


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [tuple([int(x) for x in line.split(",")]) for line in data]


def get_answer(points):
    res = -1
    for p1, p2 in combinations(points, 2):
        x1, y1 = p1
        x2, y2 = p2
        s = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        res = max(res, s)
    return res


def main():
    file = "input.txt"
    points = get_data(file)
    print(get_answer(points))


if __name__ == "__main__":
    main()
