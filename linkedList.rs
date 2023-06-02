use std::boxed::Box;

#[derive(Debug)]
pub struct LinkedList<T>(Option<(T, Box<LinkedList<T>>)>);

impl <T> LinkedList<T> {
    pub fn new() -> Self {
        LinkedList(None)
    }
    
    pub fn push_front (&mut self, data: T) {
        let t = self.0.take();
        self.0 = Some((data, Box::new(LinkedList(t))));
    }
    
    pub fn push_back (&mut self, data: T) {
        match self.0 {
            Some((_, ref mut child)) => child.push_back(data),
            None => self.push_front(data),
        }
    }
}

fn main () {
   let mut list =  LinkedList::<i32>::new();

   list.push_front(9);
    list.push_back(2);
    list.push_front(89);
    list.push_front(23);

    println!("list = {:?}", list);
}
