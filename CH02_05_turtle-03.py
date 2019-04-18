## tutle grapic Program ##
'''
   Comment for many lines
   Many lines
'''

'''
   def  함수명(매개변수) :
       global 사용할_전역_변수
       # 이 부분에 함수 내용을 코딩
'''

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
myT = None
pSize = 10
r,g,b = 0.0, 0.0, 0.0

##       turtle.clearstamp(stampid)


## Main Code ##

'''
커서를 좌우로 움직여 네모를 그리는 코드.
'''

# turtle.shape('turtle')
# turtle.shape('classic')
turtle.shape('triangle')

turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

turtle.clearscreen()

'''
커서를 좌우로 움직여 네모를 그리는 코드이고 for loop 사용 함.
'''

myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0,4) :
    turtle.forward(200)
    turtle.right(90)

turtle.clearscreen()

'''
화면에서 마우스 왼쪽 버튼을 누르면 클릭한 위치에 다양한 색상, 크기, 각도의
거북이 모양 도장이 찍히는 프로그램을 만드시오.
'''

turtle.shape('classic')

turtle.onscreenclick(screenLeftClick, 1)

turtle.done()
