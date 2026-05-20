class Stack:

    # 객체 생성
    def __init__(self):
        self.MAX_SIZE = 10
        self.stack = [None]*self.MAX_SIZE
        self.size = 0

    def _print_error(self, code):
        messages = {
            "full"    : "스택이 가득 찼습니다.",
            "empty"   : "스택의 item이 비어있습니다.",
        }
        if code in messages:
            print(messages[code])

    def push(self, e):
        if self.size == self.MAX_SIZE:
            self._print_error("full")
            return
        
        self.stack[self.size] = e
        self.size += 1

    def pop(self):
        if self.size == 0:
            self._print_error("empty")
            return

        result = self.stack[self.size -1]
        self.stack[self.size -1] = None
        self.size -=1

        return result
    
    def isfull(self): return True if self.size == self.MAX_SIZE else False

    def isempty(self):
        return True if self.size == 0 else False
    
    def peek(self):
        if self.isempty():
            self._print_error("empty")
            return
        return self.stack[self.size-1]
    
    def check_size(self):
        return self.size