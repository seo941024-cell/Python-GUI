import tkinter

import random

def random_num():
    return random.randint(1,100)
target=random_num() #1,100까지의 숫자를 랜덤으로 추출하는 함수.
                    #그 랜덤 값을 target이라는 변수라고 지정.
print(target)

#updown game
'''정수를 입력.
    그 숫자가 1,100사이의 숫자인지 확인.
    맞을 시, 입력된 값이 random 수보다 높으면 Down하세요.
    낮으면 Up 하세요.출력
    정답이면 정답입니다! 와 함께, 한 번 더 할거면 Y, 아니면 N 입력
    Y 누를시 다시 1로 돌아감. 아니면 break.    '''
#지금 해야할 것 > 이걸 함수로 정의한다.

window=tkinter.Tk()
window.title("Up Down Game")
window.geometry("640x480+0+0")
window.resizable(True, True)

tkinter.Label(window, text="1부터 100까지 중 숫자를 입력해 주세요!!!",\
              width=500, relief="solid").pack()
answer_entry = tkinter.Entry(window)
answer_entry.pack()


window.mainloop()