## tutle binary examle ##
'''
비트 논리곱을 구현한다 숫자를 2개를 입력 받아서 각 숫자에 대한 2진수와
비트 논리곱의 결과 2진수를 출력하는 프로그램을 작성하시오
'''

import turtle

## 함수 선언 ##

## 변수 선언 ##
num1, num2, results = 0, 0, 0
swidth, sheight = 1000, 300
curX, curY = 0, 0

## Main Code ##
if __name__ == "__main__" :
    turtle.title('비트 논리곱의 결과를 거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)
    num1 = int(input("첫번 째 숫자를 입력하세요 :"))
    num2 = int(input("두번 째 숫자를 입력하세요 :"))
    results = num1 & num2

    binary1 = bin(num1)
    curX = swidth / 2
    curY = (sheight / 3)
    for i in range(len(binary1) - 2) :
        turtle.goto(curX, curY)
        if num1 & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num1 >>= 1

    binary2 = bin(num2)
    curX = swidth / 2
    curY = 0
    for i in range(len(binary2) - 2) :
        turtle.goto(curX, curY)
        if num2 & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num2 >>= 1

    binary = bin(results)
    curX = swidth / 2
    curY = -(sheight / 3)
    for i in range(len(binary) - 2) :
        turtle.goto(curX, curY)
        if results & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        results >>= 1
        
    turtle.done()
