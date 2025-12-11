def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    graph = {}
    for line in data:
        key, values = line.split(":")
        graph[key] = tuple(values.strip().split())
    return graph


def get_answer(graph):
    def dfs(node):
        if node == "out":
            return 1
        return sum(dfs(neighbour) for neighbour in graph[node])

    return dfs("you")


def get_answer_2(graph):
    memo = {}

    def dfs(node, vis_state):
        key = (node, vis_state)
        if key in memo:
            return memo[key]

        dac_visited, fft_visited = vis_state
        paths = 0

        if node == "out":
            if dac_visited and fft_visited:
                paths = 1
        else:
            for v in graph.get(node, []):
                new_dac = dac_visited or (v == "dac")
                new_fft = fft_visited or (v == "fft")
                new_state = (new_dac, new_fft)
                paths += dfs(v, new_state)

        memo[key] = paths
        return paths

    return dfs("svr", (False, False))


def main():
    file = "input.txt"
    graph = get_data(file)
    print(get_answer(graph))
    print(get_answer_2(graph))


if __name__ == "__main__":
    main()
