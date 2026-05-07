class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedStack:

    def __init__(self):
        self.top = None

    def is_full(self):
        return False

    def is_empty(self):
        return self.top is None

    def push(self, e):
        self.top = Node(e, self.top)

    def pop(self):
        if self.is_empty():
            return None
        item = self.top.data
        self.top = self.top.link
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def size(self):
        n, count = self.top, 0
        while n is not None:
            n = n.link
            count += 1
        return count

    def clear(self):
        self.top = None

    def print_stack(self):
        n = self.top
        result = 'top → '
        while n is not None:
            result += str(n.data)
            if n.link is not None:
                result += ' → '
            n = n.link
        print(result + ' → None')