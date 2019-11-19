## 거북이가 서로 만나게 하기
'''
거북이 세마리가 서로 만날 때까지 화면을 임의로 돌아다닌다.
세 마리중 서로 만나는 거북이가 있다면 움직임을 먼추고,
모든 거북이의 크기를 세배로 키운다.
'''

import turtle
import random
import math

## 변수 선언 ##
t1, t2, t3 = [None] * 3
t1x, t2x, t3x, t1y, t2y, t3y = [0] * 6
swidth, sheight = 300, 300
meetCount = 0

## 함수 선언 ##

## 

## Main Code ##
if __name__ == "__main__" :
       turtle.title(' meeting Turtles ')
       turtle.setup(width = swidth + 50, height = sheight + 50)
       turtle.screensize(swidth, sheight)

## 거북이 세마리를 마련하라..
       t1 = turtle.Turtle('turtle'); t1.color('red'); t1.penup()
       t2 = turtle.Turtle('turtle'); t2.color('green'); t2.penup()
       t3 = turtle.Turtle('turtle'); t3.color('blue'); t3.penup()

## 거북이 세마리가 위치해 있을 곳을 먼저 마련하라.
       t1.goto(-100,-100); t2.goto(0,0); t3.goto(100,100)

       while True :
## 거북이 세마리가 움직이는 각도와 거리를 임의로 추출해서 움직인다.
              angle = random.randrange(0,360)
              dist = random.randrange(1, 100)
              t1.left(angle)
              t1.forward(dist)
## 거북이 세마리가 계속 움직이게 라고 위치를 추적한다.  ㅋㅋㅋ
              t1x = t1.xcor()
              t1y = t1.ycor()

              angle = random.randrange(0,360)
              dist = random.randrange(1, 100)
              t2.left(angle)
              t2.forward(dist)
              t2x = t2.xcor()
              t2y = t2.ycor()

              angle = random.randrange(0,360)
              dist = random.randrange(1, 100)
              t3.left(angle)
              t3.forward(dist)
              t3x = t3.xcor()
              t3y = t3.ycor()

## 거북이 끼리 거리가 20 미만이면 만난 것으로 처리한다. 두 거북이의 거리는 sqrt(X2 - X1)+sqrt(Y2-Y1) 으로 계산.
              if math.sqrt(((t1x - t2x) * (t1x - t2x)) + ((t1y - t2y) * (t1y - t2y))) <= 20 or \
                     math.sqrt(((t1x - t3x) * (t1x - t3x)) + ((t1y - t3y) * (t1y - t3y))) <= 20 or \
                     math.sqrt(((t2x - t3x) * (t2x - t3x)) + ((t2y - t3y) * (t2y - t3y))) <= 20 :
##                     t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
                     t1.stamp(); t2.stamp(); t3.stamp()
                     meetCount += 1
                     print("Meet Count %d" % meetCount)
                     if meetCount == 1 :
                            t1.color('red'); t2.color('red'); t3.color('red')
                     elif meetCount == 2 :
                            t1.color('blue'); t2.color('blue'); t3.color('blue')
                     elif meetCount == 3 :
                            t1.color('yellow'); t2.color('yellow'); t3.color('yellow')
                     elif meetCount == 4 :
                            t1.color('purple'); t2.color('purple'); t3.color('purple')
                     elif meetCount == 5 :
                            t1.color('orange'); t2.color('orange'); t3.color('orange')
                     else :
                            t1.color('black'); t2.color('black'); t3.color('black')


              if (-swidth / 2 <= t1x and t1x <= swidth / 2) and (-sheight / 2 <= t1y and t1y <= sheight / 2) :
                     pass
              else :
                     t1.goto(-100,-100); t2.goto(0,0); t3.goto(100,100)

              if (-swidth / 2 <= t2x and t2x <= swidth / 2) and (-sheight / 2 <= t2y and t2y <= sheight / 2) :
                     pass
              else :
                     t2.goto(0,0)

              if (-swidth / 2 <= t3x and t3x <= swidth / 2) and (-sheight / 2 <= t3y and t3y <= sheight / 2) :
                     pass
              else :
                     t3.goto(100,100)

              if meetCount >= 5 :
                     break
              
       turtle.done()
