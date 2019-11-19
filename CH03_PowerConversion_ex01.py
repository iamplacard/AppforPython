## Diamon Star ##
## Diamond 모양 출력

## 함수 선언 ##

## 변수 선언 ##

## Main Code ##

if __name__ == "__main__" :
       num = input("값 입력 : ")
       num10 = int(num, 10)
       if num10 >= 0 and num10 < 16 : 
              print("16진수 ==> ", hex(num10))
       else :
              print("16진수가 아니다. ")
