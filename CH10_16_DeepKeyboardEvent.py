##  이전 버튼과 다음 버튼으로 사진을 표시하는 앨범

from tkinter import *  # 파이썬 표준 윈도우 라이브러
from tkinter import messagebox

## 함수 선언 ##
def keyEvent(event) :
    if event.keycode == 37 :
        messagebox.showinfo(" 키보드 이벤트","눌린 키: Shift +왼쪽 화살표 ==> " + chr(event.keycode))
    elif event.keycode == 38 :
        messagebox.showinfo(" 키보드 이벤트","눌린 키: Shift +위쪽 화살표 ==> " + chr(event.keycode))
    elif event.keycode == 39 :
        messagebox.showinfo(" 키보드 이벤트","눌린 키: Shift +오른쪽 화살표 ==> " + chr(event.keycode))
    elif event.keycode == 40 :
        messagebox.showinfo(" 키보드 이벤트","눌린 키: Shift +아래쪽 화살표 ==> " + chr(event.keycode))

    print(" Key Code Value : %d" %event.keycode)

## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'

    window.bind("<Shift-Up>", keyEvent)
    window.bind("<Shift-Down>", keyEvent)
    window.bind("<Shift-Left>", keyEvent)
    window.bind("<Shift-Right>", keyEvent)

    window.mainloop()   # 화면 처리 부분이다.
