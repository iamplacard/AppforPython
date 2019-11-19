##  터틀 그래픽에서 문자열을 입력 받고, 입력 받은 문자열을 한 글자씩 임의의 크기와 색상으로
##  임의의 위치에 거북이가 쓰는 프로그램
##  adkstring()으로 문자열을 입력 받는다..
import turtle
import random
from tkinter.simpledialog import *

## 함수 선언 ##

## 변수 선언 ##
inStr = ''
swidth, sheight = 300, 300
tx, ty, txtSize = [0] * 3

numCount, numSpecialCharCount, numCapCount, numLowerCount, numHangeul = 0, 0, 0, 0, 0

## Main Code ##
if __name__ == "__main__" :
    turtle.title('Turtle String')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()

    inStr = askstring('문자열 입력', '거북이 쓸 문자열 입력')

    for ch in inStr :
        tx = random.randrange(-swidth/2,swidth/2)
        ty = random.randrange(-sheight/2,sheight)
        r = random.random(); g = random.random(); b = random.random()
        ## shape 의 임의의 크기
        txtSize = random.randrange(10,50)

        turtle.goto(tx,ty)

        turtle.pencolor((r,g,b))
        turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))



    ss = "IT CookBook 파이썬을 공부하고 있습니다. ^___^"
    ssLen = len(ss)

    for i in range(0, ssLen) :
        if ss[i].isdigit() :
            numCount += 1
        if ss[i].isalpha() :
            if ss[i].isupper() :
                numCapCount += 1
            elif ss[i].islower() :
                numLowerCount += 1
            else :
                numHangeul += 1
        else :
            numSpecialCharCount += 1

    print("대문자 : %d" % numCapCount, "소문자 : %d" % numLowerCount, "숫자 : %d" % numCount, \
          "한글 : %d" % numHangeul, "기타 : %d" % numSpecialCharCount)
            

    turtle.done()
