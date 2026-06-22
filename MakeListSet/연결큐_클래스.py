# ============================================================
# 2. 연결 구조 기반 Queue (Linked Queue)
# ============================================================

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, e):
        node = Node(e)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self._size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("underflow")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def size(self):
        return self._size

    def clear(self):
        self.front = None
        self.rear = None
        self._size = 0


print("\n=== LinkedQueue ===")
lq = LinkedQueue()
lq.enqueue('A'); lq.enqueue('B'); lq.enqueue('C')
print(lq.peek())        # A
print(lq.size())        # 3
print(lq.dequeue())     # A
print(lq.dequeue())     # B
print(lq.size())        # 1