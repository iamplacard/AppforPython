##  함수 예제 들 - 계산기
import random

## 함수 선언 ##
def calc(v1, op, v2) :
    results = 0
    if op == '+' :
        results = v1 + v2
    elif op == '-' :
        results = v1 - v2
    elif op == '*' :
        results = v1 * v2
    elif op == '/' :
        if v2 == 0 :
            print(" divide by zero is not allowed for this operation / ")
        else :
            results = v1 / v2
    elif op == '**' :
        results = v1 ** v2
    else :
        print("Operation you want is not available for this function")

    return results

## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    operation = input("Please type oprator for calculation. (+,-,*,/,**) : ")
    var1 = int(input("Please enter first value to be calculated : "))
    var2 = int(input("Please enter second value to be calculated : "))

    res = calc(var1, operation, var2)

    print("## 계산기 %d %s %d = %d" % (var1, operation, var2, res))
