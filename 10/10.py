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


def press_button(lights: tuple, buttons: tuple) -> tuple:
    new_lights = [x for x in lights]
    for b in buttons:
        new_lights[b] = (new_lights[b] + 1) % 2
    return tuple(new_lights)


def find_fewest_bfs(lights, buttons):
    lights = tuple(lights)
    start = tuple(0 for _ in range(len(lights)))
    visited = set()
    visited.add(start)
    queue = deque([(0, start)])

    while queue:
        i, l = queue.popleft()
        if l == lights:
            return i
        for b in buttons:
            new_l = press_button(l, b)
            if new_l not in visited:
                visited.add(new_l)
                queue.append((i + 1, new_l))


@timer
def get_answer(lights, buttons):
    res = 0
    for l, b in tqdm(zip(lights, buttons)):
        res += find_fewest_bfs(l, b)
    return res


def main():
    file = "input.txt"
    lights, buttons, joltages = get_data(file)
    print(get_answer(lights, buttons))


if __name__ == "__main__":
    main()
