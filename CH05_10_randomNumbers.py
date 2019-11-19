## random number ##
import random

## 함수 선언 ##

## 변수 선언 ##
numbers = []

## Main Code ##
if __name__ == "__main__" :
    for num in range(0,10) :
        numbers.append(random.randrange(0,10))

    print("생성된 리스트", numbers)

    for num in range(0,10) :
        if num not in numbers :
            print("%d is not member of Number List" % num)
