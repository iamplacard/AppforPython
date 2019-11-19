## dictionary 연습

## 변수 선언 ##
foods = {"떡볶이" : "오뎅",
         "짜장면" : "단무지",
         "라면" : "김치",
         "피자" : "피클",
         "맥주" : "땅콩",
         "치킨" : "치킨 무",
         "삼겹살" : "상추"};
         
## 함수 선언 ##

## Main Code ##
if __name__ == "__main__" :
    while True :
        myFood = input(str(list(foods.keys())) + "중 좋아하는 음식은?")

        if myFood in foods :
            print("%s 궁합 음식은 %s 입니다." % (myFood, foods.get(myFood)))
        elif myFood == '끝' :
            break
        else:
            print("그런 음식이 없습니다. 확인해 보세요.")



