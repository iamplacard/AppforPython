## Total ##
import random

## 함수 선언 ##

## 변수 선언 ##
select, answer, numStr, num1, num2 = 0,0, "", 0, 0
numbers = []

## Main Code ##
if __name__ == "__main__" :
    select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 :"))

    if select == 1 :
        numStr = input(" *** 수식을 입력하세요. :")
        ## eval 은 수식 계산 함수 입니다. ##
        answer = eval(numStr)
        print("%s 결과는 %5.1f입니다. " % (numStr, answer))
    elif select == 2 :
        num1 = int(input(" *** 첫 번째 숫자를 입력하세요. "))
        num2 = int(input(" *** 두 번째 숫자를 입력하세요. "))
        addNum = int(input(" *** 더할 숫자를 입력하세요. "))
        for i in range (num1, num2 + 1, addNum) :
            answer = answer + i
        print("%d+...+%d는 %d입니다." % (num1, num2, answer))
    else    :
        print("1 또는 2만 입력해야합니다.")


    for i in range(0,6) :
        numbers.append(random.randrange(1,50))

    print(numbers)
    

