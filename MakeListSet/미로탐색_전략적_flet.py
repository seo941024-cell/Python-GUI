import flet as ft
import asyncio

class VisualPriorityMazeSolver:
    def __init__(self, page: ft.Page):
        self.page = page
        
        # 유저님이 주신 새로운 맵 적용
        self.maze = [
            ['1','1','1','1','1','1'],
            ['e','0','0','0','0','1'],
            ['1','0','1','0','1','1'],
            ['1','1','1','0','0','x'],
            ['1','1','1','1','1','1'],
            ['1','1','1','1','1','1'],
        ]
        self.size = len(self.maze)
        
        # 알고리즘용 변수
        self.visited = [[False]*self.size for _ in range(self.size)]
        self.pq = [] # (우선순위, x, y)
        
        self.is_solving = False
        
        # UI 구성 요소
        self.cells = []  
        self.status_text = ft.Text("우선순위 큐 탐색 대기 중...", size=20, weight=ft.FontWeight.BOLD)
        self.solve_btn = ft.ElevatedButton("Solve (스마트 탐색)", on_click=self.solve, icon="play_arrow")
        self.reset_btn = ft.ElevatedButton("Reset (초기화)", on_click=self.reset, icon="refresh")

    # --- 유저님의 우선순위 큐 로직 그대로 이식 ---
    def _distance(self, r, c, exit_pos):
        er, ec = exit_pos
        return (r - er)**2 + (c - ec)**2

    def _enqueue(self, priority, r, c):
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
    # ---------------------------------------------

    def build_ui(self):
        grid_column = ft.Column(spacing=2)
        
        for r in range(self.size):
            row_controls = []
            row_cells = []
            for c in range(self.size):
                val = self.maze[r][c]
                bgcolor = ft.Colors.GREY_800 if val == '1' else ft.Colors.GREY_200
                text = ""
                
                if val == 'e':
                    bgcolor = ft.Colors.GREEN_500
                    text = "S"
                elif val == 'x':
                    bgcolor = ft.Colors.RED_500
                    text = "E"

                cell = ft.Container(
                    width=50, 
                    height=50,
                    bgcolor=bgcolor,
                    border_radius=5,
                    alignment=ft.Alignment.CENTER, 
                    content=ft.Text(text, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE if val in ('1','e','x') else ft.Colors.BLACK)
                )
                row_cells.append(cell)
                row_controls.append(cell)
                
            self.cells.append(row_cells)
            grid_column.controls.append(ft.Row(row_controls, spacing=2, alignment=ft.MainAxisAlignment.CENTER))

        return ft.Column(
            controls=[
                ft.Row([self.status_text], alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(height=10),
                grid_column,
                ft.Container(height=20),
                ft.Row([self.solve_btn, self.reset_btn], alignment=ft.MainAxisAlignment.CENTER)
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def reset(self, e=None):
        if self.is_solving:
            return  

        self.visited = [[False]*self.size for _ in range(self.size)]
        self.pq = []
        
        for r in range(self.size):
            for c in range(self.size):
                val = self.maze[r][c]
                if val == '1':
                    self.cells[r][c].bgcolor = ft.Colors.GREY_800
                elif val == '0':
                    self.cells[r][c].bgcolor = ft.Colors.GREY_200
                    self.cells[r][c].content.value = ""
                elif val == 'e':
                    self.cells[r][c].bgcolor = ft.Colors.GREEN_500
                elif val == 'x':
                    self.cells[r][c].bgcolor = ft.Colors.RED_500

        self.status_text.value = "미로가 초기화되었습니다."
        self.status_text.color = ft.Colors.WHITE
        self.page.update()

    def _find_start_exit(self):
        start = exit_pos = None
        for r in range(self.size):
            for c in range(self.size):
                if self.maze[r][c] == 'e':
                    start = (r, c)
                elif self.maze[r][c] == 'x':
                    exit_pos = (r, c)
        return start, exit_pos

    async def solve(self, e):
        if self.is_solving:
            return
            
        self.is_solving = True
        self.solve_btn.disabled = True
        self.reset_btn.disabled = True
        self.page.update()

        start, exit_pos = self._find_start_exit()

        if not start or not exit_pos:
            self.status_text.value = "시작(e) 또는 출구(x)가 없습니다"
            self.status_text.color = ft.Colors.RED_400
            self.page.update()
            self._finish_solve()
            return

        # 1. 시작점 거리를 계산하고 큐에 삽입
        d = self._distance(start[0], start[1], exit_pos)
        self._enqueue(d, start[0], start[1])

        while self.pq:
            # 2. 우선순위 큐에서 가장 출구와 가까운 노드 꺼내기
            current = self._dequeue()
            if not current:
                break
                
            priority, r, c = current

            if self.visited[r][c]:
                continue
                
            self.visited[r][c] = True

            # --- 시각화 연출: 현재 검사 중인 노드 (노란색) ---
            if self.maze[r][c] not in ('e', 'x'):
                self.cells[r][c].bgcolor = ft.Colors.YELLOW_400
            self.status_text.value = f"탐색 중... 출구까지 거리: {priority}"
            self.page.update()
            
            # 애니메이션 대기 시간 (0.3초)
            await asyncio.sleep(0.3) 

            # 출구 확인
            if (r, c) == exit_pos:
                self.status_text.value = "🎉 출구 도착! (똑똑한 경로 찾기 완료)"
                self.status_text.color = ft.Colors.GREEN_400
                self.page.update()
                self._finish_solve()
                return

            # --- 시각화 연출: 지나간 자리 (파란색) ---
            if self.maze[r][c] not in ('e', 'x'):
                self.cells[r][c].bgcolor = ft.Colors.BLUE_400
                self.cells[r][c].content.value = "·" 
            self.page.update()

            # 인접 노드 탐색 및 큐 삽입
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r+dr, c+dc
                if (0 <= nr < self.size and
                    0 <= nc < self.size and
                    not self.visited[nr][nc] and
                    self.maze[nr][nc] in ('0', 'x')):
                    
                    # 💡 핵심: 다음 위치에서 출구까지의 거리를 계산하여 삽입
                    d = self._distance(nr, nc, exit_pos)
                    self._enqueue(d, nr, nc)

        self.status_text.value = "❌ 출구가 없습니다."
        self.status_text.color = ft.Colors.RED_400
        self.page.update()
        self._finish_solve()

    def _finish_solve(self):
        self.is_solving = False
        self.solve_btn.disabled = False
        self.reset_btn.disabled = False
        self.page.update()


def main(page: ft.Page):
    page.title = "Priority Queue Maze Solver"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK 

    maze_app = VisualPriorityMazeSolver(page)
    page.add(maze_app.build_ui())

if __name__ == "__main__":
    ft.run(main)