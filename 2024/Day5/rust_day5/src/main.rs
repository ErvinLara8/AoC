use std::fs;
use std::collections::HashMap;

fn main() {
    // let data = "test_data.txt";
    let data = "data.txt";

    let contents = fs::read_to_string(data)
        .expect("Should have been able to read the file");

    part1(&contents);
    part2(&contents);
}

fn part1(contents: &String){

    let mut rules: Vec<&str> = Vec::new();
    let mut pri: Vec<&str> = Vec::new();

    let mut finished_rules = false;
    for line in contents.lines(){
        if finished_rules{
            pri.push(line);
        } else if line != ""{
            rules.push(line);
        }
        if line == ""{
            finished_rules = true;
        }
    }

    // creating map of rules where key is page and list is pages after
    let mut rules_map: HashMap<&str, Vec<&str>> = HashMap::new();
    for rule in rules.iter(){
        let rule_iter = rule.split("|");
        let sep_rules: Vec<&str> = rule_iter.collect();

        if rules_map.get(sep_rules[0]) == None {
            rules_map.insert(sep_rules[0], Vec::new());
        } 

        rules_map.get_mut(sep_rules[0]).expect("Error").push(sep_rules[1]);
    }

    let mut valid_pri: Vec<&str> = Vec::new();
    let mut previous_pri: Vec<&str> = Vec::new();

    for line in pri.iter(){
        let mut is_valid = true;

        for page in line.split(","){
            if previous_pri.len() == 0{
                previous_pri.push(page);
            } else {
  
                for previous in previous_pri.iter(){
                    if rules_map.get(page) != None && rules_map.get_mut(page).expect("").contains(previous){
                        is_valid = false;
                        break;
                    }
                }

                if !is_valid{
                    break;
                }
                previous_pri.push(page);
            }
        }
        previous_pri.clear();
        if is_valid{
            valid_pri.push(line);
        }
    }

    let mut result = 0;

    for valid_line in valid_pri.iter(){
        let valid_iter = valid_line.split(",");
        let valid_vec: Vec<&str> = valid_iter.collect();

        let middle = (valid_vec.len() - 1) / 2;

        result = result + &valid_vec[middle].parse().unwrap();
    }

    println!("{result}")

}

fn part2(contents: &String){
    let mut rules: Vec<&str> = Vec::new();
    let mut pri: Vec<&str> = Vec::new();

    let mut finished_rules = false;
    for line in contents.lines(){
        if finished_rules{
            pri.push(line);
        } else if line != ""{
            rules.push(line);
        }
        if line == ""{
            finished_rules = true;
        }
    }

    // creating map of rules where key is page and list is pages after
    let mut rules_map: HashMap<&str, Vec<&str>> = HashMap::new();
    for rule in rules.iter(){
        let rule_iter = rule.split("|");
        let sep_rules: Vec<&str> = rule_iter.collect();

        if rules_map.get(sep_rules[0]) == None {
            rules_map.insert(sep_rules[0], Vec::new());
        } 

        rules_map.get_mut(sep_rules[0]).expect("Error").push(sep_rules[1]);
    }

    let mut non_valid_pri: Vec<&str> = Vec::new();
    let mut previous_pri: Vec<&str> = Vec::new();

    for line in pri.iter(){
        let mut is_valid = true;

        for page in line.split(","){
            if previous_pri.len() == 0{
                previous_pri.push(page);
            } else {
  
                for previous in previous_pri.iter(){
                    if rules_map.get(page) != None && rules_map.get_mut(page).expect("").contains(previous){
                        is_valid = false;
                        break;
                    }
                }

                if !is_valid{
                    break;
                }
                previous_pri.push(page);
            }
        }
        previous_pri.clear();
        if !is_valid{
            non_valid_pri.push(line);
        }
    }
    
    let mut fixed_pri: Vec<Vec<&str>> = Vec::new();
    
    for line in non_valid_pri{
        
        for page in line.split(","){
            if previous_pri.len() == 0{
                previous_pri.push(page);
            } else {
                let mut has_mistake = false;
                for previous_index in 0..previous_pri.len(){
                    if rules_map.get(page) != None && rules_map.get_mut(page).expect("").contains(&previous_pri[previous_index]){
                        let mistake_index = previous_pri.iter().position(|&r| r == previous_pri[previous_index]).unwrap();
                        previous_pri.insert(mistake_index, page);
                        has_mistake = true;
                        break;
                    } 
                }
                if !has_mistake{
                    previous_pri.push(page);
                }
            }
        }
        
        fixed_pri.push(previous_pri.clone());
        previous_pri.clear();
    }

    let mut result = 0;

    for line in fixed_pri{
        let middle = (line.len() - 1) / 2;
        result = result + &line[middle].parse().unwrap();
    }
    println!("{result}");
}