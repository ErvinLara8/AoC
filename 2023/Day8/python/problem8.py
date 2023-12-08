import math


def part_2():
    # file_name = "testData.txt"
    file_name = "fulldata.txt"

    with open(file_name, "r") as data_file:
        data = data_file.read().splitlines()

    steps = ""
    steps_created = False
    guide = {}
    for line in data:
        if not steps_created and line != "":
            steps += line
        if line == "" and not steps_created:
            steps_created = True

        if steps_created and line != "":
            location = line.split(" = ")[0]
            l_destination = line.split(" = ")[1].split(", ")[0][1:]
            r_destination = line.split(" = ")[1].split(", ")[1][:-1]
            guide[location] = (l_destination, r_destination)

    curr_pos = [node for node in guide if node[-1] == "A"]
    node_steps = []
    for node in curr_pos:
        i = 0
        total_steps = 0
        while node[-1] != "Z":
            step = steps[i]
            if step == "L":
                node = guide[node][0]
            else:
                node = guide[node][1]

            total_steps += 1
            i += 1
            if i == len(steps):
                i = 0
        node_steps.append(total_steps)

    print(math.lcm(*node_steps))


def part_1():
    # file_name = "testData.txt"
    file_name = "fulldata.txt"

    with open(file_name, "r") as data_file:
        data = data_file.read().splitlines()

    steps = ""
    steps_created = False
    guide = {}
    for line in data:
        if not steps_created and line != "":
            steps += line
        if line == "" and not steps_created:
            steps_created = True

        if steps_created and line != "":
            location = line.split(" = ")[0]
            l_destination = line.split(" = ")[1].split(", ")[0][1:]
            r_destination = line.split(" = ")[1].split(", ")[1][:-1]
            guide[location] = (l_destination, r_destination)

    curr_pos = "AAA"
    i = 0
    total_steps = 0
    while curr_pos != "ZZZ":
        step = steps[i]
        if step == "L":
            curr_pos = guide[curr_pos][0]
        else:
            curr_pos = guide[curr_pos][1]

        total_steps += 1
        i += 1
        if i == len(steps):
            i = 0

    print(total_steps)


if __name__ == "__main__":
    # part_1()
    part_2()
