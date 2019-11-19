## File IO 연습
# file 을 한 번에 한 line씩 읽기

## 함수 선언 ##


## 전역 변수 선언 ##
inFp  = None    # 입력 파일
inStr = ""      # 읽어 온 문자열
outFp = ""      #  출력 파일

## Main Code ##
if __name__ == "__main__" :
    inFp = open("./picture/constitution.txt", "r")

    i = 0
    while True :
        inStr = inFp.readline()
        if inStr == "" :
            break;
        i = i + 1
        print("%d : %s \n" %(i, inStr), end="")
        
    inFp.close()

    # 한 번에 읽기
    inFp = open("./picture/constitution.txt", "r")

    inStr = inFp.readlines()
    print(inStr)
        
    inFp.close()
