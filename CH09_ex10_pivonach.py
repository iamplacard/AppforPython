##  피보나치 수열 함수
'''
피보나치 수열은 0과 1을 제외하고 자신의 앞 숫자와 그 이전 숫자를
더하는 수열을 의미한다.
'''

#  변수
numPivonach = []

# 함수
## map 함수 - 리스티에 함수 수식을 모두 한꺼번에 적용 시킨다.
## return = list(map( function, list )
addPivonach = lambda num1, num2 : num1 + num2  ## ==> lambda parameter :  function

# Recursion Function : 재귀 함수
def selfcall(num) :
    if num >= 1 :
        print('하 ', end = '')
        selfcall(num -1)
    else :
        return

def factorial(num) :
    if num <= 1 :
        return num
    else :
        return num * factorial(num-1)

## Main 함수
if __name__ == '__main__' :
    num = int(input("피보나치 수열 F(N)의 값 N 을 입력 하세요. --> "))
    for i in range(0, num + 1) :
        if i <= 1 :
            numPivonach.append(i)
        else :
            numPivonach.append(addPivonach(numPivonach[i-1], numPivonach[i-2]))

    print(numPivonach)
    print("F(%d) = %d" %(num, numPivonach[num]))
