class Node :
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedSet:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def contain(self, e):
        current = self.head
        while current:
            if current.data == e:
                return True
            current = current.next
        return False
    
    def insert(self, e):
        if self.contain(e):
            print("이미 존재하는 item입니다.")
            return
        new_node = Node(e)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, e):
        if self.size == 0:
            print("set이 비어있습니다.")
            return
        
        prev = None
        current = self.head
        while current:
            if current.data == e:
                if prev is None:
                    self.head = current.next
                else :
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        
        print("존재하지 않는 item입니다.")

    # def isfull(self):

    def isempty(self) : return True if self.size == 0 else False

    def union(self, setB):
        result = LinkedSet()
        
        return result

'''• Contain(e): 집합이 원소 e를 포함하는지 검사한다
• Insert(e): 새로운 원소 e를 삽입한다. (중복 삽입은 허용안함)
• Delete(e): 원소 e를 집합에서 꺼내고(삭제) 반환한다
• IsFull(): 집합이 가득 차 있는지를 검사한다
• isEmpty(): 공집합인지 검사한다
• Union(setB): setB와 합집합을 만들어 반환한다
• intersect(setB): setB와 교집합을 만들어 반환한다
• Difference(setB): setB와 차집합을 만들어 반환한다
• Equals(setB): setB와 같은 집합인지를 검사한다
• Size(): 집합의 원소의 개수를 반환한다
• Display(): 리스트를 화면에 출력한다'''