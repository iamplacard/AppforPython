##  모듈에 대하여 ... - 함수의 집
## 모듈 호출 방법은
##  import 모듈이름 (Ch09_05_Module)
##  사용 - Ch09_05_Module.func1() 으로 사용

## 함수 선언 ##
def para_func(*para) :
    results = 0
    for num in para :
        results += num

    return results

def dic_func(**para) :
    for k in para.keys() :
        print("%s --> %d 명입니다." %(k, para[k]))

def getNumber() :
    return random.randrange(1,46)

def func1() :
    print("Ch09_05_Module.py 의 func1() 이 호출됨")

def func2() :
    print("Ch09_05_Module.py 의 func2() 이 호출됨")

def func3() :
    print("Ch09_05_Module.py 의 func3() 이 호출됨")



'''
게임 개발 기능 외부 모듈 : pyGame
윈도우 창을 제공하는 모듈 : PyGTK
데이터베이스 기능 제공 모듈 : SQLAlchemy

유용한 서드파티 모듈 참조
-- https://wiki.python.org/moin/UsefulModules
'''
