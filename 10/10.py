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

        buttons.append([eval(x) for x in line[j + 1 : a].split()])
    return lights, buttons, joltages


def find_fewest_bfs(lights, buttons):
    pass


def get_answer(lights, buttons):
    res = 0
    for l, b in zip(lights, buttons):
        c = find_fewest_bfs(l, b)
        res += c
    return res


def main():
    file = "test_input.txt"
    lights, buttons, joltages = get_data(file)
    print(lights)
    print(buttons)
    print(joltages)
    print(get_answer(lights, buttons))


if __name__ == "__main__":
    main()
