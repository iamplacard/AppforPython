##  이전 버튼과 다음 버튼으로 사진을 표시하는 앨범

from tkinter import *  # 파이썬 표준 윈도우 라이브러
from tkinter import messagebox

## 함수 선언 ##
def clickLeft(event) :
    messagebox.showinfo('마우스', '마우스 왼쪽 버튼이 클릭됨')

def clickImage(event) :
    messagebox.showinfo('마우스', 'Beehive Image 에서 마우스가 클릭됨 ')

 
## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'

    # window에 binding 을 하여 window 내에서 click 하였을 때 동작한다. 
    window.bind("<Button-1>", clickLeft)

    window.geometry("400x400")

    photo = PhotoImage(file = "picture/beehive.gif")
    label = Label(window, image = photo)
    label.bind("<Button-1>", clickImage)
    label.pack(expand = 1,anchor =CENTER)

    window.mainloop()   # 화면 처리 부분이다.
