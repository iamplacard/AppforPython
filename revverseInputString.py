#문자열을 입력 받고, 입력 받은 문자열의 순서를 거꾸로 출력해 보자. 
## 함수 선언 ##
## 변수 선언 ##
## Main Code ##
if __name__ == "__main__" :
  inputStr = input("문자열 입력 : ")
  strSize = len(inputStr)
  
  for i in range(strSize -1, -1, -1) :
    print("%c" % inputStr[i], end = ' ')
