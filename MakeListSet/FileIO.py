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
        with open(self.filename, "r", encoding="utf-8") as f:
            f.close()
