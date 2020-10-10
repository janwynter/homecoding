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


# 문자열 함수
python = "Python is Amazing"
print("소문자 :", python.lower())
print("대문자 :", python.upper())
print("맨 앞자리 대문자 여부 :", python[0].isupper())
print("글자 길이 :", len(python))
print("글자 치환 :", python.replace("Python","Java"))

print("글자 n위치 확인 :", python.index("n")) # n이 어디있는지 위치 찾기
print("글자 n위치 확인(특정 위치 이후부터) :", python.index("n",6))

print(python.find("is"))
print("매칭되는 n글자 수 :",python.count("n"))


# 문자열 포멧
print("나는 %d살입니다." % 20)
print("나는 %s살입니다." % 20)
print("Apple의 첫 글자는 %c입니다." % "A")
print("나는 %s의 %s를 좋아합니다." %("BTS","모든 멤버"))

## 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}의 {}를 좋아합니다.".format("BTS","모든 멤버"))
print("나는 {1}의 {0}를 좋아합니다.".format("BTS","모든 멤버"))

## 방법 3
print("나는 {age}이며, {like}를 좋아해요.".format(age=20, like="bts"))

## 방법 4
age=20
like="bts"
print(f"나는 {age}살이며, {like}를 좋아해요.")



###### 리스트 []
subway =[10,20,30]
print(subway)

subway=["유재석","박명수","조세호"]

# 박명수의 위치
print(subway.index("박명수"))

# 다음 역에서 하하가 탑승
subway.append("하하")
print(subway)

# 유재석하고 박명수 사이에 넣기
subway.insert(1,"비")
print(subway)

# 지하철에 있는 사람을 한명씩 꺼냄
print(subway.pop())
print(subway)

# 정렬
num_list=[5,2,6,1,10]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
num_list.clear()
print(num_list)

mix_list = ["백지혜", 10, 30, True]
mix_list.reverse()
print(mix_list)

# 리스트 확장 
num_list = [1,33,26,13,255]
num_list.extend(mix_list)
print(num_list)


### 사전
cabinet = {"A-3":"유재석", "B-300":"서장훈"}
print(cabinet)
print(cabinet["A-3"])
cabinet["D-33"] = "박명수"
cabinet["A-1"]="하하"
print(cabinet)

cabinet["A-3"]="비"
print(cabinet)

del cabinet["B-300"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()

print(cabinet)



### 튜플
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])
#menu.add("생선까스") #튜플은 추가가 안됨

(name, age, hobby) = ("제제", 30, "컴퓨터")
print(name,age,hobby)


### 집합 (set) 중복이 안되고, 순서가 없음. 
my_set = {1,2,3,3}
print(my_set)

java = {"유재석","하하","박명수"}
python = set(["유재석","하하","서장훈"])

# 교집합
print(java & python)
print(java.intersection(python)) #교집합

# 합집합
print(java | python)
print(java.union(python)) #합집합

# 차집합 (java는 할수 있지만 python을 모르는 개발자)
print(java-python)
print(java.difference(python))

python.add("김태호")
print(python)

python.remove("하하")
print(python)



### 자료 구조의 변경 
menu = {"커피","우유","주스"}
print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))

menu = tuple(menu)
print(menu,type(menu))




## 조건문 IF
weather = input("오늘 날씨는 어때요 :")
if weather == "비" or weather=="눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")



temp = int(input("기온은 어때요 :"))

if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <=temp and temp <30:
    print("괜찮은 날씨에요")
elif 0 <=temp and temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")



##반복문
for waiting_no in range(1,11):
    print("대기번호: {0}".format(waiting_no))



customer="토르"
index=5

while index >0:
    print("{0}손님 커피 나왔습니다. {1}".format(customer,index))
    index -=1
    if index==0:
        print("폐기되었습니다")
