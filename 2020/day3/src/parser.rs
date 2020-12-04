pub trait Factory {
    type Item;
    fn create(line: &[u8]) -> Result<Self::Item, failure::Error>;
}

pub fn extract_input<F, P: AsRef<std::path::Path>>(filename: P, _f: F) -> Vec<F::Item>
    where F: Factory {
    let mut ret = Vec::new();
    if let Ok(lines) = read_lines(filename) {
        for line in lines {
            if let Ok(data) = line {
                let parsed = F::create(data.as_bytes());
                match parsed {
                    Ok(value) => {
                        ret.push(value);
                    },
                    Err(error) => panic!("Error: {}", error),
                }
            }
        }
    }
    ret
}

use std::io;
use std::fs::File;
use std::io::BufRead;

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<std::path::Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}