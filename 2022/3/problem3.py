def find_value(item:str) -> int:
    
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96
        

def main1():
    #file_name = "testData.txt"
    file_name = "fullData.txt"
    
    with open(file_name, 'r') as data_file: 
        
        data = data_file.read().splitlines()
    
    priority_sum = 0
    
    for rucksack in data:
        
        first_half, second_half = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        
        priority_item = ""
        
        for item in first_half:
            
            if item in second_half:
                
                priority_item = item
                break
            
            
        priority_sum += find_value(priority_item)
    
    print(priority_sum)
    

def main2():
    # file_name = "testData.txt"
    file_name = "fullData.txt"
    
    with open(file_name, 'r') as data_file: 
        
        data = data_file.read().splitlines()
    
    badge_sum = 0
    
    for rucksack in range(0,len(data), 3):
        
        ruck1 = data[rucksack]
        ruck2 = data[rucksack + 1]
        ruck3 = data[rucksack + 2]
        
        priority_item = ""
        
        for item in ruck1: 
            
            if item in ruck2 and item in ruck3:
                priority_item = item
                break
            
        badge_sum += find_value(priority_item)
    
    print(badge_sum)
                        
        
if __name__ == "__main__":
    
    # main1()
    main2()