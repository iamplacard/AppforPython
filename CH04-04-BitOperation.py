## bit operation
## Left shift 연산 
## Right Shift 연산
## shift 할 숫자와 출력할 횟수를 입력 받는 프로그램

## 변수 선언 ##
a       = 100
results = 0
i       = 0

## 함수 선언 ##

## 화면에서 마우스 왼쪽 버튼을 누르면 클릭한 위치에 다양한 색상, 크기, 각도의

## Main Code ##
if __name__ == "__main__" :
       print("\n Left Shift 연산")
       for i in range(1,5) :
              results = a << i
              print(" %d = %d << %d" % (results, a, i))

       print("\n bit right shift 연산 ")
       for i in range(1,5) :
              results = a >> i
              print(" %d = %d >> %d" % (results, a, i))

       print("\n shift 할 숫자와 출력할 횟수를 입력 받는 프로그램 ")
       shiftVar = int(input("shift 할 숫자 입력 :"))
       loopVar  = int(input(" looping Value : "))
       for i in range(1,loopVar) :
              results = shiftVar << i
              print(" %d = %d << %d" % (results, shiftVar, i))
       for i in range(1,loopVar) :
              results = shiftVar >> i
              print(" %d = %d >> %d" % (results, shiftVar, i))


             

