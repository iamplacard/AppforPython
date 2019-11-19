##  File Dialog(대화상자)

from tkinter import *  # 파이썬 표준 윈도우 라이브러
from tkinter.filedialog import *

## 함수 선언 ##
    
## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'
    window.geometry("400x100")

    label1 = Label(window, text = "선택된 파일 이름")
    label1.pack()

    # asksaveasfile() -
    saveFp = asksaveasfile(parent = window, mode = 'w', defaultextension = ".jpg",
                           filetypes = (("JPG 파일", "*.jpg; *.jpeg"), ("모든 파일", "*.*")))

    label1.config(text = saveFp)
    saveFp.close()

    window.mainloop()   # 화면 처리 부분이다.
    
    # askopenfilename() - 경로를 포함해서 선택한 파일의 파일명을 반환한다.
'''
    filename = askopenfilename(parent = window, filetype = (("GIF 파일", "*.gif"),
                        ("모든 파일", "*.*")))

    label1.config(text = str(filename))
'''

