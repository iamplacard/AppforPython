## Bic List ##
## 리스트에 3ㅢ 배수를 200개 입력하도록 하고,
## 또 다른 리스트에는 역순으로 리스트를 입력하도록 하라...
## bb[0] bb[199] 를 출력하라.

## 함수 선언 ##

## 변수 선언 ##
aa = []
aa1 = []
aa2 = []

value = 1

## Main Code ##
if __name__ == "__main__" :
##  two dimensional list initialization
    for i in range(3) :
        for k in range(4) :
            aa2.append(value)
            value += 1
        aa1.append(aa2)
        aa2 = []

    print("aa1 =", aa1, "aa2 = ", aa2)

    for i in range(0,3) :
        for k in range(0,4) :
            print("%3d "% aa1[i][k], end =" ")
        print("")  ## 이것으로 next line 으로 넘어 가는 것이 가능하게 하는 것. 

        
    
