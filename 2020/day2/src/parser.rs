use nom::{
    IResult,
    bytes::complete::{take, take_while1},
    character::{is_digit, is_alphabetic, complete::char}
  };

// 1-3 a: abcde

#[derive(Debug)]
pub struct Line {
    letter: char,
    min_times: i32,
    max_times: i32,
    password: String
}

impl Line {
    pub fn new(letter: char, min: i32, max: i32, password: String) -> Self {
        Self {
            letter,
            min_times: min,
            max_times: max,
            password
        }
    }

    pub fn check_password_part1(&self) -> bool {
        let mut hash = std::collections::HashMap::new();
        for c in self.password.chars() {
            let counter = hash.entry(c).or_insert(0);
            *counter += 1;
        }
        if let Some(n) = hash.get(&self.letter) {
            *n >= self.min_times && *n <= self.max_times
        } else {
            false
        }
    }

    pub fn check_password_part2(&self) -> bool {
        let pass = self.password.as_bytes();
        if self.min_times <= 0 || self.max_times as usize >= self.password.len() + 1 {
            return false;
        }
        let c1 = pass[(self.min_times - 1) as usize] as char;
        let c2 = pass[(self.max_times - 1) as usize] as char;
        (c1 == self.letter && c2 != self.letter) || (c1 != self.letter && c2 == self.letter)
    }
}

pub fn parse(input: &[u8]) -> IResult<&[u8], Line> {
    let (rest, min) = take_while1(is_digit)(input)?;
    let (rest, _) = char('-')(rest)?;
    let (rest, max) = take_while1(is_digit)(rest)?;
    let (rest, _) = char(' ')(rest)?;
    let (rest, c) = take(1u8)(rest)?;
    let (rest, _) = take(2u8)(rest)?;
    let (rest, password) = take_while1(is_alphabetic)(rest)?;
    Ok((rest, Line::new(c[0] as char,
        std::str::from_utf8(min).unwrap().parse::<i32>().unwrap(),
        std::str::from_utf8(max).unwrap().parse::<i32>().unwrap(),
        std::str::from_utf8(password).unwrap().to_string())))
}