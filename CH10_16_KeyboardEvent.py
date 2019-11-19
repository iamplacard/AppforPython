##  이전 버튼과 다음 버튼으로 사진을 표시하는 앨범

from tkinter import *  # 파이썬 표준 윈도우 라이브러
from tkinter import messagebox

## 함수 선언 ##
def keyEvent(event) :
    messagebox.showinfo(" 키보드 이벤트","눌린 키:" + chr(event.keycode))

## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'

    window.bind("<Key>", keyEvent)

    window.mainloop()   # 화면 처리 부분이다.
