#입출력 활용 예제

import sys

print("welcome to","python",sep="~",end="!",file=sys.stderr)

print("{0} is {1}".format("apple","color"))

print("{item} is {color}".format(item="apple", color="red"))

dic = {"item":"apple", "color":"red"}
print("{0[item]} is {0[color]}".format(dic))
print("{item} is {color}".format(**dic))

#!s, !r, !a 는 각각 str(), repr(), ascii() 를 실행한 결과와 동일
print("{item!s} is {color!s}".format(**dic))
print("{item!r} is {color!r}".format(**dic))
print("{item!a} is {color!a}".format(**dic))

# "." 기호를 이용하여 보다 정교하게 정렬, 폭, 부호, 공백처리, 소수점,
# 타입등을 지정하는 방법 - ">" 는 오른쪽 기준, "<" 왼쪽 기준, "^"는 가운데 기준
# "=" 가 사용되면 공백 문자들 앞에 부호가 표시됨.
# 사용되지 않으면 공백문자들 뒤, 즉. 숫자 바로 앞에 부호가 표시됨
print("{0:$>5}".format(10))
print("{0:$>-5}".format(-10))
print("{0:$>+5}".format(10))
print("{0:$> 5}".format(10))

#진수를 바꾸어 출력하는 방법 - 진수 표현법
print("{0:b}".format(10))
print("{0:o}".format(10))
print("{0:c}".format(65))

#진수 표현법 - format     #x 16진수, #o 는 8진수 , #b 는 이진수로 표현 
print("{0:#x}, {0:#o},{0:#b}".format(10))

# 실수에 대한 표현 법
# e 는 지수표현을, f는 일반적인 실수와 %는 퍼센트 표현을 의미한다... 
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:%}".format(4/3))

# 실수 표현법 - 실수에서 소수점 몇 번째 자릭까지 표현할 것인지를 지정
print("{0:.3f}".format(4/3))
print("{0:3f}".format(4/3))

# 입력 - 사용자 입력은 input() 함수를 사용
# input() 의 인자는 화면 출력할 Prompt 를 줄 수 있음 - Return 문자열 개체
a = input("insert any keys :")
print(a)

# 파일의 입출력 - open - 인자로 file 의 속성을 나타고 다음의 조합 가능
# r : 읽기 모드(디폴트), w : 쓰기 모드, a : 쓰기 + 이어쓰기 모드,
# + : 읽기 + 쓰기 모드,  b : 바이너리 모드, t : 텍스트 모드 (디폴트)
f = open("test.txt", 'w')
f.write('plow deep\nwhile sulggards sleep')
f.close()

# 파일 입출력 - read
ft = open('test.txt')
print(ft.read())
ft.close()
ft.closed

# 파일 입출력 - readline, readlines, tell, seek
# readline() : 호출 할 때 마다 한 줄씩 읽은 문자열을 반환함
# readlines() : 파일의 모든 내용을 줄 단위로 잘라서 리스트를 반환함
# tell() : 현재 파일에서 어디까지 읽고 썼는지 위치를 반환함
# seek() : 사용자가 원하는 위치로 포인터를 이동함
# with ~ as 구문
with open('test.txt') as f:
  print(f.readlines())
  print(f.closed)
f.close()

# 파일 입출력 - pickle
# 리스트나 클래스 등을 저장 하는 경우에 사용 가능한 모듈이다.
# pickle - 쓰기
colors = ['red','green','black']
import pickle
f = open('colors','wb')
    # pickle 모듈의 dump 함수를 사용하면. colors를 쉽게 파일에 저장 가능
pickle.dump('colors',f)
f.close()

del colors
f = open('colors', 'rb')
colors = pickle.load(f)
f.close()
print(colors)
      # print가 되는 데이터를 보면 리스트를 저장 하지 않고 왜, colors 라는 String이 저장이 될까?
# pickle 로 파일에 쓰거나 읽을 때는 반드시 바이너리 모드로 파일을 열어야 한다.

# pickle로 저장할 수 있는 대상은 파이선 객체라면 거의 모두 가능
# 기본 자료형은 물론이고 사용자가 정의한 클래스 객체도 가능
class test:
      var = None
a = test()
a.var = 'Test'
f = open('test','wb')
pickle.dump(a,f)
f.close()
f = open('test', 'rb')
b = pickle.load(f)
f.close()
print(b.var)
