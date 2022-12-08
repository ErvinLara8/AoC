
def part1():
    
    # file_name = "testData.txt"
    file_name = "fulldata.txt"
    
    with open(file_name, 'r') as data_file: 
        
        data = data_file.read().splitlines()
        
    
    all_elfs = []
    curr_elf = 0
    
    for line in data: 
        if line != '':
            curr_elf += int(line)
        
        if line == '' or line == data[-1]:
            all_elfs.append(curr_elf)
            curr_elf = 0
    
    max_value = max(all_elfs)
    print(max_value)
    
    return all_elfs

def part2():
    
    all_elfs = part1()
    
    all_elfs.sort(reverse=True)
    
    top_3_sum = all_elfs[0] + all_elfs[1] + all_elfs[2]
    print(top_3_sum)
        
if __name__ == "__main__":
    
    part2()
    