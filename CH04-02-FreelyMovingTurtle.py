## Free moving turtle
## Setup turtle first. Define title, shape, pensize of turtle. Define window size with width, height
## Assign pencolor. Assign angle and distance to move automatically.
## Change angle and go by distance amount.
## Set current position of cursor
## if it is within window area, then keep print. if it is out of bound 5 times, then exit program.

import turtle
import random

## 변수 선언 ##
swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r,g,b, angle, dist, curX, curY = [0]*7

## 함수 선언 ##

## 화면에서 마우스 왼쪽 버튼을 누르면 클릭한 위치에 다양한 색상, 크기, 각도의

## Main Code ##
if __name__ == "__main__" :
       turtle.title(' turtle moves freely ')
       turtle.shape('turtle')
       turtle.pensize(pSize)
       turtle.setup(width = swidth + 30, height = sheight + 30)
       turtle.screensize(swidth, sheight)

       while True :
              r = random.random()
              g = random.random()
              b = random.random()
              turtle.pencolor((r,g,b))

              angle = random.randrange(0,360)
              dist = random.randrange(1, 100)
              turtle.left(angle)
              turtle.forward(dist)
              curX = turtle.xcor()
              curY = turtle.ycor()
              print(angle, dist, curX, curY, exitCount)

              if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2) :
                     pass
              else :
                     turtle.penup()
                     turtle.goto(0,0)
                     turtle.pendown()

                     exitCount += 1
                     if exitCount >=5 :
                            break
       turtle.done()
