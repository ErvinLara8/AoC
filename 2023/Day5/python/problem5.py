import copy

def get_next_point(cord_maps: list, point: int) -> int:
    for curr_map in cord_maps:
        if point >= curr_map[1] and point <= curr_map[1] + curr_map[2]:
            diff = point - curr_map[1]
            return curr_map[0] + diff
        
    return point 

def part_1():
    file_name = "testData.txt"
    # file_name = "fulldata.txt"
    
    with open(file_name, 'r') as data_file: 
        data = data_file.read().splitlines()

    seeds = [int(x) for x in  data.pop(0).split(':')[1].split() if x.strip()]
    data_map = {}
    data.pop(0)
    next_is_name = True
    curr_nums = []
    for i in range(len(data)):
        if next_is_name:
            curr_map = data[i].replace(' ','-').replace(':','')
            next_is_name = False
        elif data[i] == '' or i == len(data)-1:
            data_map[curr_map] = copy.deepcopy(curr_nums)
            next_is_name = True
            curr_nums.clear()
        else:
            curr_nums.append([int(x) for x in data[i].split()])
            
    lowest = ''
    for seed in seeds:
        key = 'seed-to-soil-map'
        next_point = get_next_point(data_map[key], seed)
        key = 'soil-to-fertilizer-map'
        next_point = get_next_point(data_map[key], next_point)
        key = 'fertilizer-to-water-map'
        next_point = get_next_point(data_map[key], next_point)
        key = 'water-to-light-map'
        next_point = get_next_point(data_map[key], next_point)
        key = 'light-to-temperature-map'
        next_point = get_next_point(data_map[key], next_point)
        key = 'temperature-to-humidity-map'
        next_point = get_next_point(data_map[key], next_point)
        key = 'humidity-to-location-map'
        next_point = get_next_point(data_map[key], next_point)
        
        if lowest == '':
            lowest = next_point
        elif next_point < lowest:
            lowest = next_point
    
    print(lowest)

# BRUTE FORCE TAKES A LONG TIME!!!
def part_2():
    # file_name = "testData.txt"
    file_name = "fulldata.txt"
    
    with open(file_name, 'r') as data_file: 
        data = data_file.read().splitlines()

    seeds_uncal= [int(x) for x in  data.pop(0).split(':')[1].split() if x.strip()]
    seeds = []
    print("entering seeds loop")
    for i in range(0,len(seeds_uncal), 2):
        curr_num = 0
        while curr_num < seeds_uncal[i+1]:
            seeds.append(seeds_uncal[i]+curr_num)
            curr_num += 1
    print("Exiting seeds loop")
    data_map = {}
    data.pop(0)
    next_is_name = True
    curr_nums = []
    for i in range(len(data)):
        if next_is_name:
            curr_map = data[i].replace(' ','-').replace(':','')
            next_is_name = False
        elif data[i] == '' or i == len(data)-1:
            data_map[curr_map] = copy.deepcopy(curr_nums)
            next_is_name = True
            curr_nums.clear()
        else:
            curr_nums.append([int(x) for x in data[i].split()])
            
    lowest = ''
    for seed in seeds:
        key = 'seed-to-soil-map'
        next_point = get_next_point(data_map[key], seed)
        key = 'soil-to-fertilizer-map'
        next_point = get_next_point(data_map[key], next_point)
        key = 'fertilizer-to-water-map'
        next_point = get_next_point(data_map[key], next_point)
        key = 'water-to-light-map'
        next_point = get_next_point(data_map[key], next_point)
        key = 'light-to-temperature-map'
        next_point = get_next_point(data_map[key], next_point)
        key = 'temperature-to-humidity-map'
        next_point = get_next_point(data_map[key], next_point)
        key = 'humidity-to-location-map'
        next_point = get_next_point(data_map[key], next_point)
        
        if lowest == '':
            lowest = next_point
        elif next_point < lowest:
            lowest = next_point
    
    print(lowest)
    
if __name__ == "__main__":
    # part_1()
    part_2()
    