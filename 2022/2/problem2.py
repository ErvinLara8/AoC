
def main():
    # file_name = "testData.txt"
    file_name = "fullData.txt"
    
    with open(file_name, 'r') as data_file: 
        
        data = data_file.read().splitlines()
        
    point_info = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    
    score = 0
    for round in data:
        
        score += point_info.get(round[-1])
        
        if round[0] == 'A':
            
            if round[-1] == "X":
                score += 3
            
            if round[-1] == "Y":
                score += 6
                
        if round[0] == 'B':
            
            if round[-1] == "Y":
                score += 3
            
            if round[-1] == "Z":
                score += 6
                
        if round[0] == 'C':
            
            if round[-1] == "Z":
                score += 3
            
            if round[-1] == "X":
                score += 6
        
    print(score)
        
    
    point_info2 = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    
    
    score2 = 0
    for round in data:
        
        score2 += point_info2.get(round[-1])
        
        
        if round[0] == 'A':
            
            if round[-1] == "X":
                score2 += 3
            
            if round[-1] == "Y":
                score2 += 1
                
            if round[-1] == "Z":
                score2 += 2
                
                
        if round[0] == 'B':
            
            if round[-1] == "X":
                score2 += 1
            
            if round[-1] == "Y":
                score2 += 2
                
            if round[-1] == "Z":
                score2 += 3
                
        if round[0] == 'C':
            
            if round[-1] == "X":
                score2 += 2
            
            if round[-1] == "Y":
                score2 += 3
                
            if round[-1] == "Z":
                score2 += 1
        
        
    print(score2)

if __name__ == "__main__":
    
    main()
