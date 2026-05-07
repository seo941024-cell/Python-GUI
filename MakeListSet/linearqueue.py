class LinearQueue:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity  # 고정 크기 배열
        self.front = -1  # dequeue 위치
        self.rear = -1   # enqueue 위치

    def is_full(self):
        return self.rear == self.capacity - 1

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self, e):
        if self.is_full():
            print("overflow — 큐가 가득 찼습니다")
            return False
        self.rear += 1
        self.queue[self.rear] = e
        return True

    def dequeue(self):
        if self.is_empty():
            print("underflow — 큐가 비어있습니다")
            return None
        self.front += 1
        item = self.queue[self.front]
        self.queue[self.front] = None  # 자리 비우기
        return item

    def peek(self):
        if self.is_empty():
            print("큐가 비어있습니다")
            return None
        return self.queue[self.front + 1]

    def size(self):
        return self.rear - self.front

    def clear(self):
        for i in range(self.capacity):
            self.queue[i] = None
        self.front = -1
        self.rear = -1

    def print_queue(self):
        if self.is_empty():
            print("[]")
            return
        result = '['
        for i in range(self.front + 1, self.rear + 1):
            result += str(self.queue[i])
            if i != self.rear:
                result += ', '
        result += ']'
        print(result)


q = LinearQueue()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.enqueue('D')   
q.print_queue()

q.enqueue('E') 
q.print_queue()  

print(q.dequeue())  
q.print_queue()    

print(q.peek())    
print(q.size())   