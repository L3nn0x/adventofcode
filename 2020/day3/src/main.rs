mod parser;
mod line;

struct Pointer {
    column: usize,
    row: usize,
    total: usize,
    next: fn(usize, usize) -> (usize, usize)
}

impl Pointer {
    fn new(next: fn(usize, usize) -> (usize, usize)) -> Self {
        Self {
            column: 0,
            row: 0,
            total: 0,
            next
        }
    }

    fn run(&mut self, rows: &Vec<line::Line>) {
        while self.row < rows.len() {
            self.total += match rows[self.row][self.column] {
                line::Value::Ground => 0,
                line::Value::Tree => 1
            };
            let (r, c) = (self.next)(self.row, self.column);
            self.column = if c >= rows[0].len() { c - rows[0].len() } else { c };
            self.row = r;
        }
    }
}

fn run1(i: usize, j: usize) -> (usize, usize) {
    (i + 1, j + 1)
}

fn run2(i: usize, j: usize) -> (usize, usize) {
    (i + 1, j + 3)
}

fn run3(i: usize, j: usize) -> (usize, usize) {
    (i + 1, j + 5)
}

fn run4(i: usize, j: usize) -> (usize, usize) {
    (i + 1, j + 7)
}

fn run5(i: usize, j: usize) -> (usize, usize) {
    (i + 2, j + 1)
}

fn main() {
    let line = parser::extract_input("input.txt", line::LineFactory{});

    let mut pointers = vec![Pointer::new(run1), Pointer::new(run2), Pointer::new(run3), Pointer::new(run4), Pointer::new(run5)];

    let mut total = 1;
    for (i, p) in pointers.iter_mut().enumerate() {
        p.run(&line);
        println!("Run {}: {}", i, p.total);
        total *= p.total;
    }

    println!("Total: {}", total);
}
