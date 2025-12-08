from collections import defaultdict, deque
from itertools import combinations
from math import prod, sqrt

from utils import timer


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[int(x) for x in line.split(",")] for line in data]


@timer
def calculate_distances(points):
    l = len(points)
    distances = [[0 for _ in range(l)] for _ in range(l)]
    for i, j in combinations(range(l), 2):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        distances[i][j] = d
        distances[j][i] = d
    return distances


@timer
def get_sorted_ds_points(points, distances):
    l = len(points)
    ds_points = set()
    for i, j in combinations(range(l), 2):
        if i != j:
            point = frozenset({i, j})
            d = distances[i][j]
            ds_points.add((d, point))
    return sorted(ds_points)


@timer
def make_ds_points_heap(points):
    pass


def make_graph(n, sorted_ds_points):
    graph = defaultdict(set)
    for k in range(n):
        _d, indxs = sorted_ds_points[k]
        i, j = indxs
        graph[i].add(j)
        graph[j].add(i)
    return graph


def make_groups(graph):
    groups = set()
    for i in graph:
        visited = {i}
        queue = deque([i])
        while queue:
            j = queue.popleft()
            neighbors = graph[j]
            for n in neighbors:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        groups.add(frozenset(visited))
    return groups


@timer
def get_answer(n, sorted_ds_points):
    graph = make_graph(n, sorted_ds_points)
    groups = make_groups(graph)
    lens = sorted(map(lambda x: len(x), groups), reverse=True)
    return prod(lens[:3])


@timer
def get_answer_2(points, sorted_ds_points):
    max_len = -1
    n = 0
    circuits = []
    while max_len < len(points):
        _d, indxs = sorted_ds_points[n]
        i, j = indxs

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
            circuits.remove(circ_with_i)
            circuits.append(circ_with_i | {j})
        elif circ_with_j:
            circuits.remove(circ_with_j)
            circuits.append(circ_with_j | {i})
        else:
            assert False, "error case!"
        max_len = max(map(lambda x: len(x), circuits))
        n += 1
    return points[i][0] * points[j][0]


def main():
    file = "input.txt"
    n = 10 if file == "test_input.txt" else 1000
    points = get_data(file)
    distances = calculate_distances(points)
    sorted_ds_points = get_sorted_ds_points(points, distances)
    print(get_answer(n, sorted_ds_points))
    print(get_answer_2(points, sorted_ds_points))


if __name__ == "__main__":
    main()
