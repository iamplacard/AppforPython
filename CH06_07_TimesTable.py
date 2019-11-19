## 구구단 출력
## 사용자가 입력한 숫자의 단에서 구구단을 출력하는 프로그램

import math

## 변수 선언 ##
num = 0

## 함수 선언 ##

## 

## Main Code ##
if __name__ == "__main__" :
       num = int(input("구구단을 출력할 첫번째 숫자를 입력하세요.."))
       if num > 1 and num < 10 :
              for i in range(num, 10, 1) :
                     print("#    %d 단   #"% i, end = "     ")
              print(" ")

              for k in range(1, 10, 1) :
                     for i in range(num, 10, 1) :
                            print("%2d x %2d = %3d"% (i, k, i * k), end = "     ")
                     print(" ")

              for i in range(9, num - 1, -1) :
                     print("#    %d 단   #"% i, end = "     ")
              print(" ")

              for k in range(9, 0, -1) :
                     for i in range(9, num - 1, -1) :
                            print("%2d x %2d = %3d"% (i, k, i * k), end = "     ")
                     print(" ")
                     
              print("#    %d 단   #"% num, end = "     ")
              print(" ")

              for k in range(9, 0, -1) :
                     print("%2d x %2d = %3d"% (num, k, num * k), end = "     ")
                     print(" ")
       else :
              print("This number is out of range. Please input in range 2 - 9")
