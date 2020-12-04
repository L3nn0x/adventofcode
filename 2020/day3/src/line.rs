pub enum Value {
    Ground,
    Tree
}

pub struct Line {
    data: Vec<Value>
}

impl Line {
    pub fn len(&self) -> usize {
        self.data.len()
    }
}

use std::ops::Index;

impl Index<usize> for Line {
    type Output = Value;
    fn index(&self, index: usize) -> &Value {
        &self.data[index]
    }
}

pub struct LineFactory;

use super::parser::Factory;

impl Factory for LineFactory {
    type Item = Line;

    fn create(line: &[u8]) -> Result<Self::Item, failure::Error> {
        
        let mut data = Vec::with_capacity(line.len());

        for c in line {
            match *c as char {
                '.' => data.push(Value::Ground),
                _ => data.push(Value::Tree)
            }
        }

        Ok(Line{ data })
    }
}