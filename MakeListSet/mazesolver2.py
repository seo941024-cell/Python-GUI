class PriorityMazeSolver:

    def __init__(self, maze):
        self.maze = maze
        self.size = len(maze)
        self.visited = [[False]*self.size for _ in range(self.size)]
        self.pq = []  # (우선순위, x, y) → 거리가 작을수록 먼저

    def _distance(self, r, c, exit):
        er, ec = exit
        # 유클리드 거리 (루트 없이 제곱으로만 비교해도 됨)
        return (r - er)**2 + (c - ec)**2

    def _enqueue(self, priority, r, c):
        # 우선순위 작은 게 앞으로 (거리 가까울수록 우선)
        item = (priority, r, c)
        i = len(self.pq) - 1
        self.pq.append(item)
        while i >= 0 and self.pq[i][0] > self.pq[i+1][0]:
            self.pq[i], self.pq[i+1] = self.pq[i+1], self.pq[i]
            i -= 1

    def _dequeue(self):
        if not self.pq:
            return None
        item = self.pq[0]
        for i in range(len(self.pq) - 1):
            self.pq[i] = self.pq[i+1]
        self.pq.pop()
        return item

    def solve(self, start, exit):
        d = self._distance(start[0], start[1], exit)
        self._enqueue(d, start[0], start[1])

        while self.pq:
            _, r, c = self._dequeue()

            if self.visited[r][c]:
                continue
            self.visited[r][c] = True

            print(f"현재 위치: ({r},{c})  출구까지 거리: {self._distance(r,c,exit)}")

            if (r, c) == exit:
                print("출구 찾음!")
                return True

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < self.size and
                    0 <= nc < self.size and
                    not self.visited[nr][nc] and
                    self.maze[nr][nc] in ('0','x')):
                    d = self._distance(nr, nc, exit)
                    self._enqueue(d, nr, nc)  # 거리가 우선순위

        print("출구 없음")
        return False


# 테스트
map = [
    ['1','1','1','1','1','1'],
    ['e','0','0','0','0','1'],
    ['1','0','1','0','1','1'],
    ['1','1','1','0','0','x'],
    ['1','1','1','1','1','1'],
    ['1','1','1','1','1','1'],
]

solver = PriorityMazeSolver(map)
solver.solve(start=(1,0), exit=(3,5))