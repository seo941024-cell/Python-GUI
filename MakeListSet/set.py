class Set:
    def __init__(self):
        self.MAX_SIZE = 10
        self.data = [None] * self.MAX_SIZE
        self.size = 0

    def _print_error(self, code):
        messages = {
            "full"    : "원소가 가득 찼습니다.",
            "pos"     : "위치 값을 다시 입력해주세요.",
            "empty"   : "리스트의 item이 비어있습니다.",
            "same"    : "중복된 값은 넣을 수 없습니다.",
            "notin"   : "존재하지 않는 원소입니다."
        }
        if code in messages:
            print(messages[code])

    def insert(self, e):
        if self.size == self.MAX_SIZE:
            self._print_error("full")
            return 
        
        for i in range(self.size) :
            if self.data[i] == e:
                self._print_error("same")
                return
            
        self.data[self.size] = e
        self.size +=1

    def delete(self, e):
        if self.size == 0:
            self._print_error("empty")
            return
        if not e in self.data:
            self._print_error("notin")
            return
        
        for i in range(self.size):
            if self.data[i] == e:
                self.data = self.data[:i] + self.data[i+1:] + [None]
                self.size -=1
                return e
            
    def isfull(self): return True if self.size==self.MAX_SIZE else False

    def isempty(self): return True if self.size==0 else False

    def union(self, setB):
        result = Set()
        for i in self.data[:self.size]:
            result.insert(i)
        for j in setB.data[:setB.size]:
            result.insert(j)  
        return result