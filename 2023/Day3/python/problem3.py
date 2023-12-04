def part_1():
    # file_name = "testdata1.txt"
    file_name = "fulldata1.txt"
    with open(f"{file_name}", 'r') as data_file: 
        data = data_file.read().splitlines()
    
    schematics = []
    part_nums = []
    for i in range(len(data)):
        schematics.append([])
        for char in data[i]:
            schematics[i].append(char)
            
    num = ''
    is_part_num = False
    for y in range(len(schematics)):
        for x in range(len(schematics[y])):
            if schematics[y][x].isdigit():
                num += schematics[y][x]
                if ((x != 0 and not schematics[y][x-1].isdigit() and schematics[y][x-1] != '.') or 
                (x != len(schematics[y])-1 and not schematics[y][x+1].isdigit() and schematics[y][x+1] != '.') or 
                (y != 0 and x != 0 and not schematics[y-1][x-1].isdigit() and schematics[y-1][x-1] != '.') or 
                (y != 0 and not schematics[y-1][x].isdigit() and schematics[y-1][x] != '.') or
                (y != 0 and x != len(schematics[y])-1 and not schematics[y-1][x+1].isdigit() and schematics[y-1][x+1] != '.') or
                (y != len(schematics) - 1 and x != 0 and not schematics[y+1][x-1].isdigit() and schematics[y+1][x-1] != '.') or 
                (y != len(schematics) - 1 and not schematics[y+1][x].isdigit() and schematics[y+1][x] != '.') or
                (y != len(schematics) - 1 and x != len(schematics[y])-1 and not schematics[y+1][x+1].isdigit() and schematics[y+1][x+1] != '.')
                ):
                    is_part_num = True
                
                if x == len(schematics[y])-1 or not schematics[y][x+1].isdigit():
                    if is_part_num:
                        part_nums.append(int(num))
                    is_part_num = False
                    num = ''
                    
    print(sum(part_nums))
    
def part_2():
    # file_name = "testdata2.txt"
    file_name = "fulldata2.txt"
    with open(f"{file_name}", 'r') as data_file: 
        data = data_file.read().splitlines()
    
    schematics = []
    part_nums = []
    for i in range(len(data)):
        schematics.append([])
        for char in data[i]:
            schematics[i].append(char)
            
    num = ''
    gears = {}
    gear_location = ()
    for y in range(len(schematics)):
        for x in range(len(schematics[y])):
            if schematics[y][x].isdigit():
                num += schematics[y][x]
                if x != 0 and schematics[y][x-1] == '*':
                    gear_location = (x-1, y)
                if x != len(schematics[y])-1 and schematics[y][x+1] == '*':
                    gear_location = (x+1, y)
                if y != 0 and x != 0 and schematics[y-1][x-1] == '*':
                    gear_location = (x-1, y-1)
                if y != 0 and schematics[y-1][x] == '*':
                    gear_location = (x, y-1)
                if y != 0 and x != len(schematics[y])-1 and schematics[y-1][x+1] == '*':
                    gear_location = (x+1, y-1)
                if y != len(schematics) - 1 and x != 0 and schematics[y+1][x-1] == '*':
                    gear_location = (x-1, y+1)
                if y != len(schematics) - 1 and schematics[y+1][x] == '*':
                    gear_location = (x, y+1)
                if y != len(schematics) - 1 and x != len(schematics[y])-1 and schematics[y+1][x+1] == '*':
                    gear_location = (x+1, y+1)
 
                if x == len(schematics[y])-1 or not schematics[y][x+1].isdigit():
                    if len(gear_location) != 0 and gear_location not in gears.keys():
                        gears[gear_location] = int(num)
                    elif len(gear_location) != 0 :
                        part_nums.append(gears.pop(gear_location) * int(num))
                    gear_location = ()
                    num = ''
                    
    print(sum(part_nums))
    
if __name__ == "__main__":
    part_1()
    part_2()