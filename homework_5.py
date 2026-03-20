import flet as ft
import random

def main(page: ft.Page):
    page.title = "숫자 맞추기 게임"

    ran_num = random.randint(1, 100)
    chances = 5

    result_text = ft.Text()
    chance_text = ft.Text(f"남은 기회: {chances}")

    input_field = ft.TextField(label="숫자를 입력하세요", width=200)

    def check_answer(e):
        nonlocal ran_num, chances

        try:
            n = int(input_field.value)
        except:
            result_text.value = "숫자를 입력해주세요!"
            page.update()
            return

        if n == ran_num:
            result_text.value = "🎉 정답입니다!"
        else:
            chances -= 1

            if n > ran_num:
                result_text.value = "더 낮은 숫자!"
            else:
                result_text.value = "더 높은 숫자!"

            if chances <= 0:
                result_text.value = f"❌ 실패! 정답은 {ran_num}"
        
        chance_text.value = f"남은 기회: {chances}"
        page.update()

    def reset_game(e):
        nonlocal ran_num, chances
        ran_num = random.randint(1, 100)
        chances = 5
        result_text.value = ""
        chance_text.value = f"남은 기회: {chances}"
        input_field.value = ""
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text("숫자 맞추기 게임 (1~100)"),
                input_field,
                ft.Row([
                    ft.ElevatedButton("확인", on_click=check_answer),
                    ft.ElevatedButton("다시 시작", on_click=reset_game),
                ]),
                result_text,
                chance_text,
            ]
        )
    )

ft.run(main)