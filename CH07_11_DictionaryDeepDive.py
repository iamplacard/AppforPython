## dictionary 연습

## 변수 선언 ##
foods = {"떡볶이" : "오뎅",
         "짜장면" : "단무지",
         "라면" : "김치",
         "피자" : "피클",
         "맥주" : "땅콩",
         "치킨" : "치킨 무",
         "삼겹살" : "상추"};
         
## 함수 선언 ##

## Main Code ##
if __name__ == "__main__" :
## 세트 는 키만 모아놓은 사전의 특수한 형태

    ## 차집합 , 교집합, 합집합 대칭 차집합 을 구할 수 있다.
    mySet1 = {1,2,3,4,5}
    mySet2 = {4,5,6,7}

    print(mySet1 & mySet2)
    print(mySet1 | mySet2)
    print(mySet1 - mySet2)
    print(mySet1 ^ mySet2) 

## 동일하게 ..
    print(mySet1.intersection(mySet2))
    print(mySet1.union(mySet2))
    print(mySet1.difference(mySet2))
    print(mySet1.symmetric_difference(mySet2) )

    ## Comprehension : 함축
    numList = []
    for num in range(1,6) :
        numList.append(num)
    print(numList)

    ## 함축을 사용하여 같은 기능의 표현을 할 수 있다.

    numList = []
    numList = [num for num in range(1,6)]
    print(numList)
    ## 다양하게 .. num 의 제곱을.. 
    numList = []
    numList = [num*num for num in range(1,6)]
    print(numList)
    ## 조건문을 사용 
    numList = []
    numList = [num for num in range(1,21) if num%3 == 0]
    print(numList)

    ## 동시에 여러 리스트에 접근   zip 함수 이용.. 
    mySet1 = ["떡볶이", "짜장면","라면","피자","맥주","치킨","삼겹살"]
    mySet2 = ["오뎅", "단무지", "김치"]

    for food, side in zip(mySet1, mySet2) :
        print(food, '-->', side)

    ## 리스트나 튜플로 짝 지을 떄...
    tupList = list(zip(mySet1, mySet2))
    dic = dict(zip(mySet1, mySet2))
    print(tupList)
    print(dic)

    ## 리스트 복사
    ## 변수를 그대로 카피하면 다른 변화들도 같이 동작한다... 같은 메모리 공간을 사용하기 때문에..
    ## 이를 방지하기 위해 copy 할 때 [:] 으로 카피하면 새로운 리스트에 메모리를 새로 할당한다.
    ## 또는 oldList.copy() 를 사용해도 같은 효과를 본다.
    oldList = ["떡볶이", "짜장면","라면"]
    newList = oldList
    print(newList)
    oldList[0] = "짬뽕"
    oldList.append("깐풍기")
    print(newList)

    oldList = ["떡볶이", "짜장면","라면"]
    newList = oldList[:]
    print(newList)
    oldList[0] = "짬뽕"
    oldList.append("깐풍기")
    print(newList)

    ## 리스트를 이용한 스택 구현
    ## 다섯대의 차를 스택에 넣고 빼는 작업을 하려고 한다. 여기서 top 은 자동차를 넣으려고 하는 stack 의 위치.
    parking = []
    top = 0
    ## push 하면... append() 를 사용
    parking.append('CarA')
    top += 1
    parking.append('CarB')
    top += 1
    parking.append('CarC')
    top += 1
    print(parking)
    ## pop 을 하면 스택에 있는 자동차를 한 대씩 뺴낸다..
    outCar = parking.pop()
    top -= 1
    print(outCar)
