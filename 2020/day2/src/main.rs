use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

mod parser;

fn main() {
    let mut total1 = 0;
    let mut total2 = 0;
    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(data) = line {
                let parsed = parser::parse(data.as_bytes());
                match parsed {
                    Ok((_, value)) => {
                        if value.check_password_part1() {
                            total1 += 1;
                        }
                        if value.check_password_part2() {
                            total2 += 1;
                        }
                    },
                    Err(error) => println!("Error: {}", error),
                }
            }
        }
    }
    println!("Total passwords part 1: {}", total1);
    println!("Total passwords part 2: {}", total2);
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}