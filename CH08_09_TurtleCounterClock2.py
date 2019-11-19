##  터틀 그래픽에서 문자열을 입력 받고, 입력 받은 문자열을 한 글자씩 임의의 크기와 색상으로
##  임의의 위치에 거북이가 쓰는 프로그램
##  adkstring()으로 문자열을 입력 받는다..
import turtle
import random
import math
from tkinter.simpledialog import *

## 함수 선언 ##

## 변수 선언 ##
inStr = ''
swidth, sheight = 300, 300
tx, ty, txtSize = [0] * 3
angle = 0
dist = 100

numCount, numSpecialCharCount, numCapCount, numLowerCount, numHangeul = 0, 0, 0, 0, 0

## Main Code ##
if __name__ == "__main__" :
    turtle.title('Turtle String')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    txtSize = 20
    turtle.penup()
    turtle.goto(tx,ty)

    inStr = askstring('문자열 입력', '거북이 쓸 문자열 입력')

    angleUnit = 360 / len(inStr)

    for ch in inStr :
        angle += angleUnit
        r = random.random(); g = random.random(); b = random.random()
        tx = dist*math.cos(3.14*angle/180)
        ty = dist*math.sin(3.14*angle/180)
        turtle.goto(tx,ty)

        turtle.pencolor((r,g,b))
        turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))


    turtle.done()
