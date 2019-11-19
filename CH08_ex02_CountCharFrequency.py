##  긴 문장에서 각 문자의 발생 빈도를 센다. 출력은 빈도수가 높은 글자붜 출력한다.
##  단 한글만 빈도수를 세고 나머지 글자들은 무시한다. 여기서는 딕셔너리를 활용해서 코드를 작성한다.

##  contens
## 

import operator

## 함수 선언 ##

## 변수 선언 ##
ss = "내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다. \
    네가 그의 이름을 불러주었을 때, 그는 내게로 와 꽃이 되었다. \
    내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞는 누가 나의 이름을 불러다오. \
    그에게로 가서 나도 그의 꽃이 되고 싶다. \우리들은 모두 무엇이 되고 싶다. \
    나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다. "
countList = []
countDic = {}
countValue = 0

## Main Code ##
if __name__ == "__main__" :

## making dictionary
## 문자는 무조건 1을 설정 하고,
## 두 번째 나온 문자는 1을 증가 한다. 
    for ch in ss :
        if '가' <= ch and ch <= '힣' :
            if ch in countDic :
                countDic[ch] += 1
            else :
                countDic[ch] = 1

## from dictionary, we can make list for frequency of characters. ==> List can be ordered from top frequency character
    countList = sorted(countDic.items(), key = operator.itemgetter(1), reverse = True)

    print(" 원문 -- ", ss)
    print(" 문자 \t 빈도수")
    print("--------------------------")
    for i in range(0, len(countList)) :
          print(countList[i][0], '\t', countList[i][1])

    print(countDic)
    print(countList)
    
