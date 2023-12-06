from functools import reduce

def get_winners(time: int, distance: int) -> list:
    winners = []
    for button_held in range(time):
        traveled_time = time - button_held
        traveled_distance = button_held*traveled_time
        if traveled_distance > distance:
            winners.append(traveled_time)
    return winners

def part_1():
    # file_name = "testData.txt"
    file_name = "fulldata.txt"
    
    with open(file_name, 'r') as data_file: 
        data = data_file.read().splitlines()
    
    times = [int(x) for x in data[0].split(':')[1].split() if x.strip()]
    distances = [int(x) for x in data[1].split(':')[1].split() if x.strip()]
    
    differentials = []
    for i in range(len(times)):
        winners = get_winners(times[i], distances[i])
        differentials.append(len(winners))

    print(reduce(lambda x, y: x*y, differentials))

def part_2():
    # file_name = "testData.txt"
    file_name = "fulldata.txt"
    
    with open(file_name, 'r') as data_file: 
        data = data_file.read().splitlines()
    
    time = int(data[0].split(':')[1].replace(' ',''))
    distance = int(data[1].split(':')[1].replace(' ',''))
    
    winners = get_winners(time, distance)
    
    print(len(winners))
    
if __name__ == "__main__":
    part_1()
    part_2()
    