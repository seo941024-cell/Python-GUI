# 덱(Deque) 클래스 - 원형 큐를 상속받아 구현
# 덱은 앞(front)과 뒤(rear) 양쪽에서 삽입/삭제가 모두 가능한 자료구조입니다.
# ArrayQueue(원형 큐)를 부모 클래스로 상속받아, 큐의 기능을 그대로 재사용합니다.

from 원형큐_클래스 import ArrayQueue  # 원형큐_클래스.py 에서 원형 큐 클래스를 가져옵니다


class Deque(ArrayQueue):
    # ArrayQueue 를 상속받으므로 is_full, is_empty, size, clear 는
    # 부모 클래스 것을 그대로 사용합니다.

    def add_rear(self, e):
        # 덱의 맨 뒤(rear)에 요소를 추가합니다 (큐의 enqueue 와 동일)
        if self.is_full():
            print("overflow - 덱이 가득 찼습니다")
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = e
        return True

    def delete_front(self):
        # 덱의 맨 앞(front)에서 요소를 꺼냅니다 (큐의 dequeue 와 동일)
        if self.is_empty():
            print("underflow - 덱이 비어 있습니다")
            return None
        self.front = (self.front + 1) % self.capacity
        item = self.queue[self.front]
        self.queue[self.front] = None
        return item

    def add_front(self, e):
        # 덱의 맨 앞(front)에 요소를 추가합니다 (일반 큐에는 없는 덱만의 기능)
        if self.is_full():
            print("overflow - 덱이 가득 찼습니다")
            return False
        self.queue[self.front] = e
        self.front = (self.front - 1 + self.capacity) % self.capacity
        return True

    def delete_rear(self):
        # 덱의 맨 뒤(rear)에서 요소를 꺼냅니다 (일반 큐에는 없는 덱만의 기능)
        if self.is_empty():
            print("underflow - 덱이 비어 있습니다")
            return None
        item = self.queue[self.rear]
        self.queue[self.rear] = None
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return item

    def get_front(self):
        # 앞(front) 요소를 삭제하지 않고 확인만 합니다
        if self.is_empty():
            return None
        return self.queue[(self.front + 1) % self.capacity]

    def get_rear(self):
        # 뒤(rear) 요소를 삭제하지 않고 확인만 합니다
        if self.is_empty():
            return None
        return self.queue[self.rear]


# ============================================================
# 테스트
# ============================================================

print("=== Deque 테스트 ===")

d = Deque(capacity=10)

# 뒤쪽에 추가
d.add_rear('B')
d.add_rear('C')
d.add_rear('D')

# 앞쪽에 추가
d.add_front('A')

print(f"앞 요소 확인: {d.get_front()}")   # A
print(f"뒤 요소 확인: {d.get_rear()}")    # D
print(f"현재 크기: {d.size()}")           # 4

print(f"앞에서 꺼내기: {d.delete_front()}")  # A
print(f"뒤에서 꺼내기: {d.delete_rear()}")   # D
print(f"남은 크기: {d.size()}")              # 2

print(f"앞 요소 확인: {d.get_front()}")   # B
print(f"뒤 요소 확인: {d.get_rear()}")    # C
