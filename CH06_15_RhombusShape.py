## 계산기

## 변수 선언 ##
i, k = 0, 0

## 함수 선언 ##

## 

## Main Code ##
if __name__ == "__main__" :
       print('\u2605') ; print("\u4E80")
       ## \u를 붙인 후 이어서 나오는 숫자는 16진수 유니코드이다.
       ## 유니코드는 영어, 한글, 중국어, 기호..를 표시..
       
       while i < 9 :
              if i < 5 :
                     k = 0
                     while k < (4 - i) :
                            print("  ", end = "")
                            k += 1
                     k = 0
                     while k < i * 2 + 1 :
                            print("\u2605", end = "")
                            k += 1
              else :
                     k = 0
                     while k < (i - 4) :
                            print("  ", end = "")
                            k += 1
                     k = 0
                     while k < (9 - i) * 2 - 1 :
                            print("\u2605", end = "")
                            k += 1
                            
              print()
              i += 1

       i = 0
       for i in range (0,9) :
              if i < 5 :
                     k = 0
                     for k in range (0, (4 - i)) :
                            print("  ", end = "")
                            k += 1
                     k = 0
                     for k in range (0, i * 2 + 1) :
                            print("\u2665", end = "")
                            k += 1
              else :
                     k = 0
                     for k in range (0, (i - 4)) :
                            print("  ", end = "")
                            k += 1
                     k = 0
                     for k in range (0, (9 - i) * 2 - 1) :
                            print("\u2665", end = "")
                            k += 1
                            
              print()
              i += 1
