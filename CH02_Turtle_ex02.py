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

## 함수 선언 ##

## 변수 선언 ##
myT = None

## Main Code ##
myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0,4) :
    turtle.forward(200)
    turtle.right(90)

turtle.done()
