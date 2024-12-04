use std::fs;

fn main() {
    // let data = "./test_data.txt";
    let data = "./data.txt";

    let contents = fs::read_to_string(data)
        .expect("Should have been able to read the file");

    // part1(&contents);
    part2(&contents);
}

fn part1(contents: &String){
    let mut safe_count = 0;
    let mut is_safe: bool;
    let mut prev_num: Option<i32>;
    let mut prev_diff:i32;
    for line in contents.lines() {
        is_safe = true;
        prev_num = None;
        prev_diff = 0;
        for str_num in line.split_whitespace(){
            let num: i32 = str_num.parse().unwrap();

            if prev_num == None {
                prev_num = Some(num);
                continue;
            }

            let diff = prev_num.unwrap() - num;

            if diff.abs() > 3 || diff == 0{
                is_safe = false;
                break;
            }

            if (prev_diff < 0 && diff > 0) || 
               (prev_diff > 0 && diff < 0) {
                is_safe = false;
                break;
            }

            prev_diff = diff;
            prev_num = Some(num);   
        }
        if is_safe {
            safe_count = safe_count + 1;
        }
    }

    // println!("{safe_count}")
}

fn part2(contents: &String){
    let mut safe_count = 0;

    for line in contents.lines() {
        
        if check_if_safe(&line) {
            safe_count = safe_count + 1;
        }
    }

    println!("{safe_count}")
}


fn check_if_safe(line: &str) -> bool{

    let mut is_safe: bool = true;
    let split_iter = line.split_whitespace();
    let num_vec: Vec<&str> = split_iter.collect();

    for i in 0..(num_vec.len()+1){

        let mut curr_pattern = num_vec.clone();

        if i > 0{
            curr_pattern.remove(i-1);
        }

        is_safe = true;
        let mut prev_num: Option<i32> = None;
        let mut prev_diff:i32 = 0;

        for str_num in curr_pattern.iter_mut(){

            let num: i32 = str_num.parse().unwrap();

            if prev_num == None {
                prev_num = Some(num);
                continue;
            }

            let diff = prev_num.unwrap() - num;

            if diff.abs() > 3 || diff == 0{
                is_safe = false;
                break;
            }

            if (prev_diff < 0 && diff > 0) || 
                (prev_diff > 0 && diff < 0) {
                is_safe = false;
                break;
            }

            prev_diff = diff;
            prev_num = Some(num);  
        }

        if is_safe{
            break;
        }
    }

    return is_safe;
}
