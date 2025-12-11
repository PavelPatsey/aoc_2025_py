from collections import defaultdict


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    graph = defaultdict(list)
    for line in data:
        key, values = line.split(":")
        graph[key] = values.strip().split()
    return graph


def get_answer(graph):
    res = 0

    def dfs(node):
        if node == "out":
            nonlocal res
            res += 1
            return
        for neighbour in graph[node]:
            dfs(neighbour)

    dfs("you")
    return res


def main():
    file = "input.txt"
    graph = get_data(file)
    print(graph)
    print(get_answer(graph))


if __name__ == "__main__":
    main()
