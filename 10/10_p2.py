from collections import deque

from tqdm import tqdm
from utils import timer


def get_data(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    lights = []
    buttons = []
    joltages = []
    for line in data:
        i = line.find("[")
        j = line.find("]")
        lights.append([0 if x == "." else 1 for x in line[i + 1 : j]])

        a = line.find("{")
        b = line.find("}")
        joltages.append([int(x) for x in line[a + 1 : b].split(",")])

        buttons.append(
            [
                tuple(int(y) for y in x.strip("(").strip(")").split(","))
                for x in line[j + 1 : a].split()
            ]
        )
    return lights, buttons, joltages


def press_button(joltages: tuple, buttons: tuple) -> tuple:
    new_lights = [x for x in joltages]
    for b in buttons:
        new_lights[b] = new_lights[b] + 1
    return tuple(new_lights)


def is_valid(j, joltages):
    for a, b in zip(j, joltages):
        if a > b:
            return False
    return True


def find_fewest_bfs(joltages, buttons):
    joltages = tuple(joltages)
    start = tuple(0 for _ in range(len(joltages)))
    visited = set()
    visited.add(start)
    queue = deque([start])

    i = 0
    while True:
        new_queue = deque([])
        while queue:
            j = queue.popleft()
            if j == joltages:
                return i
            for b in buttons:
                new_l = press_button(j, b)
                if new_l not in visited and is_valid(j, joltages):
                    visited.add(new_l)
                    new_queue.append(new_l)
        queue = new_queue
        i += 1


@timer
def get_answer_2(joltages, buttons):
    res = 0
    for j, b in tqdm(zip(joltages, buttons)):
        c = find_fewest_bfs(j, b)
        print(f"{c=}")
        res += c
    return res


def main():
    file = "test_input.txt"
    lights, buttons, joltages = get_data(file)
    print(get_answer_2(joltages, buttons))


if __name__ == "__main__":
    main()
