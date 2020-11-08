'''
Quiz2) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다. 
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오. 

조건 1: 랜덤으로 날짜를 뽑아야함. 
조건 2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건 3: 매월 1~3일은 스터디 준비를 해야 므로 제외 

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다. 

from random import *
dday = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월",dday,"일로 선정되었습니다.")



=================================================================================
Quiz3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
예) http://naver.com

규칙1 : http://부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 '2' 갯수 + "!" 로 구성 

url="http://naver.com"
rule1=6
rule2=url.find(".")
result=url[7:rule2]
password=result[0:3]+str(len(result))+str(result.count("e"))+"!"
print("생성된 비밀번호 : %s" %password)



### 정답풀이
url="http://naver.com"
my_str=url.replace("http://","") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url,password))




=================================================================================
Quiz4) 당신의 학교에서는 파있너 코딩 대회를 주최합니다. 
    참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
    댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
    추첨 프로그램을 작성하시오.

    조건1 : 편의상 댓글을 20명이 작성하였고, 아이디는 1~20이라고 가정 
    조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가 
    조건3 : random 모듈의 shuffle과 sample을 활용 

    (출력 예제)
    -- 당첨자 발표 -- 
    치킨 당첨자 : 1
    커피 당첨자 : [2,3,4]
    -- 축하합니다. --


from random import *

ids=list(range(1,21)) # 조건 1
shuffle(ids) # 무작위로 추첨 

chiken=sample(ids, 1).pop() #치킨 당첨자
ids.remove(chiken) #치킨 당첨자 제외 

shuffle(ids) # 무작위로 추첨 
coffe=sample(ids, 3)
print(ids)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(chiken))
print("커피 당첨자 : {}".format(coffe))
print("-- 축하합니다. --")


### 정답풀이
from random import *
ids=list(range(1,21)) # 조건 1
shuffle(ids) # 무작위로 추첨 

winners=sample(ids, 4) # 4명을 일괄 뽑기

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다. --")



=================================================================================
Quiz) 당신은 CoCoa 서비스를 이용하는 택시 기사님입니다. 50명의 승객과 매칭 기회가 있을때 총 탑승 승객수를 구하는 프로그램을 작성해보세요. 
조건 1: 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다. 
조건 2: 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 합니다. 

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[] 2번째 손님 (소요시간 : 15분)
[] 3번째 손님 (소요시간 : 15분)
[0] 4번째 손님 (소요시간 : 15분)



from random import *

result=0
maxtime=15
mintime=5

for person in range(1,51):
    time = randint(5,50)

    if 15>= time >=5:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(person,time))
        result=result+1 #result+=1
    else: 
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(person,time))

print("총 탑승 승객 : {0}".format(result))
    




Quiz) 표준 체중을 구하는 프로그램을 작성하시오. 
* 표준 체중 : 각 개인의 키에 적당한 체중 

(성별에 따른 공식)

남자 : 키(m) X 키(m) X 22
여자 : 키(m) X 키(m) X 21

조건 1: 표준 체중은 별도의 함수 내에서 계산 
    * 함수명 : std_weight
    * 전달 값 : 키(height), 성별(gender)
조건 2: 표준 체중은 소수점 둘째자리까지 표시 


(출력 예재)
키 175cm 남자의 표준 체중은 67.38kg



def std_weight(height, gender):
    result = 0
    if gender == "남자":
        result = (height/100) * (height/100) * 22    # height*height*22
    elif gender == "여자":
        result =  (height/100) * (height/100) * 21
    else:
        print("잘못 입력하였습니다. 다시 진행해주세요")
        return
    return result


height = input("키를 입력해주세요 cm로 기입: ")
gender = input("성별을 입력해주세요 : ")
std_weight = std_weight(int(height), gender)  #std_weight(int(height)/100, gender) 

#std_weight = round(std_weight(int(height)/100, gender),2)

print("키 {0}cm의 {1}의 표준 체중은 {2:.2f}kg".format(height,gender,std_weight))



Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다. 보고서는 항상 아래와 같은 형태로 출력되어야 합니다. 

-X 주차 주간보고 - 
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오. 

조건 : 파일명은 '1주차.txt .... 이런식으로 만드세요 '


for count in range (1,6):
    filename = str(count)+"주차.txt"
    with open(filename,"w",encoding="utf-8") as report_file:   #    with open(str(i)+"주차.txt","w",encoding="utf-8") as report_file:
        report_file.write("- {0} 주차 주간보고 -\n".format(count)) 
        report_file.write("부서 : \n이름 : \n업무 요약 : \n")


Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오. 

(출력 예제)
총 3대의 매물이 있습니다. 
강남 아파트 매매 10억 2010년 
마포 오피스텔 전세 5얼 2007년 
송파 빌라 월세 500/50 2000년

[코드]


class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.deal_type, self.completion_year)


h1 = House("강남","아파트","매매","10억","2010년")
h2 = House("마포","오피스텔","전세","5억","2007년")
h3 = House("송파","빌라","월세","500/50","2000년")

house_list = []
house_list.append(h1)
house_list.append(h2)
house_list.append(h3)

print ("총 {0}대의 매물이 있습니다.".format(len(house_list)))
for house in house_list:
    house.show_detail()


Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다. 
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다. 
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오. 

조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리 
    출력 메세지 : "잘못된 값을 입력하였습니다"
조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
    치킨 소진 시 사용자 정의 에러 [soldouterror]를 발생시키고 프로그램을 종료
    출력 메세지 : "재고가 소진 되어 더이상 주문을 받지 않습니다."

[코드]



class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg


chicken = 10
waiting = 1 # 홀 안에는 현재 만석, 대기 번호 1부터 시작

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까? :"))
    
        
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <=0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken ==0 :
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")

    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as err:
        print(err)
        break

'''
class SoldOutError(Exception):
    pass


chicken = 10
waiting = 1 # 홀 안에는 현재 만석, 대기 번호 1부터 시작

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까? :"))
    
        
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <=0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken ==0 :
            raise SoldOutError

    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break


