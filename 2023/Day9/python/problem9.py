def find_next(pattern: list) -> int:
    increments = []
    for i in range(len(pattern)):
        if i + 1 == len(pattern):
            break
        increments.append(pattern[i + 1] - pattern[i])

    if increments.count(0) == len(increments):
        return pattern[-1]
    else:
        return pattern[-1] + find_next(increments)


def find_next_reversed(pattern: list) -> int:
    increments = []
    for i in range(len(pattern)):
        if i + 1 == len(pattern):
            break
        increments.append(pattern[i + 1] - pattern[i])

    if increments.count(0) == len(increments):
        return pattern[0]
    else:
        return pattern[0] - find_next_reversed(increments)


def part_2():
    # file_name = "testData.txt"
    file_name = "fulldata.txt"

    with open(f"/Users/elara/AoC/2023/Day9/python/{file_name}", "r") as data_file:
        data = data_file.read().splitlines()

    history = []
    for line in data:
        pattern = [int(x) for x in line.split()]
        history.append(find_next_reversed(pattern))

    print(sum(history))


def part_1():
    # file_name = "testData.txt"
    file_name = "fulldata.txt"

    with open(f"/Users/elara/AoC/2023/Day9/python/{file_name}", "r") as data_file:
        data = data_file.read().splitlines()

    history = []
    for line in data:
        pattern = [int(x) for x in line.split()]
        history.append(find_next(pattern))

    print(sum(history))


if __name__ == "__main__":
    # part_1()
    part_2()
