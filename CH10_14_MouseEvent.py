##  이전 버튼과 다음 버튼으로 사진을 표시하는 앨범

from tkinter import *  # 파이썬 표준 윈도우 라이브러
from tkinter import messagebox

## 함수 선언 ##
def clickMouse(event) :
    txt = ""
    if event.num == 1 :
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3 :
        txt += "마웃 오른쪽 버튼이 ("

    txt += str(event.y) + "," + str(event.x) +")에서 클릭됨"
    label1.configure(text = txt)
        
## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'

    window.geometry("400x400")

    label1 = Label(window, text = "이곳이 바뀜")
    window.bind("<Button>", clickMouse)

    label1.pack(expand = 1, anchor = CENTER)

    window.mainloop()   # 화면 처리 부분이다.
