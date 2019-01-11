## Free moving Turtle

import turtle
import random

## 함수 선언 ##
def  screenLeftClick(x,y) :
       global r, g, b
       r = random.random()
       g = random.random()
       b = random.random()
       turtle.color((r,g,b))
       
       tSize = random.randrange(1,10)
       turtle.shapesize(tSize)

       tTilt = random.randrange(10, 350)
       turtle.tilt(tTilt)

       turtle.stamp()
       turtle.goto(x,y)
       
## 변수 선언 ##
pSize = 10
r,g,b = 0.0, 0.0, 0.0## 함수 선언 ##

## 화면에서 마우스 왼쪽 버튼을 누르면 클릭한 위치에 다양한 색상, 크기, 각도의
## 거북이 모양 도장이 찍히는 프로그램
##  turtle.shape('turtle')
##  turtle.onscreenclick(screenLeftClick, 1)
##  turtle.done()

## Main Code ##
if __name__ == "__main__" :

