## 거북이 100마리 리스트를 만든 후 
## 100 마리가 화면 중앙에서 임의의 위치로 차례대로 움직이게 한다.

## 변수 선언 ##
import turtle
import random

## 변수 선언 ##
myTurtle, tColor, tSize = [None]*3
r, g, b, i, k, tx, ty, tSum = [0] * 8
swidth, sheight = 500, 500
shapeList = []
playerTurtles = []
newplayerTurtles = []

## 함수 선언 ##

## 

## Main Code ##
if __name__ == "__main__" :
    turtle.title('Turtle Pop Up')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

## 거북이 100 마리를 마련하라..++++++
    ## shape list
    shapeList = turtle.getshapes()
    for i in range(0,100) :
        ## shuffle shape list
        random.shuffle(shapeList)
        myTurtle = turtle.Turtle(shapeList[0])
        ## 임의의 위치로 위치 tx, ty
        tx = random.randrange(-swidth/2,swidth/2)
        ty = random.randrange(-sheight/2,sheight)
        tSum = tx + ty
        r = random.random()
        g = random.random()
        b = random.random()
        ## shape 의 임의의 크기
        tSize = random.randrange(1,3)
        ## Turtle Player List --- 생성
        playerTurtles.append([myTurtle, tx, ty, tSize, r, g, b, tSum])

        ## tSum을 key로 해서 playerTurtles를 오름차순 정렬한 다음 reverse ##
        ## playerTurtles의 각 원소를 반환하면 이를 turtles로 받아 turtles[7]인 tSum을 key로 사용 #
        ## 람다를 사용한 이유는 한줄짜리 간략한 함수를 구현하기 위해서입니다.
        ## temp = lambda x: x # 아래와 용도가 같습니다. 
        ## def temp(x):
        ##      return x
        newplayerTurtles = sorted(playerTurtles, key = lambda turtles : turtles[7], reverse = True)

    for index, tList in enumerate(newplayerTurtles[0:]) : # enumerate 는 tuple 형태로 index 값을 반환 해준다..
        myTurtle = tList[0]
        myTurtle.color(tList[4], tList[5], tList[6])
        myTurtle.pencolor(tList[4], tList[5], tList[6])
        myTurtle.turtlesize(tList[3])
        myTurtle.penup()
        if index == 0 :
            myTurtle.goto(tList[1], tList[2])
            continue
        ## 선을 그을 거북이의 이전 거북이 위치로 가야지요..
        myTurtle.goto(newplayerTurtles[index-1][1], newplayerTurtles[index-1][2])

        myTurtle.pendown()
        myTurtle.goto(tList[1], tList[2])
        

    turtle.done()
        
## 거북이 100 마리를 제각각의 위치로 뛰게..
'''
    for tList in playerTurtles :
        ## get Turtle from list
        myTurtle = tList[0]
        ## setup color              color
        myTurtle.color(tList[4], tList[5], tList[6])
        ## setup pen color          pencolor
        myTurtle.pencolor(tList[4], tList[5], tList[6])
        ## setup turtle size         turtlesize
        myTurtle.turtlesize(tList[3])
        ## setup turtle position  goto
        myTurtle.goto(tList[1], tList[2])
'''
    

