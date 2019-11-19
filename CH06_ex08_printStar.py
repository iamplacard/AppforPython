## printing Star

import re

## 변수 선언 ##
i, k = 0, 0
count = 0
inputStr, ch = "", ""
starLine, inputNum, printingNum = 0, 0, 0

## 함수 선언 ##

## 

## Main Code ##
if __name__ == "__main__" :
       ## 입력한 숫자의 두 배만큼 별을 출력하는 프로그램
       
       inputStr = input("프린트 할 별의 개수슬 입력하세요 : ")

       if inputStr.isdigit() :
              starLine = len(inputStr)
              inputNum = int(inputStr)
              i = 1
              while i < starLine + 1 :
                     divideNum = 10 ** (starLine - i)
                     printingNum = inputNum // divideNum
                     inputNum = inputNum % divideNum
                     i += 1
                     print(" printNum %d divideNum %d starLine %d " % (printingNum, divideNum, starLine))

                     k = 0
                     while k < printingNum * 2:
                            print("\u2605", end = "")
                            k += 1
                     print()
       else :
              print(" Please enter numbers not character ")


       ## 입력한 숫자만큼 하트를 출력하는 프로그램
       numStr = input("숫자를 여러개 입력하세요 : ")

       i = 0
       ch = numStr[i]

       if ch.isdigit() :
              while  True :
                     heartNum = int(ch)

                     heartStr = ""
                     for k in range(0, heartNum) :
                            heartStr += "\u2665"
                            k += 1
                            
                     print(heartStr)

                     i += 1
                     if (i > len(numStr) - 1) :
                            break

                     ch = numStr[i]
       else :
              print(" Please enter numbers not character ")
       
