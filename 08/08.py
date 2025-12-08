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


def get_answer(n, points, distances):
    l = len(points)
    ds_points = set()
    for i, j in product(range(l), range(l)):
        if i != j:
            point = frozenset({i, j})
            d = distances[i][j]
            ds_points.add((d, point))
    print(ds_points)
    sorted_ds_points = sorted(ds_points)
    print(sorted_ds_points)

    graph = defaultdict(set)
    for k in range(n):
        _d, indxs = sorted_ds_points[k]
        i, j = indxs
        graph[i].add(j)
        graph[j].add(i)
    print(graph)

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
    print(f"{groups=}")
    lens = sorted(map(lambda x: len(x), groups), reverse=True)
    print(f"{lens=}")
    print(f"{lens[:3]=}")
    return prod(lens[:3])


def main():
    file = "input.txt"
    n = 10 if file == "test_input.txt" else 1000
    points = get_data(file)
    distances = calculate_distances(points)
    print(get_answer(n, points, distances))


if __name__ == "__main__":
    main()
