class PriorityQueue:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity  # (우선순위, 데이터) 튜플로 저장
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e, priority):
        if self.is_full():
            print("overflow")
            return False

        # 우선순위 높은 순(숫자 작을수록 높음)으로 정렬해서 삽입
        i = self.size - 1
        while i >= 0 and self.queue[i][0] > priority:
            self.queue[i + 1] = self.queue[i]  # 한 칸씩 뒤로 밀기
            i -= 1
        self.queue[i + 1] = (priority, e)
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("underflow")
            return None
        item = self.queue[0]           # 맨 앞 = 가장 높은 우선순위
        for i in range(self.size - 1):
            self.queue[i] = self.queue[i + 1]
        self.queue[self.size - 1] = None
        self.size -= 1
        return item[1]                 # 데이터만 반환

    def peek(self):
        if self.is_empty(): return None
        return self.queue[0][1]

    def clear(self):
        for i in range(self.capacity):
            self.queue[i] = None
        self.size = 0

    def print_queue(self):
        if self.is_empty():
            print("[]")
            return
        result = '['
        for i in range(self.size):
            p, e = self.queue[i]
            result += f"{e}(p{p})"
            if i != self.size - 1:
                result += ', '
        result += ']'
        print(result)


pq = PriorityQueue()

pq.enqueue('환자C', 3)
pq.enqueue('환자A', 1)  
pq.enqueue('환자D', 3)
pq.enqueue('환자B', 2)
pq.print_queue()        

print(pq.dequeue())     
print(pq.dequeue())      
pq.print_queue()        
print(pq.peek())         
print(pq.size)         