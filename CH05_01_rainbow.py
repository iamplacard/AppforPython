## Rainbow ##
'''

'''

import turtle

## 함수 선언 ##

## 변수 선언 ##
swidth, sheight = 1000, 300

## Main Code ##
if __name__ == "__main__" :
    turtle.title('원형 무지게 그리기 ')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.goto(0,-sheight/2)
    turtle.pendown()
    turtle.speed(10)

    for radius in range(1,250) :
        if radius % 6 == 0 :
            turtle.pencolor('red')
        elif radius % 5 == 0 :
            turtle.pencolor('orange')
        elif radius % 4 == 0 :
            turtle.pencolor('yellow')
        elif radius % 3 == 1 :
            turtle.pencolor('green')
        elif radius % 2 == 0 :
            turtle.pencolor('blue')
        elif radius % 1 == 0 :
            turtle.pencolor('navyblue')
        else :
            turtle.pencolor('purple')

        turtle.circle(radius)
        turtle.goto((250 - radius),(-sheight/2 + radius))


    turtle.done()

'''
dot(self, size=None, *color)
Draw a dot with diameter size, using color.
 
Optional arguments:
size -- an integer >= 1 (if given)
color -- a colorstring or a numeric color tuple
 
Draw a circular dot with diameter size, using color.
If size is not given, the maximum of pensize+4 and 2*pensize is used.
 
Example (for a Turtle instance named turtle):
>>> turtle.dot()
>>> turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
'''
