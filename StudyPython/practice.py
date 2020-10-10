# #숫자처리함수
from math import *
from random import *

print("절대값 : ", abs(-5)) # 절대값 구하기 
print("제곱 : ", pow(4,2)) # 4^2 
print("최대값 : ", max(1,10)) # 최대값 구하기
print("최소값 : ", min(1,10)) # 최소값 구하기


print("반올림 : ", round(3.14)) # 반올림
print("내림 : ", floor(3.14)) # 내림
print("올림 : ", ceil(3.14)) # 올림
print("제곱근 : ", sqrt(4)) # 제곱근 

print("랜덤 숫자 : ", random()) # 0.0~1.0 미만 임의의 값 생성
print("랜덤 숫자(int형) : ", int(random()))
print("랜덤 숫자[1-45] : ", int(random()*45)+1)
print("랜덤 숫자[1-45] : ", int(randint(1,45))) # 1~45이하 임의의 값 생성
print("랜덤 숫자[1-45] : ", int(randrange(1,46))) #1~45미만 임의의 값 생성

# 문자열 
sentence = "문자열 처리에 대해 알아보기"
print(sentence)
section = """
    다중 문자열을 넣어보기
    헛 둘 셋 넷
"""
print(section)