from itertools import combinations


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [tuple([int(x) for x in line.split(",")]) for line in data]


def calc_area(p1, p2) -> int:
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def is_horizontal(edge) -> bool:
    p1, p2 = edge
    x1, y1 = p1
    x2, y2 = p2
    return y1 == y2


def is_vertical(edge) -> bool:
    p1, p2 = edge
    x1, y1 = p1
    x2, y2 = p2
    return x1 == x2


def is_intersects(edge1: tuple, edge2: tuple) -> bool:
    set1 = set(edge1)
    set2 = set(edge2)
    if set1.intersection(set2):
        return False
    if is_horizontal(edge1) == is_horizontal(edge2):
        return False

    if is_horizontal(edge1):
        assert is_vertical(edge2)
        h = edge1
        v = edge2
    else:
        assert is_vertical(edge1)
        h = edge2
        v = edge1

    ph1, ph2 = h
    xh1, yh = ph1
    xh2, _ = ph2

    pv1, pv2 = v
    xv, yv1 = pv1
    _, yv2 = pv2

    return min(xh1, xh2) <= xv <= max(xh1, xh2) and min(yv1, yv2) <= yh <= max(yv1, yv2)


def is_intersect_with_edges(edge, edges) -> bool:
    for e in edges:
        if is_intersects(e, edge):
            return True
    return False


def horizontal_ray_intersects_edge(point, edge):
    if is_horizontal(edge):
        return False
    x, y = point
    p1, p2 = edge
    x1, y1 = p1
    x2, y2 = p2
    return min(y1, y2) < y < max(y1, y2) and x1 > x


def point_in_area(point, edges):
    counter = 0
    for edge in edges:
        if horizontal_ray_intersects_edge(point, edge):
            counter += 1
    print(f"{counter=}")
    return counter % 2 == 1


def is_valid_rectangle(p1, p2, edges) -> bool:
    x1, y1 = p1
    x2, y2 = p2

    p1 = x1, y1
    p2 = x2, y1
    p3 = x2, y2
    p4 = x1, y2

    rect_edges = {
        (p1, p2),
        (p2, p3),
        (p3, p4),
        (p4, p1),
    }

    for re in rect_edges:
        if is_intersect_with_edges(re, edges):
            return False

    inner_point = (x2 + x1) / 2, (y2 + y1) / 2
    res = point_in_area(inner_point, edges)
    return res


def get_answer_2(points):
    edges = []
    extended_points = points + [points[0]]
    for p1, p2 in zip(extended_points, extended_points[1:]):
        edges.append((p1, p2))

    res = -1
    for p1, p2 in combinations(points, 2):
        if is_valid_rectangle(p1, p2, edges):
            res = max(res, calc_area(p1, p2))
    return res


def main():
    file = "test_input.txt"
    points = get_data(file)
    print(get_answer_2(points))


def test():
    edge1 = ((7, 1), (7, 11))
    edge2 = ((9, 5), (2, 5))
    assert is_intersects(edge1, edge2)


if __name__ == "__main__":
    test()
    # main()
