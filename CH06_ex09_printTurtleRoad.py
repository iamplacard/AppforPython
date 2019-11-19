## 거북 구구 단
'''

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
