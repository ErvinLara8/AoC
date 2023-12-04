def part_1():
    # file_name = "testdata1.txt"
    file_name = "fulldata1.txt"
    with open(f"{file_name}", 'r') as data_file: 
        data = data_file.read().splitlines()
    
    valid_game_ids = []
    for line in data:
        seperated_info = line.split(":")
        game_id = seperated_info[0].split(' ')[1]
        game_sets = seperated_info[1].split(';')
        valid_set = True
        for run in game_sets:
            for play in run.split(','):
                play = play[1:]
                sep_info_2 = play.split(' ')
                count = sep_info_2[0]
                color = sep_info_2[1]
                if color == 'red' and int(count) > 12:
                    valid_set = False
                    break
                if color == 'green' and int(count) > 13:
                    valid_set = False
                    break
                if color == 'blue' and int(count) > 14:
                    valid_set = False
                    break
            
        if valid_set:
            valid_game_ids.append(int(game_id))
                
    result = sum(valid_game_ids)
    print(result)
    
def part_2():
    # file_name = "testdata1.txt"
    file_name = "fulldata2.txt"
    with open(f"{file_name}", 'r') as data_file: 
        data = data_file.read().splitlines()
        
    powers = []
    for line in data:
        seperated_info = line.split(":")
        game_id = seperated_info[0].split(' ')[1]
        game_sets = seperated_info[1].split(';')
        valid_set = True
        highest_nums = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for run in game_sets:
            for play in run.split(','):
                play = play[1:]
                sep_info_2 = play.split(' ')
                count = sep_info_2[0]
                color = sep_info_2[1]
                if int(count) > highest_nums[color]:
                    highest_nums[color] = int(count)
        
        curr_num = 1
        for key, value in highest_nums.items():
            curr_num *= value
        
        powers.append(curr_num)
    result = sum(powers)
    print(result)
    
if __name__ == "__main__":
    # part_1()
    part_2()