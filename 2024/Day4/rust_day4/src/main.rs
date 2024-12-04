use std::fs;

fn main() {
    // let data = "test_data.txt";
    let data = "data.txt";

    let contents = fs::read_to_string(data)
        .expect("Should have been able to read the file");

    part1(&contents);
    part2(&contents);
}

fn part1(contents: &String){

    let data_iter = contents.split_whitespace();
    let data_vec: Vec<&str> = data_iter.collect();
    let mut map: Vec<Vec<char>> = Vec::new();

    for line in 0..data_vec.len(){
        map.push( Vec::new());
        for c in data_vec[line].chars(){
            map[line].push(c);
        }
    }

    let mut xmas_count = 0;

    for y_pos in 0..map.len(){
        for x_pos in 0..map[y_pos].len(){
            let curr_c = map[y_pos][x_pos];
            if curr_c == 'X'{
                let mut word: String;

                // checking right
                if x_pos <  map[y_pos].len() - 3{
                    word = curr_c.to_string() + &map[y_pos][x_pos+1].to_string() + &map[y_pos][x_pos+2].to_string() + &map[y_pos][x_pos+3].to_string();
                    if word == "XMAS"{
                        xmas_count = xmas_count + 1;
                    }
                }

                // checking left
                if  x_pos >= 3{
                    word = curr_c.to_string() + &map[y_pos][x_pos-1].to_string() + &map[y_pos][x_pos-2].to_string() + &map[y_pos][x_pos-3].to_string();
                    if word == "XMAS"{
                        xmas_count = xmas_count + 1;
                    }
                }

                // checking up
                if y_pos < map.len() - 3 {
                    word = curr_c.to_string() + &map[y_pos+1][x_pos].to_string() + &map[y_pos+2][x_pos].to_string() + &map[y_pos+3][x_pos].to_string();
                    if word == "XMAS"{
                        xmas_count = xmas_count + 1;
                    }
                }

                // checking down
                if y_pos >= 3 {
                    word = curr_c.to_string() + &map[y_pos-1][x_pos].to_string() + &map[y_pos-2][x_pos].to_string() + &map[y_pos-3][x_pos].to_string();
                    if word == "XMAS"{
                        xmas_count = xmas_count + 1;
                    }
                }

                // checking up right 
                if y_pos < map.len() - 3 && x_pos <  map[y_pos].len() - 3 {
                    word = curr_c.to_string() + &map[y_pos+1][x_pos+1].to_string() + &map[y_pos+2][x_pos+2].to_string() + &map[y_pos+3][x_pos+3].to_string();
                    if word == "XMAS"{
                        xmas_count = xmas_count + 1;
                    }
                }

                // checking up left 
                if y_pos < map.len() - 3 && x_pos >= 3 {
                    word = curr_c.to_string() + &map[y_pos+1][x_pos-1].to_string() + &map[y_pos+2][x_pos-2].to_string() + &map[y_pos+3][x_pos-3].to_string();
                    if word == "XMAS"{
                        xmas_count = xmas_count + 1;
                    }
                }

                // checking down left 
                if y_pos >= 3 && x_pos >= 3 {
                    word = curr_c.to_string() + &map[y_pos-1][x_pos-1].to_string() + &map[y_pos-2][x_pos-2].to_string() + &map[y_pos-3][x_pos-3].to_string();
                    if word == "XMAS"{
                        xmas_count = xmas_count + 1;
                    }
                }

                // checking down right  
                if y_pos >= 3 && x_pos <  map[y_pos].len() - 3 {
                    word = curr_c.to_string() + &map[y_pos-1][x_pos+1].to_string() + &map[y_pos-2][x_pos+2].to_string() + &map[y_pos-3][x_pos+3].to_string();
                    if word == "XMAS"{
                        xmas_count = xmas_count + 1;
                    }
                }
            }
        }
       
    }
    println!("{xmas_count}");
}

fn part2(contents: &String){

    let data_iter = contents.split_whitespace();
    let data_vec: Vec<&str> = data_iter.collect();
    let mut map: Vec<Vec<char>> = Vec::new();

    for line in 0..data_vec.len(){
        map.push( Vec::new());
        for c in data_vec[line].chars(){
            map[line].push(c);
        }
    }

    let mut xmas_count = 0;

    for y_pos in 0..map.len(){
        for x_pos in 0..map[y_pos].len(){
            let curr_c = map[y_pos][x_pos];
            if curr_c == 'A'{

                let mut word: String;
                let mut has_up_right_to_down_left = false;
                let mut has_up_left_to_down_right = false;

                // checking up right to down left
                if (y_pos < map.len() - 1 && x_pos <  map[y_pos].len() - 1) && 
                (y_pos >= 1 && x_pos >= 1)
                {
                    word = map[y_pos+1][x_pos+1].to_string() + &curr_c.to_string() + &map[y_pos-1][x_pos-1].to_string();

                    has_up_right_to_down_left = (word == "MAS" || word == "SAM");
                    
                }
                // checking up left to down right
                if (y_pos < map.len() - 1 && x_pos >= 1) && 
                (y_pos >= 1 && x_pos <  map[y_pos].len() - 1 )
                {
                    word = map[y_pos+1][x_pos-1].to_string() + &curr_c.to_string() + &map[y_pos-1][x_pos+1].to_string();
                    has_up_left_to_down_right = (word == "MAS" || word == "SAM");

                }

                if has_up_left_to_down_right && has_up_right_to_down_left{
                    xmas_count = xmas_count + 1;
                }

            }
        }
       
    }
    println!("{xmas_count}");
}

