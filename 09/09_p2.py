from itertools import combinations

from matplotlib import pyplot
from tqdm import tqdm
from utils import timer


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [tuple([int(x) for x in line.split(",")]) for line in data]


def drow_answer(points, rectangle):
    extended_points = points + [points[0]]
    xs = [p[0] for p in extended_points]
    ys = [p[1] for p in extended_points]
    pyplot.plot(xs, ys, "bo-")

    x1, y1 = rectangle[0]
    x2, y2 = rectangle[1]
    rect_x = [x1, x2, x2, x1, x1]
    rect_y = [y1, y1, y2, y2, y1]
    pyplot.fill(rect_x, rect_y, alpha=0.3, color="red")

    pyplot.axis("equal")
    pyplot.grid()
    pyplot.show()


def calc_area(p1, p2) -> int:
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def is_intersect(edge, diagonal) -> bool:
    d1, d2 = diagonal
    xd1, yd1 = d1
    xd2, yd2 = d2
    p1, p2 = edge
    x1, y1 = p1
    x2, y2 = p2
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    return xd1 < x2 and xd2 > x1 and yd1 < y2 and yd2 > y1


def is_valid_rectangle(p1, p2, edges) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    if y1 == y2 or x1 == x2:
        return False
    d1 = min(x1, x2), min(y1, y2)
    d2 = max(x1, x2), max(y1, y2)
    diagonal = d1, d2
    for edge in edges:
        if is_intersect(edge, diagonal):
            return False
    return True


@timer
def get_answer_2(points):
    edges = []
    extended_points = points + [points[0]]
    for p1, p2 in zip(extended_points, extended_points[1:]):
        edges.append((p1, p2))

    max_area, max_rectangle = -1, ()
    for p1, p2 in tqdm(combinations(points, 2)):
        if is_valid_rectangle(p1, p2, edges):
            area = calc_area(p1, p2)
            if area > max_area:
                max_area = area
                max_rectangle = p1, p2
    return max_area, max_rectangle


def main():
    file = "input.txt"
    points = get_data(file)
    max_area, max_rectangle = get_answer_2(points)
    print(max_area)
    drow_answer(points, max_rectangle)


def test():
    diagonal = ((0, 0), (5, 5))
    edge = ((-2, -2), (-1, -2))
    assert is_intersect(edge, diagonal) == False

    edge = ((2, 2), (-2, 2))
    assert is_intersect(edge, diagonal) == True


if __name__ == "__main__":
    test()
    main()
