## 동전 교환 
## 함수 선언 ##
## 변수 선언 ##
## Main Code ##
if __name__ == "__main__" :
  inputCoin = int(input("교환할 금액 입력 : "))
  if inputCoin < 0 :
    print("교환 가능하지 않습니다. 금액을 입력 하여 주십시오")
  else :
    NumOf500Coin = int(inputCoin / 500)
    inputFor100Coin = inputCoin - NumOf500Coin * 500
    NumOf100Coin = int(inputFor100Coin / 100)
    inputFor10Coin = inputFor100Coin - NumOf100Coin * 100
    NumOf10Coin = int(inputFor10Coin / 10)
    UnchangedCoin = inputFor10Coin - NumOf10Coin * 10 
    print("500원짜리 ==> %d 개" % NumOf500Coin)
    print("100원짜리 ==> %d 개" % NumOf100Coin)
    print("10원짜리 ==> %d 개" % NumOf10Coin)
    print("우수리  ==> %d 원" % UnchangedCoin)
