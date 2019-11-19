## 동전 교환 
## 함수 선언 ##
## 변수 선언 ##
## Main Code ##
if __name__ == "__main__" :
  inputCoin = int(input("교환할 금액 입력 : "))
  if inputCoin < 0 :
    print("교환 가능하지 않습니다. 금액을 입력 하여 주십시오")
  else :
    NumOf50000bil = int(inputCoin / 50000)
    inputFor10000bil = inputCoin - NumOf50000bil * 50000
    NumOf10000bil = int(inputFor10000bil / 10000)
    inputFor5000bil = inputFor10000bil - NumOf10000bil * 10000
    NumOf5000bil = int(inputFor5000bil / 5000)
    inputFor1000bil = inputFor5000bil - NumOf5000bil * 5000
    NumOf1000bil = int(inputFor1000bil / 1000)
    inputFor500Coin = inputFor1000bil - NumOf1000bil * 1000
    NumOf500Coin = int(inputFor500Coin / 500)
    inputFor100Coin = inputFor500Coin - NumOf500Coin * 500
    NumOf100Coin = int(inputFor100Coin / 100)
    inputFor10Coin = inputFor100Coin - NumOf100Coin * 100
    NumOf10Coin = int(inputFor10Coin / 10)
    UnchangedCoin = inputFor10Coin - NumOf10Coin * 10 
    print("50000원짜리 ==> %d 개" % NumOf50000bil)
    print("10000원짜리 ==> %d 개" % NumOf10000bil)
    print("5000원짜리 ==> %d 개" % NumOf5000bil)
    print("1000원짜리 ==> %d 개" % NumOf1000bil)
    print("500원짜리 ==> %d 개" % NumOf500Coin)
    print("100원짜리 ==> %d 개" % NumOf100Coin)
    print("10원짜리 ==> %d 개" % NumOf10Coin)
    print("우수리  ==> %d 원" % UnchangedCoin)


## '/' 나누기   '//' 나누기(몫)   '%%' 나머지값  
