## leap Year example ##
'''
윤년을 게산하는 프로그램이다.
'''

import turtle

## 함수 선언 ##

## 변수 선언 ##
num, results = 0, 0
swidth, sheight = 1000, 300

## Main Code ##
if __name__ == "__main__" :
    turtle.title('윤년을 거북이로 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)
    num = int(input("윤년을 확인하고자 하는 년도를 입력하세요 :"))
    results1 = num % 4
    print("Before compare results1 %d" % num)
    if results1 == 0 :
        results2 = num % 100
        print("Before compare results2 %d" % num)
        if results2 == 0 :
            print("Year %d is not Leap Year" % num)
            curX = swidth / 2
            curY = (sheight / 3)
            turtle.goto(curX, curY)
            turtle.color('red')
            turtle.turtlesize(3)
        else :
            print("Year %d is Leap Year" % num)
            curX = swidth / 2
            curY = -(sheight / 3)
            turtle.goto(curX, curY)
            turtle.color('blue')
            turtle.turtlesize(2)
    else :
        print("Year %d is not Leap Year" % num)
        curX = swidth / 2
        curY = 0
        turtle.goto(curX, curY)
        turtle.color('yellow')
        turtle.turtlesize(1)


    turtle.stamp()

    turtle.done()
