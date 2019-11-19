## 좋아하는 동물 투표
from tkinter import *  # 파이썬 표준 윈도우 라이브러

## 함수 선언 ##
def myFunc() :
    if var.get() == 1 :
        labelImage.configure(image = photo1)
    elif var.get() == 2 :
        labelImage.configure(image = photo2)
    else :
        labelImage.configure(image = photo3)

## 전역 변수 선언 ##
var, labelImage = 0, None
photo1, photot2, photot3 = [None]*3

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'
    window.geometry("400x400")
    window.title("webOS Icon 선택하")
    labelText = Label(window, text = "webOS Icon 선택하기", fg = "blue",
                      font = ("궁서체", 20))

    var = IntVar()
    rb1 = Radiobutton(window, text = "Beehive", variable = var, value = 1)
    rb2 = Radiobutton(window, text = "Combover", variable = var, value = 2)
    rb3 = Radiobutton(window, text = "LGwebOS", variable = var, value = 3)
    buttonOK = Button(window, text = "사진 보기", command = myFunc)

    photo1 = PhotoImage(file = "picture/beehive.gif")
    photo2 = PhotoImage(file = "picture/combover.gif")
    photo3 = PhotoImage(file = "picture/LGwebOS.gif")

    labelImage = Label(window, width = 200, height = 200, bg = "yellow", image = None)

    labelText.pack(padx = 5, pady = 5)
    rb1.pack(padx = 5, pady = 5)
    rb2.pack(padx = 5, pady = 5)
    rb3.pack(padx = 5, pady = 5)
    buttonOK.pack(padx = 5, pady = 5)
    labelImage.pack(padx = 5, pady = 5)

    window.mainloop()   # 화면 처리 부분이다.
    
