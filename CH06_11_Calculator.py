## 계산기

## 변수 선언 ##
ch = ""
a, b = 0,0

## 함수 선언 ##

## 

## Main Code ##
if __name__ == "__main__" :
       while True :
              a = int(input("계산할 첫번째 숫자를 입력하세요.."))
              b = int(input("계산할 첫번째 숫자를 입력하세요.."))
              ch = input("계산할 연산자를 입력하세요..")

              if ( ch == "+" ) :
                   print("%d + %d = %d" % (a, b, a + b))
              elif ( ch == "-" ) :
                   print("%d - %d = %d" % (a, b, a - b))
              elif ( ch == "*" ) :
                   print("%d * %d = %d" % (a, b, a * b))
              elif ( ch == "/" ) :
                   print("%d / %d = %d" % (a, b, a / b))
              elif ( ch == "%" ) :
                   print("%d % %d = %d" % (a, b, a % b))
              elif ( ch == "//" ) :
                   print("%d // %d = %d" % (a, b, a // b))
              elif ( ch == "**" ) :
                   print("%d ** %d = %d" % (a, b, a ** b))
              else :
                   print("You have wrong operator, please type correct operator for calculation.")
