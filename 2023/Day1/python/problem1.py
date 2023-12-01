
def check_sub(string: str, keys: list) -> [bool, str]:
    for key in keys:
        if key in string:
            return True, key
    return False, "-1"


def part_1():
    
    # file_name = "testdata.txt"
    file_name = "fulldata.txt"
    with open(file_name, 'r') as data_file: 
        data = data_file.read().splitlines()
    
    num_list = []
    for line in data:
        curr_num = ""
        for i in line:
            if i.isdigit():
                curr_num += i
                break
        for j in reversed(line):
            if j.isdigit():
                curr_num += j
                break
        
        num_list.append(int(curr_num))
    
    result = sum(num_list)
    print(result)

def part_2():
    
    # file_name = "testdata2.txt"
    file_name = "fulldata2.txt"
    with open(f"/Users/elara/AoC/2023/Day1/python/{file_name}", 'r') as data_file: 
        data = data_file.read().splitlines()
    
    valid_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    num_list = []
    for line in data:
        curr_num = ""
        spelled_digit = ""
        for i in line:
            is_sub, key = check_sub(spelled_digit.lower(), valid_digits.keys())
            if is_sub:
                curr_num += valid_digits[key]
                break
            if i.isdigit():
                curr_num += i
                break
            spelled_digit += i
        
        spelled_digit = ""     
        for j in reversed(line):
            reversed_digit = spelled_digit[::-1]
            is_sub, key = check_sub(reversed_digit.lower(), valid_digits.keys())
            if is_sub:
                curr_num += valid_digits[key]
                break
            if j.isdigit():
                curr_num += j
                break
            spelled_digit += j
        
        num_list.append(int(curr_num))
    
    result = sum(num_list)
    print(result)

if __name__ == "__main__":
    # part_1()
    part_2()