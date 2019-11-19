##  메뉴의 구성
#   메뉴 자체 = Menu(부모윈도)
#   부모 윈도.config(menu = 메뉴 자체)
#
#   상위메뉴 = Menu(메뉴자체)
#   메뉴자체.add_cascade(label = "상위메뉴텍스트", menu = 상위메뉴)
#   상위메뉴.add_command(label = "하위메뉴1", command = 함수1)
#   상위메뉴.add_command(label = "하위메뉴2", command = 함수2)

from tkinter import *  # 파이썬 표준 윈도우 라이브러
from tkinter import messagebox

## 함수 선언 ##
def func_open() :
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")
    
def func_exit() :
    window.quit()
    window.destroy()
    
## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'

    mainMenu = Menu(window)
    window.config(menu = mainMenu)

    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label = "파일", menu = fileMenu)
    fileMenu.add_command(label = "열기", command = func_open)
    fileMenu.add_separator()
    fileMenu.add_command(label = "종료", command = func_exit )

    window.mainloop()   # 화면 처리 부분이다.
