## File IO 연습
# file 을 한 번에 한 line씩 읽

## 함수 선언 ##


## 전역 변수 선언 ##
inFp  = None    # 입력 파일
inStr = ""      # 읽어 온 문자열

## Main Code ##
if __name__ == "__main__" :
    with open("./picture/constitution.txt", "r") as inFp :
        inStr = inFp.readlines()
        print(inStr)

    with open("./picture/constitution.txt", "r") as inFp :
        i = 0
        while True :
            inStr = inFp.readline()
            if inStr == "" :
                break
            i += 1
            print("%d : %s" % (i, inStr), end ="")
    
