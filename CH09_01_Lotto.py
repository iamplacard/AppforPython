##  로또 번호 추첨
##  매개 변수를 정하지 않고 전달 하는 방법

import random

## 함수 선언 ##

##  파라미터가 튜플로 전달이 된다.  parameter 앞에 * 를 붙임
def para_func(*para) :
    results = 0
    for num in para :
        results += num

    return results

##  파라미터가 Dictionary 형식으로 전달이  된다.  parameter 앞에 ** 를 붙임
def dic_func(**para) :
    for k in para.keys() :
        print("%s --> %d 명입니다." %(k, para[k]))

def getNumber() :
    return random.randrange(1,46)

## 변수 선언 ##
hap = 0
lotto = []
num = 0

## Main Code ##
if __name__ == "__main__" :
    hap = para_func(10,20)
    print("매개 변수가 2개인 함수를 호출한 결과 : ", hap)
    hap = para_func(10,20,30)
    print("매개 변수가 3개인 함수를 호출한 결과 : ", hap)

    print("걸그룹의 멤버는 ?")
    dic_func(트와이스 = 7, 소녀시대 = 9, 걸스데이 = 4, 블랙핑크 = 4)

    print(" 로또 추첨을 시작 합니다. ^^^^")

    k = 0
    while True :
        k += 1
        num = getNumber()

        if lotto.count(num) == 0 :
            lotto.append(num)

        if len(lotto) == 6 :
            break


    print(" 추첨된 로또 번호 ==> ", end = '')
    lotto.sort()
    for i in range(0,6) :
        print("%d " %lotto[i], end = '')

    print(" ")
    print("Lotto Number is : ", lotto, "횟수", k)
