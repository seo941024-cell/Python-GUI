# BFS(너비 우선 탐색)를 이용한 미로 탐색 프로그램
# DFS(스택)와 달리 BFS는 큐를 사용해서 가까운 칸부터 순서대로 탐색합니다.
# 그래서 BFS는 항상 최단 경로를 찾을 수 있습니다.

class BFSMazeSolver:

    def __init__(self):
        # 미로 맵 정의
        # '1' = 벽  '0' = 이동 가능한 길  'e' = 시작점  'x' = 출구
        self.maze = [
            ['1', '1', '1', '1', '1', '1'],
            ['e', '0', '0', '0', '0', '1'],
            ['1', '0', '1', '0', '1', '1'],
            ['1', '1', '1', '0', '0', 'x'],
            ['1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1'],
        ]
        self.size = 6

        # 각 칸의 방문 여부를 저장하는 2차원 배열
        # 처음에는 전부 False (아직 방문 안 함)
        self.visited = [[False] * self.size for _ in range(self.size)]

        # 어느 칸에서 이 칸으로 왔는지 저장하는 딕셔너리
        # 나중에 경로를 역추적할 때 사용합니다
        self.parent = {}

    def find_start_and_exit(self):
        # 미로를 한 칸씩 확인하며 시작점(e)과 출구(x)의 위치를 찾습니다
        start = None
        exit_pos = None

        for r in range(self.size):
            for c in range(self.size):
                if self.maze[r][c] == 'e':
                    start = (r, c)
                elif self.maze[r][c] == 'x':
                    exit_pos = (r, c)

        return start, exit_pos

    def get_path(self, start, exit_pos):
        # 출구에서 시작점까지 부모 딕셔너리를 거슬러 올라가며 경로를 복원합니다
        path = []
        current = exit_pos

        while current != start:
            path.append(current)
            current = self.parent[current]  # 이전 칸으로 이동

        path.append(start)
        path.reverse()  # 출구 → 시작 순서를 시작 → 출구 순서로 뒤집기

        return path

    def solve(self):
        start, exit_pos = self.find_start_and_exit()

        if start is None or exit_pos is None:
            print("시작점(e) 또는 출구(x)를 찾을 수 없습니다.")
            return None

        # BFS에서 사용할 큐 (리스트로 구현)
        # 앞에서 꺼내고 뒤에 넣는 FIFO 방식입니다
        queue = []
        queue.append(start)

        # 시작점은 바로 방문 처리
        self.visited[start[0]][start[1]] = True

        while len(queue) > 0:

            # 큐의 맨 앞에서 꺼내기 (FIFO - 먼저 들어온 것이 먼저 나옴)
            current = queue.pop(0)
            r = current[0]
            c = current[1]

            print(f"현재 탐색 위치: ({r}, {c})")

            # 출구에 도달했으면 경로를 역추적해서 반환
            if (r, c) == exit_pos:
                path = self.get_path(start, exit_pos)
                print(f"\n출구 도착! 최단 경로: {path}")
                return path

            # 상하좌우 네 방향을 차례로 탐색
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # 미로 범위 안에 있는지 확인
                if 0 <= nr < self.size and 0 <= nc < self.size:
                    # 아직 방문하지 않았고 이동 가능한 칸인지 확인
                    if not self.visited[nr][nc] and self.maze[nr][nc] in ('0', 'x'):
                        self.visited[nr][nc] = True
                        self.parent[(nr, nc)] = (r, c)  # 이 칸의 부모(이전 칸)를 기록
                        queue.append((nr, nc))

        print("출구를 찾지 못했습니다.")
        return None

    def print_maze(self, path):
        # 경로를 '·'으로 표시하며 미로를 출력합니다
        symbols = {'1': '■', '0': '□', 'e': 'S', 'x': 'E'}

        for r in range(self.size):
            row = ''
            for c in range(self.size):
                # 경로에 포함된 칸이고 시작/출구가 아니면 '·' 표시
                if (r, c) in path and self.maze[r][c] not in ('e', 'x'):
                    row += '· '
                else:
                    row += symbols.get(self.maze[r][c], '?') + ' '
            print(row)


# 프로그램 실행
solver = BFSMazeSolver()
path = solver.solve()

if path is not None:
    print()
    print("[ 최단 경로가 표시된 미로 ]")
    solver.print_maze(path)
