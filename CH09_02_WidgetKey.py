##  위젯의 배치와 크기 조절을 확인한다. pack() / place() / configure()

from tkinter import *  # 파이썬 표준 윈도우 라이브러
import random

## 함수 선언 ##
def myFunc() :
    messagebox.showinfo("Beanbird", "Beanbird가 귀엽죠? ^^")

    
## 변수 선언 ##
fnameList = ["Afro.gif", "beehive.gif", "Combover.gif", "dreadlocks.gif",
            "Sure.gif", "surf.gif", "SVL.gif", "winter.gif", "zzz.gif"]
photoList = [None]*9
i,k = 0, 0
xPos, yPos = 0,0
num = 0

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'
    
    window.title("윈도우")
    window.geometry("1000x1000")
#    window.resizable(width = FALSE, height = FALSE)

    button1 = Button(window, text = "버튼1")
    button2 = Button(window, text = "버튼2")
    button3 = Button(window, text = "버튼3")

    button1.pack(side = LEFT)
    button2.pack(side = LEFT)
    button3.pack(side = LEFT)

    btnList = [None]*3

    for i in range(0,3) :
        btnList[i] = Button(window, text = "버튼" + str(i+1))

    for btn in btnList :
        btn.pack(side = RIGHT)  # TOP / BOTTOM / LEFT
    for btn in btnList :
        btn.pack(side = RIGHT, fill = X)  # fill = X 는 폭 조정 윈도우 창에 맞추기
    
    for btn in btnList :
        btn.pack(side = RIGHT, fill = X, padx = 10, pady = 10)  # 위젯 사이에 여백 주기   padx = 10, pady = 10

    for btn in btnList :
        btn.pack(side = RIGHT, fill = X, padx = 10, pady = 10, ipadx = 10, ipady = 10)  # 위젯내부의 여백 주기   ipadx = 10, ipady = 10

    #   이미지 button 을 정렬하여 두자. 
    btnList = [None]*9

    for i in range(0,9) :
        photoList[i] = PhotoImage(file = "picture/" + fnameList[i])
        btnList[i] = Button(window, image = photoList[i])

    random.shuffle(btnList)

    for i in range(0,3) :
        for k in range(0,3) :
            btnList[num].place(x = xPos, y = yPos)  # pack 을 대신하여 place 를 사용하여 그릴 위치를 지정한다.
            num += 1
            xPos += 200
        xPos = 0
        yPos += 200

    window.mainloop()   # 화면 처리 부분이다.
