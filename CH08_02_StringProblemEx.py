## 문자열이 괄호로 감싸 있지 않으면 괄호로 감싸 주는 프로그램

## 함수 선언 ##

## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    ss = input("test 하려는 문자를 입력 하시기 바랍니다. : ")
    sslen = len(ss)
    print("input string", ss, sslen)
    if sslen > 0 :
        if ss.startswith('(') :
            if ss.endswith(')') :
                print("it is correct string set we are looking for")
            else :
                ss = ss + ')'
                print("corrected streing",ss)
                print("string does have ) character at the end of string")
        else :
            ss = '(' + ss
            if ss.endswith(')') :
                print("String does not have start signal ( ")
            else :
                ss = ss + ')'
                print("corrected string",ss)
                print("String did not have (, ) character in the string")
    else :
        print("string is empty")


    ## 문자열 함수 - 대문자와 소문자 변환하
    ## method() - upper(), lower(), swapcase(), title()
    ## 문자열 함수 - 문자열 찾기
    ## count(), find(), rfind(), index(), rindex(), startswith(), endswith()
    ## count(str) str 이 몇 개 들어 있는 지 개수를 센다.
    ## find(str)  str 이 왼쪽 끝(0 번 위치)부터 시작해서 몇 번째 위치하는지 찾는다.
    ## rfind(str) reverse find 로서 오른쪽 끝부터 찾는다..
    ## index(str) str 이 왼쪽 끝(0 번 위치)부터 시작해서 몇 번째 위치하는지 찾는다.
    ## rindex(), reverse 로서 오른쪽 끝부터 찾는다.. 없으면 오류가 발생
    ## startswith(str) 찾는 문자열로 시작하면 True
    ## endswith()    찾는 문자열로 끝나면 True

    print("\n Corrected Program which is more clear than orginal ㅠㅠ ")
    ss = input("입력 문자열 ==> ")
    if ss.startswith('(') == False :
        print(" ( ", end = '')

    print(ss, end ='')

    if ss.endswith(')') == False :
        print(" ) ", end = '')
