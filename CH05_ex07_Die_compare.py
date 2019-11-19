## Dice Compare ##
import random

## 함수 선언 ##

## 변수 선언 ##
dice1, dice2, dice3, dice4, dice5, dice6 = 1, 1, 1, 1, 1, 1
count, count6 = 0, 0


## Main Code ##
if __name__ == "__main__" :

##  example 7 ##    
##  두 개의 주사위에서 나온 결과를 비교하여 주사위 결과 크기 비교  ##
    dice1 = random.randrange(1,6)
    dice2 = random.randrange(1,6)

    if dice1 == dice2 :
        print("주서위 A 와 주사위 B는 비겼습니다. A %d  B %d" % (dice1, dice2))
    elif dice1 > dice2 :
        print("주서위 A 가 이겼습니다. A %d  B %d" % (dice1, dice2))
    else :
        print("주사위 B 가 이겼습니다.A %d  B %d" % (dice1, dice2))

        
##  example 5-1 ##    
##  6개의 주사위를 던져 같은 숫자가 나올 때까지 무한 반복해서 던진다. ##
##  그 때까지 몇 회 그리고 1 에서 6까지 연속된 숫자는 몇 번 나왔나요  ##
    while True :

        count += 1
        
        dice1 = random.randrange(1,7)
        dice2 = random.randrange(1,7)
        dice3 = random.randrange(1,7)
        dice4 = random.randrange(1,7)
        dice5 = random.randrange(1,7)
        dice6 = random.randrange(1,7)

        if dice1 == dice2 == dice3 == dice4 == dice5 == dice6 :
            print(" 6개의 숫자가 모두 동일하게 숫자가 나옴 --> %d %d %d %d %d %d %d ", dice1, dice2, dice3, dice4, dice5, dice6)
            break
        elif (dice1 == 1 or dice2 == 1 or dice3 == 1 or dice4 == 1 or dice5 == 1 or dice6 == 1) and \
             (dice1 == 2 or dice2 == 2 or dice3 == 2 or dice4 == 2 or dice5 == 2 or dice6 == 2) and \
             (dice1 == 3 or dice2 == 3 or dice3 == 3 or dice4 == 3 or dice5 == 3 or dice6 == 3) and \
             (dice1 == 4 or dice2 == 4 or dice3 == 4 or dice4 == 4 or dice5 == 4 or dice6 == 4) and \
             (dice1 == 5 or dice2 == 5 or dice3 == 5 or dice4 == 5 or dice5 == 5 or dice6 == 5) and \
             (dice1 == 6 or dice2 == 6 or dice3 == 6 or dice4 == 6 or dice5 == 6 or dice6 == 6) :
            print(" 6개의 숫자가 1-6 의 연속 숫자가 나옴 --> %d %d %d %d %d %d %d ", dice1, dice2, dice3, dice4, dice5, dice6)
            count6 +=1

    print(" 6개가 동일한 숫자가 나올 때까지의 카운트 --> %d " % count)
    print(" 6개의 동일한 숫자가 나올 때까지 1-6의 연속 숫자가 너온 횟수 --> %d " % count6 )
        
        
