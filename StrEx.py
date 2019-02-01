# This is file for training String Class
import sys

print("This file is for training String Class")

# str 문자열을 다루는 기본 클래스이다.이는 특별한 클래스를 import 할 필요가 없다.
# Capitalize() - 문장이나 단어의 첫번째 문자를 대문자로 한다.
a = 'PYTHON'.capitalize()
print(a)
a = "python is powerful".capitalize()
print(a)

# count(keyword, [start,[end]]) - string 내에 포함되어 있는 keyword 문자의 수
# start 는 문장에서의 문자 개수 측정 시작 시점, end 는 끝 지점.
a = "python is powerful".count('p') # 2
print(a)
a = "python is powerful".count('p',3) # 1
print(a)
a = "python is powerful".count('py')  # 1
print(a)
a = "python is powerful".count('')  # 19
print(a)
a = "python is powerful".count(' ') # 2
print(a)
a = "python is powerful".count('p', 0, -1) # 2 start 가 0 이고, 전체를 한 바퀴 돌아 처음으로
print(a)

# encode 사용 법  encode([encoding, [errors]])
a = "가나다".encode('cp949')   # 윈도우에서 사용하는 'CP949' 로 변환
print(a)
a = "가나다".encode('utf-8')   # 'UTF-8' 로 변환
print(a)
# encode 사용 법  - errors
# a = "가나다 abc".encode('latin1','strict')
# print(a)
a = "가나다 abc".encode('latin1','ignore')
print(a)
a = "가나다 abc".encode('latin1','replace')
print(a)
a = "가나다 abc".encode('latin1','xmlcharrefreplace')
print(a)
a = "가나다 abc".encode('latin1','backslashreplace')
print(a)

# endswith(postfix, [start,[end]]) 활용 법 - 찾고자 하는 문자로 끝이 났느냐? 확인.
a = "python is powerful".endswith('ful')  # 'ful' 이라는 문자열이 이 문장에 있는가 - Bool
print(a)
a = "python is powerful".endswith('ful',5)  # start 활용
print(a)
a = "python is powerful".endswith('ful',5, -1)  # start / end 활용
print(a)
a = "python is powerful".endswith('ful',0, -1)
print(a)
a = "python is powerful".endswith(('m','l'))  # 'm','l' 로 끝이 난 것인가?
print(a)
a = "python is powerful".endswith(('m','s'))  
print(a)

# expandtabs(tabsize]) - 문자열 사이에 tab 을 추가 하고, 그 atb 의 사이즈를 지정 가능 하다.
a = "python\tis\tpowerful"
print(a)
a = "python\tis\tpowerful".expandtabs()
print(a)
a = "python\tis\tpowerful".expandtabs(2)
print(a)
a = "python\tis\tpowerful".expandtabs(1)
print(a)

# find(keyword, [start,[end]]) - keyword 를 찾아 위치를 알려준다. 
a = "python is pwoerful".find('p')
print(a)
a = "python is pwoerful".find('p', 5)
print(a)
a = "python is pwoerful".find('p',5, -1)
print(a)
a = "python is pwoerful".find('p', 0, -1)
print(a)
a = "python is pwoerful".find('pa') # keyword 를 찾지 못하는 경우 '-1' return
print(a)

# index(keyword, [start, [end]]) - 찾고자 하는 문자열이 있는 위치의 index
a = "python is pwoerful".index('p')
print(a)
a = "python is pwoerful".index('p', 5)
print(a)
a = "python is pwoerful".index('p',5, -1)
print(a)
a = "python is pwoerful".index('p', 0, -1)
print(a)
# a = "python is pwoerful".index('pa') # keyword 를 찾지 못하는 경우에는 error message들이 나온다.. 
                                     # 이 경우 Error 처리를 어떻게 해야 하나?


# isalnum()  - Bool return - Is this alphbet or num ? 알파벳과 숫자만으로 이루어 진것인가?
a = "python".isalnum()
print(a)
a = "python3302".isalnum()
print(a)
a = "python3.2".isalnum()
print(a)

# isalpha()  - Bool return - Is this alphbet? 알파벳만으로 이루어 진것인가?
a = "python".isalpha()
print(a, "  python - isalpha()")
a = "Python3302".isalpha()
print(a,"   Python3302 - isalpha()" )
a = "python3.2".isalpha()
print(a, "  python3.2 - isalpha()")

# islower()  - Bool return - Is this lower alphbet? 알파벳 소문자 만으로 이루어 진것인가?
a = "python".islower()
print(a, "  python - islower()")
a = "Python3302".islower()
print(a,"   Python3302 - islower()" )
a = "python3.2".islower()
print(a, "  python3.2 - islower()")

# isspace()  - Bool return - Is this space? Space 만으로 되어 있는가?
a = "".isspace()
print(a, "- isspace()")
a = " ".isspace()
print(a," - isspace()" )
a = "\t\n".isspace()
print(a, "'\''t''\''n' - isspace()")
a = "\thi\n".isspace()
print(a, "'\''t''hi''\''n' - isspace()")

# istitle()  - Return Bool - Is this title? 타이틀인지 Check. 
a = "python is powerful".istitle()
print(a, "python is powerful - istitle()")
a = "Python is Powerful".istitle()
print(a, "Python is Powerful - istitle()")
a = "Python Is Powerful".istitle()
print(a, "Python Is Powerful - istitle()")  # 유일하게 True 이다.
a = "PYTHON IS POWERFUL".istitle()
print(a, "PYTHON IS POWERFUL - istitle()")


# isupper()  - Bool return - Is this upper alphbet? 알파벳 대문자 만으로 이루어 진것인가?
a = "python".isupper()
print(a, "  python - isupper()")
a = "Python".isupper()
print(a, "  Python - isupper()")
a = "PYTHON3302".isupper()
print(a,"   PYTHON3302 - isupper()" )
a = "PYTHON3.2".isupper()
print(a, "  PYTHON3.2 - isupper()")

# isdecimal(), isdigit()  - Bool return - Is this deciaml? 10진수인가?
a = "2590".isdecimal()
print(a, "2590 - isdecimal()")
a = "\u0699".isdecimal()
print(a,"\u0699","'\'u0699 - isdecimal()")
a = "\u00bc".isdecimal()
print(a,"\u00bc", "'\'u00bc - isdecimal()" )

# isnumeric()  - Bool return - Is this numeric? 숫자인가?
a = "\u00bc".isnumeric()
print(a,"\u00bc", "'\\'u00bc - isnumeric()")

# join()  - Return Joined String. (sequence)
a = ".".join('HOT')
print(a, "join()")
a = "\t".join(["Python","is","powerful"])
print(a)

# rstrip([chars]) - stripping space : rstrip ()은 문자열의 지정된 문자열의 끝을 (기본값은 공백입니다) 삭제합니다.
a = "python \t".rstrip()
print(a, " ::: rstrip example")
a = ">> python is powerful <<<".rstrip("<>")  # 설명이 좀 필요해요..
print(a, " ::: rstrip example")
a = "<< python is powerful >>>".rstrip("><")  # 설명이 좀 필요해요..
print(a, " ::: rstrip example")

# Istrip([chars]) - 문자열 왼쪽 공간을 자른다. 
a = "\t python".Istrip()
print(a)
a = ">>> python is powerful".Istrip(">")
print(a)
