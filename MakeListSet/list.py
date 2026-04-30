class MyList:
    # 객체 생성
    def __init__(self):
        self.MAX_SIZE = 10
        self.my_list = [None]*self.MAX_SIZE
        self.size = 0

    # 객체 출력 형식 지정
    # 정의 안할 시, 출력이 <__main__.MyList object at 0x0000023A0E3F8590>
    def __str__(self):
        return str(self.my_list)
    
    # 오류 출력용 dictionary 
    def _print_error(self, code):
        messages = {
            "full"    : "리스트가 가득 찼습니다.",
            "pos"     : "위치 값을 다시 입력해주세요.",
            "empty"   : "리스트의 item이 비어있습니다.",
        }
        if code in messages:
            print(messages[code])

    # insert 
    def insert(self, pos, e):
        # 리스트의 item의 개수가 MAX_SIZE 를 넘을 때 
        if self.size >= self.MAX_SIZE:
            self._print_error("full")
            return
        # 순차적으로 list가 쌓이는 구조
        if pos < 0 or pos > self.size:
            self._print_error("pos")
            return

        #입력된 pos 이후 요소들을 한 칸씩 뒤로 이동
        for i in range(self.size, pos, -1):
            self.my_list[i] = self.my_list[i-1]

        self.my_list[pos] = e
        self.size += 1
    
    # delete
    def delete(self, pos):
        if self.size <= 0:
            self._print_error("empty")
            return

        if pos < 0 or pos >= self.size:
            self._print_error("pos")
            return
        
        deleted = self.my_list[pos]

        for i in range(pos, self.size -1):
            self.my_list[i] = self.my_list[i+1]

        self.my_list[self.size -1] = None 
        self.size -= 1

        return deleted
    
    def isfull(self):
        return self.size == self.MAX_SIZE
    
    #
    def isempty(self):
        return self.size == 0
    
    def getEntry(self, pos):
        if pos < 0 or pos >= self.size:
            self._print_error("pos")
            return None

        return self.my_list[pos]
    
    def get_size(self):
        return self.size
    
    def clear(self):
        self.size = 0
   
    '''def Make_Clear2(self):
        for i in range(self.size):
            self.my_list[i] = None
        self.size = 0
        return''' 
    
    def find(self, item): 
        for i in range(self.size):
            if self.my_list[i] == item:
                return i
        return None
    
    def replace(self, pos, item):
        if pos < 0 or pos >= self.size:
            self._print_error("pos")
            return
        self.my_list[pos] = item 

    def sort(self):
        #값을 비교할 수 있을때 가장 작은 순서부터, 큰 순서대로 나열
        for i in range(self.size):
             for j in range(0, self.size - i - 1):
                if self.my_list[j] > self.my_list[j + 1]:
                    self.my_list[j], self.my_list[j + 1] = self.my_list[j + 1], self.my_list[j]     

    # 만들어둔 insert 활용           
    def append(self, e):
        self.insert(self.size, e)

    def display(self):
        if self.size == 0:
            self._print_error("empty")
            return
        print(self.my_list[:self.size])

    '''def merge(self, other_list):
        for i in other_list:
            self.append(i)'''

#테스트용 list 선언 / isfull확인용 templist
testlist = MyList()
templist = MyList()
print(testlist)

#insert============== =====
testlist.insert(0, 1)
testlist.insert(1, 2)
testlist.insert(3, 3) #error 확인
testlist.insert(2, 3)
testlist.insert(3, 4)
testlist.insert(4, 5)
testlist.insert(5, 6)
testlist.insert(6, 7)
testlist.insert(7, 8)
testlist.insert(8, 9)
testlist.insert(9, 10)
print(testlist)

#delete====================
testlist.delete(1)
print(testlist)

#isfull====================
for i in range(10):
    templist.insert(i, i)
print(templist.isfull())

#isempty===================
print(testlist.isempty())
testlist.delete(1)
testlist.delete(1)
testlist.delete(1)
testlist.delete(1)
testlist.delete(1)
testlist.delete(1)
testlist.delete(1)
testlist.delete(1)
testlist.delete(0)
print(testlist.isempty())

#getEntry==================
print(templist.getEntry(3))
print(templist.getEntry(9))

#getEntry / item is None===
print(testlist.getEntry(0))