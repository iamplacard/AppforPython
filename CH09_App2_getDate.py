##  날짜 세기 및 요일 구하기
'''
입력한 날짜에서 현재 날짜가지 며칠이 지났는 지 날짜 수를 세는 프로그램을 만든다.
추가로 현재 날짜에 해당하는 요일도 출력한다. '''

from time import *
from datetime import *

# 함수
def countDays(date1, date2) :
    retDays = 0
    year, month, day = date1.split('/')
    sDays = date(int(year), int(month), int(day))
    year, month, day = date2.split('/')
    eDays = date(int(year), int(month), int(day))
    diffDays = eDays - sDays
    retDays = diffDays.days
    return retDays

def getDays(t) :
    weeks = ['월', '화', '수', '목', '금', '토', '일']
    return weeks[t.tm_wday]

#  변수
startDate, curDate, tm = '','',None

## Main 함수
if __name__ == '__main__' :
    startDate = input("시작 날짜(년/월/일) --> ")
    tm = localtime()
    curDate = str(tm.tm_year) + '/' + str(tm.tm_mon) + '/' + str(tm.tm_mday)

    print(startDate, '부터 오늘 (', curDate,')까지는 ', countDays(startDate,curDate), '일이 지났습니다.')
    print("오늘은 %s요일 입니다."%getDays(tm))
