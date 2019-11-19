##  기본 위젯 활용
#   위젯은 윈도우 창에 나올 수 있는 문자, 버튼, 체크박스,
#   라디오 버튼 등을 의미한다.

from tkinter import *  # 파이썬 표준 윈도우 라이브러
from tkinter import messagebox

## 함수 선언 ##
def myFunc() :
    messagebox.showinfo("Beanbird", "Beanbird가 귀엽죠? ^^")

def myFunc2() :
    if chk.get() == 0 :
        messagebox.showinfo("", "체크 버튼이 꺼졌어요")
    else :
        messagebox.showinfo("", "체크 버튼이 켜졌어")

def myFunc3() :
    if var.get() == 1 :
        label1.configure(text = "파이썬")
    elif var.get() == 2 :
        label1.configure(text = "C++")
    else :
        label1.configure(text = "Java")
    
## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    window = Tk()       # window name 'Tk'
    
    window.title("윈도우 창 연습")
    window.geometry("1000x1000")
#    window.resizable(width = FALSE, height = FALSE)

    label1 = Label(window, text = "COOKBOOK~` Pythn 을") # label 생성
    label2 = Label(window, text = "열심히", font = ("궁서체", 30), fg = "blue")
    label3 = Label(window, text = "공부 중입니다.", bg = "magenta", width = 20,
                   height =5, anchor = SE)
    #   anchor 는 위젯이 어느 뉘치에 자리 잡을 지 결정
    #   N = north, NE = North East, .. CENTER 등.
    label1.pack()       # pack 함수가 화면에 뿌려준다.
    label2.pack()
    label3.pack()

    #   lable 에 이미지를 넣는다.
    photo = PhotoImage(file = 'picture/hallowin.gif')
    label4 = Label(window, image = photo, width = 200, height =200, anchor = N)

    label4.pack(side=LEFT)

    photo1 = PhotoImage(file = 'picture/LGwebOS.gif')
    label5 = Label(window, image = photo1)

    label5.pack(side=RIGHT)

    photo2 = PhotoImage(file = 'picture/finish.gif')
    label6 = Label(window, image = photo2, width = 200, height =200)

    # 버튼을 삽입한다.
    # 버튼을 누르면 IDLE 이 빠져 나가는 코드이다.
    button1 = Button(window, text =" 파이썬 종료", fg = "red", command = quit)
    button1.pack(side=BOTTOM)

    label6.pack(side=LEFT)

    #   이미지 버튼을 누르면 간단한 메세지 창이 나오는 코드
    photo3 = PhotoImage(file = 'picture/zzz.gif')
    button2 = Button(window, image = photo3, width = 200, height =200, command = myFunc)
    button2.pack(side=BOTTOM)

    label6.pack(side=TOP)

    #   체크 버튼
    chk = IntVar()  # 정수를 return 받는다. check 가 되면 '1', check 가 풀리면 '0' ==> chk.get() 을 통해 전달 됨.
    cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc2)

    cb1.pack(side=RIGHT)

    #   Radio 버튼의 사용
    var = IntVar()
    rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = myFunc3)
    rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = myFunc3)
    rb3 = Radiobutton(window, text = "Java", variable = var, value = 3, command = myFunc3)

    label7 = Label(window, text = "선택한 언어 : ", fg = "blue")

    rb1.pack()
    rb2.pack()
    rb3.pack()
    label7.pack()

    window.mainloop()   # 화면 처리 부분이다.
