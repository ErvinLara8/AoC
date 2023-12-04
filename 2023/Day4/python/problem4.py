def part_1():
    # file_name = "testData.txt"
    file_name = "fulldata.txt"
    
    with open(file_name, 'r') as data_file: 
        data = data_file.read().splitlines()
    
    total_points = 0
    for line in data:
        card_points = 0
        winning_nums = [x for x in line.split("|")[0].split(':')[1].split(' ') if x.strip()]
        game_nums = [x for x in line.split("|")[1].split(' ') if x.strip()]
        
        for num in winning_nums:
            matches = game_nums.count(num)
            if (card_points == 0 or card_points == 1) and matches:
                card_points += 1
                matches -=1
            for _ in range(matches):
                card_points = card_points*2
            
        total_points += card_points
            
    print(total_points)


def part_2():
    # file_name = "testData.txt"
    file_name = "fulldata.txt"
    
    with open(file_name, 'r') as data_file: 
        data = data_file.read().splitlines()    
    
    cards = {}
    for line in data: 
        card_num = line.split(':')[0].split()[1]
        cards[int(card_num)] = [
                1,
                [x for x in line.split("|")[0].split(':')[1].split(' ') if x.strip()],
                [x for x in line.split("|")[1].split(' ') if x.strip()]
            ]
        
    for card_num in cards.keys():
        curr_card_count = cards[card_num][0]
        winning_nums = cards[card_num][1]
        game_nums = cards[card_num][2]
        
        matches = 0
        for num in winning_nums:
            matches += game_nums.count(num)
            
        if matches:
            curr_won = card_num + 1
        
        for _ in range(matches):
            cards[curr_won][0] += curr_card_count
            curr_won += 1
    
    total_cards = 0 
    for card_num in cards.keys():
        total_cards += cards[card_num][0] 
    
    print(total_cards)
                
if __name__ == "__main__":
    # part_1()
    part_2()
    