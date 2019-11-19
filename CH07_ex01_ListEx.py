## 순서 정렬

import random

## 변수 선언 ##
data = [] # list 
i, k = 0, 0

## 함수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    ## 16진수 정렬하기
    for i in range(0,10) :
        tmp = hex(random.randrange(0,100000))
        data.append(tmp)

    print("\n 정렬전 데이터 : ", end = " ")
    [print(num, end = ' ') for num in data]   ## list comprehension

    for i in range(0, len(data) - 1) :
        for k in range(i+1, len(data)) :
            if int(data[i],16) > int(data[k],16) :
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp
    
    print("\n 정렬후 데이터 : ", end = " ")
    [print(num, end = ' ') for num in data] ## list comprehension
