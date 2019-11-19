##  모듈에 대하여 ... - 함수의 집
## 모듈 호출 방법은
##  import 모듈이름 (Ch09_05_Module)
##  사용 - Ch09_05_Module.func1() 으로 사용

##  모듈 명을 생략하고 함수명만 쓰고 싶으면 import 할 때 다음 형식으로 하면 됨.
from Ch09_05_Module import func1, func2, func3
import math
import random
import sys

## 또는 from Ch09_05_Module import *

## 함수 선언 ##

##  변수 선언   ##

## Main Code ##
if __name__ == "__main__" :
    func1()
    func2()
    func3()


##    print(sys.builtin_module_names, end = '')

    print("\n")

    dir(math)

    print("\n")

##    dir(random)
