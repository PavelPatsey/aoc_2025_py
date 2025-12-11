from collections import defaultdict, deque


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    graph = defaultdict(set)
    for line in data:
        key, values = line.split(":")
        for v in values.strip().split():
            graph[key].add(v)
    return graph


def dfs(graph):
    res = 0

    def _dfs(node, visited):
        if node == "out":
            if "dac" in visited and "fft" in visited:
                nonlocal res
                res += 1
            return
        for neighbour in graph[node]:
            if neighbour not in visited:
                _dfs(neighbour, visited | {neighbour})

    _dfs("svr", frozenset({"svr"}))
    return res


def bfs(graph):
    start = "svr"
    end = "out"
    all_paths = []
    queue = deque()
    queue.append((start, [start]))

    while queue:
        node, visited = queue.popleft()
        if node == end:
            if "dac" in visited and "fft" in visited:
                all_paths.append(visited)
            continue
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, visited + [neighbor]))

    return len(all_paths)


def main():
    file = "test_input_2.txt"
    graph = get_data(file)
    print(dfs(graph))
    print(bfs(graph))


if __name__ == "__main__":
    main()
