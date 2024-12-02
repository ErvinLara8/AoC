use std::fs;
use std::convert::TryFrom;

fn main() {
    // let data = "./test_data.txt";
    let data = "./data.txt";

    let contents = fs::read_to_string(data)
        .expect("Should have been able to read the file");

    part1(&contents);
    part2(&contents);
}

fn part1(contents: &String){
    let mut left_points: Vec<i32> = Vec::new();
    let mut right_points: Vec<i32> = Vec::new();

    for line in contents.lines() {
        let points = line.split_whitespace().collect::<Vec<&str>>();
        let left:i32 = points[0].parse().unwrap();
        let right:i32 = points[1].parse().unwrap();
        
        left_points.push(left);
        right_points.push(right);
    }

    left_points.sort();
    right_points.sort();

    let mut diff = 0;
    for i in 0..left_points.len() {
        if left_points[i] >= right_points[i] {
            diff = (left_points[i] - right_points[i]) + diff;
        } else {
            diff = (right_points[i] - left_points[i]) + diff;
        }
    }

    println!("{diff}")
}

fn part2(contents: &String){
    let mut left_points: Vec<i32> = Vec::new();
    let mut right_points: Vec<i32> = Vec::new();

    for line in contents.lines() {
        let points = line.split_whitespace().collect::<Vec<&str>>();
        let left:i32 = points[0].parse().unwrap();
        let right:i32 = points[1].parse().unwrap();
        
        left_points.push(left);
        right_points.push(right);
    }

    let mut diff = 0;
    for i in 0..left_points.len() {
        let appereances = right_points.iter().filter(|&n| *n == left_points[i]).count();
        diff = (left_points[i] * i32::try_from(appereances).unwrap()) + diff
    }

    println!("{diff}")
}