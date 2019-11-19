## 그림판 만들기 
# 마우스로 그림을 그릴 수 있는 그림판 프로그램을 만들어 보자. 마우스를 클릭하고 드래그한 후
# 드롭하는 시점에 선이 그려지도록 한다. 색상과 두께는 메뉴에서 선택한다.

from tkinter import *  # 파이썬 표준 윈도우 라이브러
from tkinter.colorchooser import *
from tkinter.simpledialog import *

## 함수 선언 ##
def mouseClick(event) :
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

def mouseDrop(event) :
    global x1, y1, x2, y2, penWidth, penColor
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2, width = penWidth, fill = penColor)

def getColor() :
    global penColor
    color = askcolor()
    penColor = color[1]

def getWidth() :
    global penWidth
    penWidth = askinteger("선 두께", "선 두께(1~10)을 입력하세요",
                          minvalue = 1, maxvalue = 10)

## 전역 변수 선언 ##
window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None
penColor = 'black'
penWidth = 5

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'
    window.title("그림판 비슷한 프로그램")
    canvas = Canvas(window, height = 600, width = 600)
    canvas.bind("<Button-1>", mouseClick)
    canvas.bind("<ButtonRelease-1>", mouseDrop)
    canvas.pack()
    
    mainMenu = Menu(window)
    window.config(menu = mainMenu)

    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "설정", menu = fileMenu)
    fileMenu.add_command(label = "선 색상 선택", command = getColor)
    fileMenu.add_separator()
    fileMenu.add_command(label = "선 두께 설정", command = getWidth)

    window.mainloop()   # 화면 처리 부분이다.
    
