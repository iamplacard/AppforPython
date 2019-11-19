##  문자와 숫자가 섞인 데이터 정렬하기
'''
'''
import random

# 함수
def getNumber(strData) :
    numStr = ''
    for ch in strData :
        if ch.isdigit() :
            numStr += ch

    return int(numStr)

#  변수
data = []
i, k = 0, 0

## Main 함수
if __name__ == '__main__' :
    for i in range(0,10) :
        tmp = hex(random.randrange(0, 100000))
        tmp = tmp[2:] # 앞의 0x 제거
        data.append(tmp)      #

    print("정렬전 데이터 : ", end = ' ' )
    [print(num, end = ' ') for num in data]

    for i in range(0, len(data) - 1) :
        for k in range(i+1, len(data)) :
            if getNumber(data[i]) > getNumber(data[k]) :
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp

    print("\n정렬 후 데이터 : ", end = ' ')
    [print(num, end = ' ') for num in data]
