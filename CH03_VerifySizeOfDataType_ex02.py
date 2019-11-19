## 파이썬에서 제공되는 각 데이터형의 기본 크기를 확인하는 프로그램이다.  ##

import sys

## 함수 선언 ##
## 변수 선언 ##
intVar, floatVar, boolVar, strVar, listVar, tupleVar, dicVar, setVar = [None] * 8

## Main Code ##
if __name__ == "__main__" :
  intVar = 0
  floatVar = 0.0
  boolVar = True
  strVar = ''
  listVar = []
  tupleVar = ()
  dicVar = {}
  setVar = set()
  
  print('int        형 기본 크기 --> ', sys.getsizeof(intVar))
  print('float      형 기본 크기 --> ', sys.getsizeof(floatVar))
  print('bool       형 기본 크기 --> ', sys.getsizeof(boolVar))
  print('string     형 기본 크기 --> ', sys.getsizeof(strVar))
  print('list       형 기본 크기 --> ', sys.getsizeof(listVar))
  print('tuple      형 기본 크기 --> ', sys.getsizeof(tupleVar))
  print('dictionary 형 기본 크기 --> ', sys.getsizeof(dicVar))
  print('집합 set   형 기본 크기 --> ', sys.getsizeof(setVar))
