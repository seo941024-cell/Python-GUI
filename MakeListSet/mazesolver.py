class MazeSolver:

    def __init__(self, size=6):
        self.size = size
        # 기본 미로 
        self.maze = [
            ['1','1','1','1','1','1'],
            ['e','0','0','0','0','1'],
            ['1','0','1','0','1','1'],
            ['1','1','1','0','x','1'],
            ['1','1','1','1','1','1'],
            ['1','1','1','1','1','1'],
        ]
        self.visited = [[False]*size for _ in range(size)]
        self.stack = []
        self.path = []  # 지나온 경로 저장

    def reset(self):
        self.visited = [[False]*self.size for _ in range(self.size)]
        self.stack = []
        self.path = []

    def _find_start_exit(self):
        start = exit = None
        for r in range(self.size):
            for c in range(self.size):
                if self.maze[r][c] == 'e':
                    start = (r, c)
                elif self.maze[r][c] == 'x':
                    exit = (r, c)
        return start, exit

    def solve(self, verbose=True):
        start, exit = self._find_start_exit()

        if not start or not exit:
            print("시작(e) 또는 출구(x)가 없습니다")
            return False

        self.stack.append(start)

        while self.stack:
            pos = self.stack.pop()
            r, c = pos

            if self.visited[r][c]:
                continue
            self.visited[r][c] = True
            self.path.append(pos)

            if verbose:
                print(f"현재 위치: {pos}")

            if pos == exit:
                print(f"\n출구 찾음! 경로: {self.path}")
                return True

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < self.size and
                    0 <= nc < self.size and
                    not self.visited[nr][nc] and
                    self.maze[nr][nc] in ('0','x')):
                    self.stack.append((nr, nc))

        print("출구 없음")
        return False

    def print_maze(self):
        symbols = {'1':'■', '0':'□', 'e':'S', 'x':'E'}
        for r in range(self.size):
            row = ''
            for c in range(self.size):
                if (r,c) in self.path:
                    row += '· '
                else:
                    row += symbols.get(self.maze[r][c], '?') + ' '
            print(row)



solver = MazeSolver()
solver.solve()
print()
solver.print_maze()