# 🎳 Bowling Score Board (Python + Flet)

## 📌 프로젝트 소개

이 프로젝트는 Python과 Flet을 활용하여 구현한 **볼링 점수판 GUI 프로그램**입니다.
사용자의 투구 결과를 입력받아 **실시간으로 프레임 점수와 누적 점수**를 시각적으로 표시합니다.

---

## 🚀 주요 기능

* 🎯 투구 입력 (핀 개수 입력)
* 📊 실시간 점수 계산 및 누적 점수 표시
* 🎳 스트라이크 / 스페어 자동 판별
* 🧾 프레임별 점수 시각화
* 🏁 게임 종료 시 최종 점수 출력

---

## 🛠️ 사용 기술

* **Python 3**
* **Flet (GUI Framework)**
* 객체지향 프로그래밍 (OOP)

---

## 📂 프로젝트 구조

```id="p1"
📦 Bowling-Score-Board
 ┣ 📜 main.py              # Flet UI 및 이벤트 처리
 ┣ 📜 bowling_func.py      # 볼링 점수 계산 로직 (BowlingGame 클래스)
 ┣ 📜 README.md
 ┗ 📜 requirements.txt
```

---

## 🧠 핵심 로직 설명

### 🎳 BowlingGame 클래스

* `throw_list`를 기반으로 투구 기록 저장
* 스트라이크 / 스페어 규칙에 맞게 점수 계산
* 프레임별 누적 점수 반환

### 클래스 코드 ###
```python
class BowlingGame:
    def __init__(self):
        self.throw_list = []

    # ================= 점수 계산 =================
    def calculate_live_scores(self):
        scores = []
        total = 0
        i = 0

        for _ in range(10):
            if i >= len(self.throw_list):
                break

            # 스트라이크
            if self.throw_list[i] == 10:
                if i + 2 >= len(self.throw_list):
                    break
                total += 10 + self.throw_list[i+1] + self.throw_list[i+2]
                scores.append(total)
                i += 1

            # 스페어 / 일반
            else:
                if i + 1 >= len(self.throw_list):
                    break

                if self.throw_list[i] + self.throw_list[i+1] == 10:
                    if i + 2 >= len(self.throw_list):
                        break
                    total += 10 + self.throw_list[i+2]
                else:
                    total += self.throw_list[i] + self.throw_list[i+1]

                scores.append(total)
                i += 2

        return scores

    # ================= 화면 출력 =================
    def show_display(self):
        display_score = []
        i = 0

        for frame in range(10):
            if i >= len(self.throw_list):
                display_score.append(" ")
                continue

            # ================= 10프레임 =================
            if frame == 9:
                result = []
                roll_in_frame = 0  # ⭐ 핵심

                while i < len(self.throw_list):
                    val = self.throw_list[i]

                    # 스트라이크
                    if val == 10:
                        result.append("❌")
                        i += 1
                        roll_in_frame += 1
                        continue

                    if i + 1 < len(self.throw_list):
                        nxt = self.throw_list[i + 1]

                        # ⭐ 2번째 투구일 때만 스페어 허용
                        if roll_in_frame == 1 and val + nxt == 10:
                            result.append(str(val))
                            result.append("/")
                            i += 2
                            roll_in_frame += 2
                            continue

                    # 일반
                    result.append("-" if val == 0 else str(val))
                    i += 1
                    roll_in_frame += 1

                display_score.append(" ".join(result))

            # ================= 일반 프레임 =================
            else:
                # 스트라이크
                if self.throw_list[i] == 10:
                    display_score.append("❌")
                    i += 1

                else:
                    if i + 1 < len(self.throw_list):

                        first = self.throw_list[i]
                        second = self.throw_list[i+1]

                        # 스페어
                        if first + second == 10:
                            a = "-" if first == 0 else str(first)
                            display_score.append(f"{a} /")
                        else:
                            a = "-" if first == 0 else str(first)
                            b = "-" if second == 0 else str(second)
                            display_score.append(f"{a} {b}")

                        i += 2
                    else:
                        display_score.append("-" if self.throw_list[i] == 0 else str(self.throw_list[i]))
                        i += 1

        return display_score

    # ================= 보드 출력 =================
    def print_live_board(self):
        frames = self.show_display()
        scores = self.calculate_live_scores()

        print("\n======================================")
        print("프레임:", " | ".join(frames))

        score_line = []
        for i in range(10):
            if i < len(scores):
                score_line.append(f"{scores[i]:3}")
            else:
                score_line.append("   ")

        print("점수  :", " | ".join(score_line))
        print("======================================\n")

    # ================= 투구 추가 =================
    def add_throw(self, pins):
        self.throw_list.append(pins)
        self.print_live_board()
```

### 📊 실시간 점수 처리

* 투구 시마다 `add_throw()` 실행
* UI 즉시 업데이트
* `calculate_live_scores()`로 누적 점수 반영

---

## ▶️ 실행 방법

### 1️⃣ 패키지 설치

```id="p2"
pip install flet
```

### 2️⃣ 실행

```id="p3"
python main.py
```

---

## 💡 실행 화면

* 프레임별 점수 박스 UI
* 점수 누적 표시
* 입력창 + 투구 버튼
  
![preview](https://raw.githubusercontent.com/seo941024/Python/master/flet/bowling.png)
---

## 📖 학습 포인트

* 이벤트 기반 GUI 프로그래밍
* 클래스 기반 로직 분리 (UI vs Logic)
* 리스트 및 조건문을 활용한 상태 관리
* 실시간 데이터 업데이트 처리

---

## ✨ 향후 개선 사항

* 🎨 UI 애니메이션 (스트라이크 효과 등)
* 🎮 자동 랜덤 투구 모드 추가 / 현재 코드 구현 완료. GUI 미적용
* 📈 점수 그래프 시각화
* 💾 게임 기록 저장 기능

---

## 👤 작성자

* 이름: 서지섭
* GitHub: https://github.com/seo941024

---
