## 문자열 분리

## 함수 선언 ##
    ## split(), splitlines(), joim()
    ## split() : 문자열을 공백이나 다른 분자로 분리해 리스트를 반환한다.
    ## splitlines() : 행단위로 분리
    ## join() : 묶어 줄 구분자를 먼저 ss 에 준비한 후 구분자.join('문자열')로 사용한다.

## 변수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    ss = "Python 을 열심히 공부 하는 중"
    print("테스트할 문자열 1  : ", ss)
    print("split 로 분리한 분자열    : ", ss.split())
    ss = "하나:둘:셋"
    print("테스트할 문자열 1  : ", ss)
    print("split 와 : 로 분리한 문자열  : ", ss.split(':'))
    ss = "하나\n둘\n셋"
    print("행단위로 분리 하는 열  : ", ss)
    print("행 단위 분리한 문자열  : ", ss.splitlines())

##  년/월/일 형식으로 문자열을 입력 받아 10 년 후 날짜를 출력하는 코드이다.
    ss = input("연/월/일 입력 ==> ")
    ssList = ss.split('/')
    print("년 월 일", ssList)

    print("입력한 날짜의 10년 후 ==> ", end = "")
    print(str(int(ssList[0]) + 10) + '년', end = "")
    print(ssList[1] + '월', end = "")
    print(ssList[2] + '일', end = "")

##  함수 명에 대입하기 : map() 함수 - map(함수명, 리스트명)- 함수는 리스트  값 한한를 함수명에 대입한다.
    before = ['2019', '7', '16']
    after = list(map(int,before))
    print("\n", after)

##  문자열 정렬하고 채우기 - center(), ljust(), rjust(),zfill()
    ##  center(숫자) 숫자만큼 전체 자리수를 잡은 후 문자열을 가운데 배치
    ##  center(숫자, '문자') 앞뒤 공간에 문자로 채워 넣는다..
    ##  ljust() 왼쪽에 붙여서 출력
    ##  rjust() 오른쪽에 붙여서 출력
    ##  zfill() 오른쪽으로 붙여쓰고 왼쪽 빈 공간은 0 으로 채운다.
    ss = 'python'
    print("문자정렬 연습", ss)
    print("가운데 문자열 정렬 center(10) ==>", ss.center(10))
    print("가운데 문자열 정렬 및 양쪽 $ 로 채우기  center(10,'$') ==>", ss.center(10,'$'))
    print("왼쪽 문자열 정렬 ljust(10) ==>", ss.ljust(10))
    print("오른쪽 문자열 정렬 rjust(10) ==>", ss.rjust(10))
    print("오른쪽 문자열 정렬 하고 왼쪽은 0으로 채우기  zfill(10) ==>", ss.zfill(10))

##  문자열 구성 파악하기 - isdigit() / isalpha() / isalnum() / islower() / isupper() / isspace()
    ##  isdigit() : 숫자로만 되어 있는가?
    ##  isalpha() : 글자 알파벳으로만 되어 있는 가?
    ##  isalnum() : 글자와 숫자가 썩여있는가?
    ##  islower() : 전체가 소문자인가?
    ##  isupper() : 전체가 대문자인가?
    ##  isspace() : 전체가 공백 문자인가?

    print("1234 isdigit() ==> ", '1234'.isdigit())
    print("abcd isalpha() ==> ", 'abcd'.isalpha())
    print("abc1234 isalnum() ==> ", 'abc1234'.isalnum())
    print("abcd islower() ==> ", 'abcd'.islower())
    print("ABCD isupper() ==> ", 'ABCD'.isupper())
    print("abcABC islower() ==> ", '1234'.islower())
    print("     isspace() ==> ", '    '.isspace())

    ss = input("문장을 입력 하시오 : ")

    if ss.isdigit() :
        print("입력 문자는 숫자 입니다.")
    elif ss.isalpha() :
        print("입력 문자는 글자와 Alphabet 입니다.")
    elif ss.isalnum() :
        print("입력 문자는 글자와 숫자 입니다.")
    else :
        print("입력 문자는 글자 인지 숫자인지 확인이 되지 않습니다. - 특수 문자 입니다. ")
