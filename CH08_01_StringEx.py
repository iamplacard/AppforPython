## random number ##

## 함수 선언 ##

## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    ss = "파이썬 최고"
    print(ss[0])
    print(ss[1:3])
    print(ss[3:])
    ss = 'python이 최고다. 파이썬 화이팅'
    ss = ss*3
    sslen = len(ss)
    for i in range(0,sslen) :
        print(ss[i] + '$', end = " ")
    print(" ")
    ## 홀수번째를 '$'로 표시
    for i in range(0,sslen) :
        if i  % 2 != 0 :
            print('$', end = "")
        else :
            print(ss[i], end = "")
    print(" ")

    ## 입력된 문자열을 꺼꾸로 출력
    for i in range(0,sslen) :
        print(ss[sslen - i - 1], end = "")


    ## 문자열 함수 - 대문자와 소문자 변환하
    ## method() - upper(), lower(), swapcase(), title()
    ss.upper(); print(ss); print(" "); print(ss.upper()); print(" ")
    ss.lower(); print(ss); print(" "); print(ss.lower()); print(" ")
    ss.swapcase(); print(ss); print(" "); print(ss.swapcase()); print(" ")
    ss.title(); print(ss); print(" "); print(ss.title()); print(" ")

    ## 문자열 함수 - 문자열 찾기
    ## count(), find(), rfind(), index(), rindex(), startswith(), endswith()
    ## count(str) str 이 몇 개 들어 있는 지 개수를 센다.
    ## find(str)  str 이 왼쪽 끝(0 번 위치)부터 시작해서 몇 번째 위치하는지 찾는다.
    ## rfind(str) reverse find 로서 오른쪽 끝부터 찾는다..
    ## index(str) str 이 왼쪽 끝(0 번 위치)부터 시작해서 몇 번째 위치하는지 찾는다.
    ## rindex(), reverse 로서 오른쪽 끝부터 찾는다.. 없으면 오류가 발생
    ## startswith(str) 찾는 문자열로 시작하면 True
    ## endswith()    찾는 문자열로 끝나면 True
    ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠.^^'
    ss.count('공부'); print(ss); print(" "); print(ss.count('공부')); print(" ")
    print('find 공부 : ', ss.find('공부')); print(" ")            
    print("rfind(reverse) 공부 : ", ss.rfind('공부')); print(" ")            
    print("find 공부 5 : ",ss.find('공부',5)); print(" ")            
    print("find 없다 : ", ss.find('없다')); print(" ")            
    print("index 공부 : ", ss.index('공부')); print(" ")            
    print("rindex (reverse) 공부 : ", ss.rindex('공부')); print(" ")            
    print("index 공부 5 : ", ss.index('공부',5)); print(" ")
    print("startswith 파이썬 : ", ss.startswith('파이썬')); print(" ")            
    print("startswith 파이썬 10 : ", ss.startswith('파이썬', 10)); print(" ")            
    print("endswith ^^ : ", ss.endswith('^^')); print(" ")

    
