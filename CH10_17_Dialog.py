##  Dialog(대화상자)

from tkinter import *  # 파이썬 표준 윈도우 라이브러
from tkinter.simpledialog import *

## 함수 선언 ##
    
## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'
    window.geometry("400x100")

    label1 = Label(window, text = "입력된 값")
    label1.pack()

    # askinterger("제목", "내용", 옵션) - 정수를 받기 위해서..
    # askfloat("제목", "내용", 옵션) - 실수를 받기 위해서는 float 를 사용
    value = askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue = 1, maxvalue = 6)

    label1.config(text = str(value))

    window.mainloop()   # 화면 처리 부분이다.
