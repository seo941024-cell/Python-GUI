class FileIO:
    def __init__ (self):
        self.filename = "text.txt" #파일 생성
        self.line_num = [] #라인 번호로 관리

    def i (self, line_no, text):
        self.line_num = self.line_num[:line_no -1] + [text] + self.line_num[line_no -1:]
        
    def d (self, line_no): self.line_num = self.line_num[:line_no -1] + self.line_num[line_no:]
    
    def r (self, line_no, text): self.line_num[line_no -1] = text

    def p (self):
        i = 1
        for value in self.line_num:
            print(f"{i}: {value}")
            i += 1

    def l(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                self.line_num = self.line_num + [line]

    def s(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for line in self.line_num:
                f.write(line)

    def q(self):
        print("종료합니다.")
        exit()

f = FileIO()

# 삽입
print("=== insert ===")
f.i(1, "첫번째 줄\n")
f.i(2, "두번째 줄\n")
f.i(3, "세번째 줄\n")
f.p()

# 중간 삽입
print("\n=== 2번째 줄에 삽입 ===")
f.i(2, "중간 삽입\n")
f.p()

# 수정
print("\n=== 1번째 줄 수정 ===")
f.r(1, "수정된 첫번째 줄\n")
f.p()

# 저장
print("\n=== 저장 ===")
f.s()

# 불러오기
print("\n=== 불러오기 ===")
f2 = FileIO()
f2.l()
f2.p()

# 삭제
print("\n=== 2번째 줄 삭제 ===")
f.d(2)
f.p()

# 종료
print("\n=== 종료 ===")
f.q()