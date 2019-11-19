##  터틀 그래픽에서 문자열을 입력 받고, 입력 받은 문자열을 한 글자씩 임의의 크기와 색상으로
##  임의의 위치에 거북이가 쓰는 프로그램
##  adkstring()으로 문자열을 입력 받는다..
##  같은 프로그램을 임의의 위치, 색상, 글자 크기 등을 함수를 사용해 추출하고
##  앞에서 배운 모듈로 작성한다.

import turtle
import random
from tkinter.simpledialog import *

## 함수 선언 ##
def getString() :
    retStr = ''
    retStr = askstring('문자열 입력', '거북이 쓸 문자열 입력')
    return  retStr

def getRGB() :
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b) ## tuple return

def getXYAS(sw, sh) :
    x, y, size = 0, 0, 0
    x = random.randrange(-swidth/2,swidth/2)
    y = random.randrange(-sheight/2,sheight)
    size = random.randrange(10,50)
    angle = random.randrange(0,360)

    return [x,y,size, angle]
    
    

## 변수 선언 ##
inStr = ''
swidth, sheight = 300, 300
tx, ty, txtSize, tAngle = [0] * 4

## Main Code ##
if __name__ == "__main__" :
    turtle.title('Turtle String')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()

    inStr = getString()

    for ch in inStr :
        tx, ty, txtSize, tAngle = getXYAS(swidth, sheight)
        r, g, b = getRGB()

        turtle.goto(tx,ty)
        turtle.left(tAngle)

        turtle.pencolor(r, g, b)
        turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))

    turtle.done()
