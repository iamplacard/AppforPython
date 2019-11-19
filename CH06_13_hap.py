## 계산기

## 변수 선언 ##
i, hap = 0, 0

## 함수 선언 ##

## 

## Main Code ##
if __name__ == "__main__" :
       while True :
              if i >= 100 :
                     print(" Total Hap is %d" % hap)
                     break
              i += 1

              if i % 3 == 0 :
                     continue
              
              hap += i

              if hap > 1000 :
                     print(" %d is the point hap is over 1000" % i)
                     print(" Total hap is %d " % hap)
                     break

       i = 0; hap = 0
       while i < 101 :
              hap = hap + i
              i += 2

       print(" Even number hap between 0 to 100 is %d" % hap)

       i = 1; hap = 0
       while i < 1001 :
              hap = hap + i
              if hap > 1000 :
                     print(" %d is the point hap is over 1000" % i)
                     print(" Total hap is %d " % hap)
                     break
              i += 2

