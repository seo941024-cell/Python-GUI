class Deque:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == self.rear

    def add_front(self, e):
        if self.is_full():
            print("overflow")
            return False
        self.queue[self.front] = e
        self.front = (self.front - 1 + self.capacity) % self.capacity
        return True

    def add_rear(self, e):
        if self.is_full():
            print("overflow")
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = e
        return True

    def delete_front(self):
        if self.is_empty():
            print("underflow")
            return None
        self.front = (self.front + 1) % self.capacity
        item = self.queue[self.front]
        self.queue[self.front] = None
        return item

    def delete_rear(self):
        if self.is_empty():
            print("underflow")
            return None
        item = self.queue[self.rear]
        self.queue[self.rear] = None
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return item

    def get_front(self):
        if self.is_empty(): return None
        return self.queue[(self.front + 1) % self.capacity]

    def get_rear(self):
        if self.is_empty(): return None
        return self.queue[self.rear]

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def clear(self):
        for i in range(self.capacity):
            self.queue[i] = None
        self.front = 0
        self.rear = 0


# 테스트
d = Deque()

d.add_rear('A');  d.add_rear('B');  d.add_rear('C')
d.add_front('Z')

print(d.get_front())   
print(d.get_rear())  
print(d.size())       

print(d.delete_front()) 
print(d.delete_rear())  
print(d.size())        