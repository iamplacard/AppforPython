##  이전 버튼과 다음 버튼으로 사진을 표시하는 앨범

from tkinter import *  # 파이썬 표준 윈도우 라이브러
from time import *

## 함수 선언 ##
def clickNext() :
    global num
    num += 1
    if num > 8 :
        num = 0
    photo = PhotoImage(file = "picture/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo

def clickPrev() :
    global num
    num -= 1
    if num < 0 :
        num = 8
    photo = PhotoImage(file = "picture/" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    
    
## 변수 선언 ##
fnameList = ["Afro.gif", "beehive.gif", "Combover.gif", "dreadlocks.gif",
            "Sure.gif", "surf.gif", "SVL.gif", "winter.gif", "zzz.gif"]
photoList = [None]*9
num = 0

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'
    
    window.title("윈도우 사진 앨범 보기")
    window.geometry("1000x1000")
#    window.resizable(width = FALSE, height = FALSE)

    btnPrev = Button(window, text = "<< 이전", command = clickPrev)
    btnNext = Button(window, text = ">> 다음", command = clickNext)

    photo = PhotoImage(file = "picture/" + fnameList[0])
    pLabel = Label(window, image = photo)
    tLabel = Label(window, text = "webOS Beanbird")

    btnPrev.place(x = 400, y = 10)
    btnNext.place(x = 600, y = 10)
    pLabel.place(x = 15, y = 50)
    tLabel.place(x = 480, y = 10)

    window.mainloop()   # 화면 처리 부분이다.
