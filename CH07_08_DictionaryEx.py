## dictionary 연습

## 변수 선언 ##

## 함수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    ## dictionary 는 쌍 2개가 하나로 묶인 자료 구조이다.
    ## 구성 : dictioanry_var = {key1 : value1, key2 : value2, key3 : value3, ...}
    ## dictionary 생성
    dict1 = {1:'a', 2 : 'b', 3 : 'c'}
    print(dict1)

    ## student dictionary 
    student1 = {'이름' : '홍길동', '학번' : 85004801, '전화번호' : '010-8001-9895'}
    print(student1)
    ## 항목 추가
    student1['학과'] = 'IT 공학과'
    print(student1)

    ## 이미 존재하는 항목을 추가 하면 이전의 내용이 변경 됨
    print(student1)
    student1['학과'] = '의료공학과'
    print(student1)

    ## 딕셔너리의 항목 삭제는 del(딕셔너리 명[키]) 로 가능하다.
    print(student1)
    del(student1['학과'])
    print(student1)

    ## student dictionary 에서 같은 키를 계속 정의하면 제일 마지막의 것이 적용된다. 
    student1 = {'이름' : '홍길동', '학번' : 85004801, '전화번호' : '010-8001-9895', "이름" : 'Hans Lee'}
    print(student1)

    print("학번 : ", student1['학번'])
    print("이름 : ", student1['이름'])
    print("전화번호 : ", student1['전화번호'])

    ## 딕셔너리에서 Key 로 값에 접근하는 방법 dictionary.get(key)
    print(" 이름 : ", student1.get('이름'))
    
    ## 딕셔너리의 모든 key 반환 : dictionary.keys()
    print(" key list : ", student1.keys())
    ## 딕셔너리의 모든 key 만 반환 : list(dictionary.keys())
    print(" key list only : ", list(student1.keys()))
    ## 딕셔너리의 모든 value 반환 : dictionary.values()
    print(" value list : ", student1.values())
    ## 딕셔너리의 모든 value 만  반환 : list(dictionary.values())
    print(" value list only : ", list(student1.values()))
    ## 딕셔너리의 모든 item 반환 - key value pair : dictionary.items()
    print(" item list : ", student1.items()) 
    ## 딕셔너리의 모든 item 만 반환 - key value pair : list(dictionary.items()) - tuple 로 출력
    print(" item list only : ", list(student1.items()))

    ## for 문을 이용해서 dictionary 의 모든 값을 출력하는 프로그램.. 
    singer = {}

    singer['이름'] = '트와이스'
    singer['구성원 수'] = 9
    singer['데뷔'] = '서바이벌 식스틴'
    singer['대표곡'] = 'SIGNAL'

    for k in singer.keys() :
        print("%s --> %s" % (k, singer[k]))

    ## Dictionary 의 정렬
    ## Key 로 정렬하여 딕셔너리 추출하는 데... 결과는Tuple 로 변경이 되고, 리스트로 반환이 된다.

    import operator

    trainDic, trainList = {}, []

    trainDic = {'Thomas' : '토마스', 'Edward' : '에드워드', 'Henry' : '헨리', 'Gothon' : '고든', 'James' : '제임스'}
    print(trainDic)

    ## key 로 sorting : itemgetter(0)
    trainList = sorted(trainDic.items(), key = operator.itemgetter(0))

    print(trainList)
    
    ## value 로 sorting : itemgetter(1)
    trainList = sorted(trainDic.items(), key = operator.itemgetter(1))

    print(trainList)
