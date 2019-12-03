## 기차 수송량에 따른 순위 매기기
## 여러대의 기차가 수송하는 수송량을 합산하여 순위를 메기는 것으로, (토마스 2톤) (제임스 4톤) (토마스 5톤) ...
## 같은 순위가 여러번 나오면 같은 순위만큼 거너띄고 다음 순위를 출력한다.
## 여기서는 튜플을 딕셔너리로 변경 한 후 다 시 딕셔너리를 튜플로 정렬하는 방식 사용

import random
import operator

## 변수 선언 ##
trainName = ('토마스', '헨리','에드워드', '에밀리', '토마스','헨리', '토마스', '에밀리', '퍼시', '고든')
weight = (5,8,9,5,4,7,3,8,5,13)

trainTupList = [('토마스',5), ('헨리',8),('에드워드',9), ('에밀리',5), ('토마스',4),('헨리',7),
                   ('토마스',3), ('에밀리',8), ('퍼시',5), ('고든',13)]
trainData = {}
trainDic, trainList = {}, []
tmpTup = None
totalRank, currentRank = 1, 1
i, k = 0, 0

## 함수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    trainData = dict(zip(trainName, weight))
    print(trainData)

    for tmpTup in trainTupList :
        tName = tmpTup[0]  ## tuple 의 첫번째 원소이지...
        tWeight = tmpTup[1]
        if tName in trainDic :
            trainDic[tName] += tWeight    ## tName 이 키가 되고 여기에 tWeight 가 Value 로 들어가는 구나! 즉 추가 되는 형태
        else :
            trainDic[tName] = tWeight

    print('기차 수송량 목록 ==>', trainTupList)
    print('--------------------------')
    trainList = sorted(trainDic.items(), key = operator.itemgetter(1), reverse = True)

    print('기차\t 총 수송량 \t 순위')
    print('--------------------------')
    print(trainList[0][0], '\t', trainList[0][1], '\t', currentRank)
    for i in range (1, len(trainList)) :
        totalRank += 1
        if trainList[i][1] == trainList[i-1][1] :
            pass
        else :
            currentRank = totalRank
        print(trainList[i][0], '\t', trainList[i][1], '\t', currentRank)

    
    
