# 노드 클래스 - 데이터와 다음 노드를 가리키는 링크로 구성
class Node:

    def __init__(self, data, link=None):
        self.data = data   # 저장할 데이터
        self.link = link   # 다음 노드를 가리키는 링크


class Stack:

    # 객체 생성
    def __init__(self):
        self.top = None  # 스택의 최상단 노드를 가리킴 (처음엔 비어있음)
        self.size = 0    # 현재 스택에 들어있는 요소 수

    def _print_error(self, code):
        messages = {
            "full"  : "스택이 가득 찼습니다.",
            "empty" : "스택의 item이 비어있습니다.",
        }
        if code in messages:
            print(messages[code])

    def push(self, e):
        # 새 노드를 만들어 현재 top 위에 연결하고, top을 새 노드로 변경
        new_node = Node(e, self.top)
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            self._print_error("empty")
            return

        # top 노드의 데이터를 꺼내고, top을 그 다음 노드로 이동
        result = self.top.data
        self.top = self.top.link
        self.size -= 1

        return result

    def isfull(self):
        # 연결 구조는 메모리가 허용하는 한 무한히 추가 가능하므로 항상 False
        return False

    def isempty(self):
        return True if self.size == 0 else False

    def peek(self):
        if self.isempty():
            self._print_error("empty")
            return
        # top 노드의 데이터를 삭제 없이 반환
        return self.top.data

    def check_size(self):
        return self.size
