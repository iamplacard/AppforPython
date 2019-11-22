## 거북 구구 단
'''
window size 를 1800x900으로 설정을 하고, 전체 window 의 setup 은 가로 세로 50씩 더해서 설정한다.
초기에는 Turtle 의 pen 을 들고 중앙 좌료로 이동
수평으로 먼저 80씩 8번 이동하고 40씩 아래로 9번을 써내려간다. 
이때 쓰는 내용은 2x1 3x1 을 계속 쓰고, 다음 줄에 2x2 3x2 와 같이 쓰게 된다.
그 이후에 커서의 위치를 200.-200 으로 옮기고 
거북이가 화면 가운데에서 출발해 선 80개를 소라 모양으로 그리도록 프로그램을 작성한다.
선의 색상은 무작위로 선택하고, 선의 길이는 5에서 시작해서 1씩 증가하게 하고, 각도는 30도씩 회전시킨다.
'''

import turtle
import random
import math

## 변수 선언 ##
r, g, b, i, k, t1x, t1y = [0] * 7
swidth, sheight = 1800, 900
angle = 30
dist = 5

## 함수 선언 ##

## 

## Main Code ##
if __name__ == "__main__" :
       turtle.title(' Turtle Multiplication ')
       turtle.shape('turtle')
       turtle.setup(width = swidth + 50, height = sheight + 50)
       turtle.screensize(swidth, sheight)
       turtle.penup()
       t1x, t1y = -900, 500
       turtle.goto(t1x, t1y)

       for i in range(1, 10, 1) :
              for k in range(2, 10, 1) :
                     turtle.goto(t1x + 80 * k, t1y - 40 * i)
                     gugu = str(k) + ' x ' + str(i) + ' = ' + str(k * i)
                     turtle.write(gugu, font = ('Arial', 12, 'bold'))

       turtle.penup()
       t1x, t1y = 200, -200
       turtle.goto(t1x, t1y)
       turtle.pendown()

       for i in range (0, 80) :
              r = random.random()
              g = random.random()
              b = random.random()
              turtle.pencolor((r,g,b))
              dist += 1
              turtle.forward(dist)
              turtle.left(angle)

       turtle.done()
