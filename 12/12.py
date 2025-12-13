from xmlrpc.client import FastParser


def make_index_size(item: str) -> tuple[int, int]:
    index = int(item.split(":")[0])
    size = sum(map(lambda x: x == "#", item))
    return index, size


def make_region(item: str):
    cs, indexes = item.split(":")
    x, y = [int(x) for x in cs.strip().split("x")]
    quantities = [int(x) for x in indexes.strip().split()]
    return x, y, quantities


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().strip().split("\n\n")
    sizes = dict([make_index_size(x) for x in data[: len(data) - 1]])
    regions = [make_region(x) for x in data[-1].strip().splitlines()]
    return sizes, regions


def get_answer(sizes, regions):
    res = 0
    for x, y, quantities in regions:
        region_area = x * y
        shapes_area = sum([sizes[i] * q for i, q in enumerate(quantities)])
        if shapes_area > region_area:
            continue
        squares_num = (x // 3) * (y // 3)
        shapes_num = sum(quantities)
        if squares_num >= shapes_num:
            res += 1
    return res


def main():
    file = "input.txt"
    sizes, regions = get_data(file)
    print(get_answer(sizes, regions))


if __name__ == "__main__":
    main()
