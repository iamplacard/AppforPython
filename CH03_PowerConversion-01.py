## Power Conversio program
## I present power conversion program which decides type of power first and then input the number to convert.
## If it is not right select, notify that it is not within scope and exit program.
## If you got right selection within scope, then check power index and convert input number you typed to decimal digit.
## Print all numbers converted.

## 함수 선언 ##

## 변수 선언 ##

## Main Code ##

if __name__ == "__main__" :
       sel = int(input("입력 진수 결정 (16/10/8/2) :  "))
       num = input("값 입력 : ")

       if sel != 16 and sel != 10 and sel !=8 and sel !=2 :
              print("16, 10, 8, 2 숫자 중 하나만 입력 하세요")
              exit()
       
       if sel == 16 :
              num10 = int(num, 16)
       if sel == 10 :
              num10 = int(num, 10)
       if sel == 8 :
              num10 = int(num, 8)
       if sel == 2 :
              num10 = int(num, 2)

       print("16진수 ==> ", hex(num10))
       print("10진수 ==> ", num10)
       print("8진수 ==> ", oct(num10))
       print("2진수 ==> ", bin(num10))
