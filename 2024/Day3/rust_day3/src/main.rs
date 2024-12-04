use std::fs;
use regex::Regex;

fn main() {
    // let data = "/Users/elara/AoC/2024/Day3/test_data.txt";
    let data = "/Users/elara/AoC/2024/Day3/data.txt";

    let contents = fs::read_to_string(data)
        .expect("Should have been able to read the file");

    // part1(&contents);
    part2(&contents);
}

fn part1(contents: &String){
    let re = Regex::new(r"mul\([0-9]{1,3},[0-9]{1,3}\)").unwrap();
    let found_patterns: Vec<&str> = re.find_iter(contents).map(|m| m.as_str()).collect();
    let mut sum = 0;
    for i in found_patterns.iter(){
        let mut curr = i.to_string();
        curr = curr.replace("mul(", "").replace(")","");
        let nums_iter = curr.split(",");
        let nums_vec: Vec<&str> = nums_iter.collect();
        sum = (nums_vec[0].parse::<i32>().unwrap() * nums_vec[1].parse::<i32>().unwrap()) + sum
    }
    
    println!("{sum}")
}

fn part2(contents: &String){

    let all_do_iter = contents.split("do()");
    let all_do: Vec<&str> = all_do_iter.collect();
    let mut valid_muls: Vec<&str> = Vec::new();

    for x in all_do.iter(){
        let patterns_iter = x.split("don't()");
        let pattern: Vec<&str> = patterns_iter.collect();
        valid_muls.push(pattern[0]);
    }

    let re = Regex::new(r"mul\([0-9]{1,3},[0-9]{1,3}\)").unwrap();
    let mut found_patterns: Vec<&str> = Vec::new();
    
    for pattern in valid_muls.iter(){
        let mut curr_pattern: Vec<&str> = re.find_iter(pattern).map(|m| m.as_str()).collect();
        found_patterns.append(&mut curr_pattern);
    }

    let mut sum = 0;
    for i in found_patterns.iter(){
        let mut curr = i.to_string();
        curr = curr.replace("mul(", "").replace(")","");
        let nums_iter = curr.split(",");
        let nums_vec: Vec<&str> = nums_iter.collect();
        sum = (nums_vec[0].parse::<i32>().unwrap() * nums_vec[1].parse::<i32>().unwrap()) + sum
    }
    
    println!("{sum}")
}