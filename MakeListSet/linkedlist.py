class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return False

    def _get_node(self, pos):
        n = self.head
        for _ in range(pos):
            if n is None:
                return None
            n = n.link
        return n

    def insert(self, pos, e):
        if pos == 0:
            self.head = Node(e, self.head)
        else:
            prev = self._get_node(pos - 1)
            if prev is None:
                return
            prev.link = Node(e, prev.link)

    def delete(self, pos):
        if self.is_empty():
            return None
        if pos == 0:
            item = self.head.data
            self.head = self.head.link
            return item
        prev = self._get_node(pos - 1)
        if prev is None or prev.link is None:
            return None
        item = prev.link.data
        prev.link = prev.link.link
        return item

    def get_entry(self, pos):
        n = self._get_node(pos)
        return n.data if n else None

    def replace(self, pos, item):
        n = self._get_node(pos)
        if n:
            n.data = item

    def find(self, item):
        n = self.head
        idx = 0
        while n is not None:
            if n.data == item:
                return idx
            n = n.link
            idx += 1
        return -1

    def size(self):
        n, count = self.head, 0
        while n is not None:
            n = n.link
            count += 1
        return count

    def clear(self):
        self.head = None

    def append(self, e):
        if self.is_empty():
            self.head = Node(e)
        else:
            n = self.head
            while n.link is not None:
                n = n.link
            n.link = Node(e)

    def merge(self, lst):
        n = lst.head
        while n is not None:
            self.append(n.data)
            n = n.link

    def sort(self):
        if self.is_empty():
            return
        changed = True
        while changed:
            changed = False
            n = self.head
            while n.link is not None:
                if n.data > n.link.data:
                    n.data, n.link.data = n.link.data, n.data
                    changed = True
                n = n.link

    def display(self):
        n = self.head
        result = 'head → '
        while n is not None:
            result += str(n.data)
            if n.link is not None:
                result += ' → '
            n = n.link
        print(result + ' → None')


# 테스트
ll = LinkedList()

ll.append('A'); ll.append('B'); ll.append('C'); ll.append('D')
ll.display()            # head → A → B → C → D → None

ll.insert(0, 'Z')
ll.display()            # head → Z → A → B → C → D → None

ll.insert(2, 'X')
ll.display()            # head → Z → A → X → B → C → D → None

print(ll.delete(0))     # Z
print(ll.get_entry(1))  # X
print(ll.find('C'))     # 3
print(ll.size())        # 5

ll.replace(0, 'K')
ll.display()            # head → K → X → B → C → D → None

ll2 = LinkedList()
ll2.append('E'); ll2.append('F')
ll.merge(ll2)
ll.display()            # head → K → X → B → C → D → E → F → None

ll.sort()
ll.display()            # head → B → C → D → E → F → K → X → None