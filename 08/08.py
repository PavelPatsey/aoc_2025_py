import heapq
from copy import copy
from itertools import combinations
from math import prod

from utils import timer


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[int(x) for x in line.split(",")] for line in data]


@timer
def make_ds_points_heap(points):
    l = len(points)
    heap = []
    visited = set()
    for i, j in combinations(range(l), 2):
        point = frozenset({i, j})
        if i != j and point not in visited:
            x1, y1, z1 = points[i]
            x2, y2, z2 = points[j]
            d = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
            heapq.heappush(heap, (d, i, j))
            visited.add(point)
    return heap


def union(circuits: list[set], i, j) -> None:
    circ_with_i = None
    circ_with_j = None
    for circ in circuits:
        if i in circ:
            circ_with_i = circ
        if j in circ:
            circ_with_j = circ
    if circ_with_i is None and circ_with_j is None:
        circuits.append({i, j})
    elif circ_with_i and circ_with_j:
        if circ_with_i != circ_with_j:
            circuits.remove(circ_with_j)
            circ_with_i.update(circ_with_j)
    elif circ_with_i:
        circ_with_i.add(j)
    elif circ_with_j:
        circ_with_j.add(i)
    else:
        assert False, "error case!"


@timer
def get_answer(n, heap):
    heap = copy(heap)
    circuits = []
    for _ in range(n):
        _, i, j = heapq.heappop(heap)
        union(circuits, i, j)
    lens = sorted(map(lambda x: len(x), circuits), reverse=True)
    return prod(lens[:3])


@timer
def get_answer_2(points, heap):
    heap = copy(heap)
    max_len = -1
    circuits = []
    while max_len < len(points):
        _, i, j = heapq.heappop(heap)
        union(circuits, i, j)
        max_len = max(map(lambda x: len(x), circuits))
    return points[i][0] * points[j][0]


def main():
    file = "input.txt"
    n = 10 if file == "test_input.txt" else 1000
    points = get_data(file)
    heap = make_ds_points_heap(points)
    print(get_answer(n, heap))
    print(get_answer_2(points, heap))


if __name__ == "__main__":
    main()
