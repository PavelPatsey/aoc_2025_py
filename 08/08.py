from collections import defaultdict, deque
from itertools import product
from math import prod, sqrt


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return [[int(x) for x in line.split(",")] for line in data]


def calculate_distances(points):
    l = len(points)
    distances = [[0 for _ in range(l)] for _ in range(l)]
    for i, j in product(range(l), range(l)):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        distances[i][j] = d
        distances[j][i] = d
    return distances


def get_sorted_ds_points(points, distances):
    l = len(points)
    ds_points = set()
    for i, j in product(range(l), range(l)):
        if i != j:
            point = frozenset({i, j})
            d = distances[i][j]
            ds_points.add((d, point))
    return sorted(ds_points)


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


def get_answer(n, points):
    distances = calculate_distances(points)
    sorted_ds_points = get_sorted_ds_points(points, distances)
    graph = make_graph(n, sorted_ds_points)
    groups = make_groups(graph)
    lens = sorted(map(lambda x: len(x), groups), reverse=True)
    return prod(lens[:3])


def get_answer_2(points):
    distances = calculate_distances(points)
    sorted_ds_points = get_sorted_ds_points(points, distances)
    max_len = -1
    n = 0
    groups = []
    while max_len < len(points):
        _d, indxs = sorted_ds_points[n]
        i, j = indxs

        found_i = set()
        found_j = set()
        for gr in groups:
            if i in gr:
                found_i = gr
            if j in gr:
                found_j = gr
        if not found_i and not found_j:
            groups.append({i, j})
        elif found_i and found_j:
            if found_i == found_j:
                groups.remove(found_i)
            else:
                groups.remove(found_i)
                groups.remove(found_j)
            groups.append(found_i | found_j)
        elif found_i:
            groups.remove(found_i)
            groups.append(found_i | {j})
        elif found_j:
            groups.remove(found_j)
            groups.append(found_j | {i})
        else:
            assert False, "error case!"
        lens = list(map(lambda x: len(x), groups))
        max_len = max(lens)
        n += 1
    return points[i][0] * points[j][0]


def main():
    file = "input.txt"
    n = 10 if file == "test_input.txt" else 1000
    points = get_data(file)
    print(get_answer(n, points))
    print(get_answer_2(points))


if __name__ == "__main__":
    main()
