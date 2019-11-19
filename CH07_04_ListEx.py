## Bic List ##
## 리스트에 3ㅢ 배수를 200개 입력하도록 하고,
## 또 다른 리스트에는 역순으로 리스트를 입력하도록 하라...
## bb[0] bb[199] 를 출력하라.

## 함수 선언 ##

## 변수 선언 ##
aa = []
bb = []
cc = []
dd = []

value = 0

## Main Code ##

## basic example to make a many inputs
if __name__ == "__main__" :
    value = 0
    for i in range (0, 200) :
        aa.append(value)
        value +=3

    value = 0
    for i in range (0, 200) :
        bb.append(aa[199 - i])

    print(" b[0] = %d, b[199] = %d " % (bb[0], bb[199]))

##  음수값으로 접근 
    print(" bb[-1] = %d, bb[-200] = %d " % (bb[-1], bb[-200]))
    print(" bb[199] = %d, bb[0] = %d " % (bb[199], bb[0]))

##  콜론을 사용하여 범위를 표시한다. 리스트의 범위
    print(" bb[0:10] = ", bb[0:10])

##  리스트의 덧셈 및 곱셈
    for i in range (0,5) :
        cc.append(aa[i])
        dd.append(aa[5 + i])
    print(" cc = ", cc)
    print(" dd = ", dd)
    print(" 더하여도 항이 늘어남 cc + dd ", cc + dd)
    print(" 곱하면 똑같은 항이 늘어남 cc * 3 = ", cc * 3)

##  건너 뛰기
    print("리스트 cc = ", cc)
    print("앞에서 부터 두 칸 씩 건너뛰기 cc[::2] = ", cc[::2])
    print("뒤에서 부터 두 칸 씩 건너뛰기 cc[::-2] = ", cc[::-2])
    print("뒤에서 부터 한 칸 씩 건너뛰기 (즉 역순) cc[::-1] = ", cc[::-1])
    print("첫 번째 에서 부터 두 칸 씩 건너뛰기 cc[1::2] = ", cc[1::2])

##  리스트 항목 삭제 방법
    print("\n cc = ", cc)
    del(cc[2])
    print(" delete element of List del(cc[2]) = ", cc)

##  리스트에서 여러개 항목을 삭제하는 방법
    print("\n cc = ", cc)
    cc[1:3] = []
    print(" delete elements of List - delete cc[1], cc[2], not cc[3] --> cc[1:3] = []) = ", cc)

##  리스트를 삭제하는 방법
    cc = dd
    print("\n dd = ", dd)
    dd = []
    print("delete List dd = []) = ", dd)

    dd = cc
    print("\n dd = ", dd)
    dd = None
    print("delete List dd = None) = ", dd)
    
    dd = cc
    print("\n dd = ", dd)
    del(dd)
    ##    print("delete List dd = None) = ", dd) --> error 발생

##  List 조작 함수
##  append() 리스트의 맨 뒤에 항목 추가 - Usage : list.append(value)
##  pop()    리스트 맨 뒤의 항목을 뺀다.- Usage : list.pop()
##  sort()   리스트 항목을 정리한다.    - Usage : list.sort()
##  reverse()리스트 항목을 역순으로 만듦 - Usage : list.reverse()
##  index()  지정한 값을 찾아 해당 위치를 반환한다. : Usage : list.index(findingValue)
##  insert() 지정된 위치에 값을 삽입한다. - Usage : list.insert(index, value)
##  remove() 리스트에서 지정한 값을 삭제한다. 지정한 값이 여러개인 경우에는 첫 번째 값만 지운다.
##                                          Usage : list.remove(reemovingValue)
##  extend() 리스트 뒤에 리스트를 추가한다. Usage : list.extend(appendingList)
##  count()  리스트에서 해당 값의 개수를 샌다. Usage : list.count(countingValue)
##  clear()  리스트의 내용을 모두 지운다.   Usage : list.clear()
##  del()    리스트에서 해당 위치의 항목을 지운다. Usage : del(list[index])
##  len()    리스트에 포함된 전체 항목의 개수를 센다. Usage : len(list)
##  copy()   리스의 내용을 새로운 리스트에 복사한다. Usage : newList = list.copy()
##  sorted() 리스트의 항목을 정렬해서 새로운 리스트에 대입한다. Usage : newList = sorted(list)

    dd = cc.copy()
    print("list dd ", dd, "list cc ", cc)

    print("\n list cc ", cc)
    cc.append(100)
    print(" append() 리스트의 맨 뒤에 항목 추가 - Usage : list.append(value) \n ", cc)

    print("\n list cc ", cc)
    cc.pop()
    print(" pop() 리스트 맨 뒤의 항목을 뺀다.- Usage : list.pop() \n", cc)

    print("\n list cc ", cc)
    cc.sort()
    print("sort()   리스트 항목을 정리한다.    - Usage : list.sort() \n", cc)

    print("\n list cc ", cc)
    cc.reverse()
    print("reverse()리스트 항목을 역순으로 만듦 - Usage : list.reverse() \n", cc)

    print("\n list cc ", cc)
    cc.index(27)
    print("index()  지정한 값을 찾아 해당 위치를 반환한다. : Usage : list.index(findingValue) \n", cc.index(27))

    print("\n list cc ", cc)
    cc.insert(3, 100)
    print("insert() 지정된 위치에 값을 삽입한다. - Usage : list.insert(index, value) \n", cc)

    print("\n list cc ", cc)
    cc.remove(100)
    print("remove() 리스트에서 지정한 값을 삭제한다. 지정한 값이 여러개인 경우에는 첫 번째 값만 지운다.\
                                          Usage : list.remove(reemovingValue) \n", cc)

    print("\n list cc ", cc)
    cc.extend(dd)
    print("extend() 리스트 뒤에 리스트를 추가한다. Usage : list.extend(appendingList) \n", cc)     
    
    print("\n list cc ", cc)
    cc.count(27)
    print("count()  리스트에서 해당 값의 개수를 샌다. Usage : list.count(countingValue) \n", cc.count(27))

    print("\n list dd ", dd)
    dd.clear()
    print("  clear()  리스트의 내용을 모두 지운다.   Usage : list.clear() \n", dd)
    dd = cc.copy()

    print("\n list dd ", cc, "dd \n", dd)
    dd = sorted(cc)
    print(" sorted() 리스트의 항목을 정렬해서 새로운 리스트에 대입한다. Usage : newList = sorted(list) \n", cc, "dd \n", dd)
