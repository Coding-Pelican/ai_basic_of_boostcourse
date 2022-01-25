# Q1 - Case 1
"""
def get_mid():
    mid = float(input("mid score :"))
    print("mid term score ", mid, "was enterd.")
    return mid

def get_final():
    final = float(input("final score:"))
    print("final term score ", final, "was enterd.")
    return final

mid = get_mid()
final = get_final()

class score:
    def __init__(self, mid, final):
        self.__mid = mid
        self.__final = final

    def cal_avg(self):
        avg = (self.__mid + self.__final)/2
        print("semester average :", avg)
        return avg

    def notify(self):
        print("mid term :", mid, "final term :", final)

    def mid(self):
        mid = self.__mid
        print("mid term score :", mid)
        return mid

    def final(self):
        final = self.__final
        print("final term score :", final)
        return final

result = score(mid, final)
result.cal_avg()
result.notify()
result.mid()
print(result.mid())
print(result.final())
print(result.mid()+result.final())
"""

# Q1 - Case 2
"""
class Score():
  def __init__(score, mid, final):
    score.mid = mid
    score.final = final
  
score = Score(50, 75)
print((score.mid + score.final) / 2)
"""

# Q1 - Case 3
"""
class Score():                      # Class 선언
    def __init__(self,mid,final):   # __init__ Method를 통해 Constructor 생성
        self.__mid = mid            # private mid 객체 변수 선언
        self.__final = final        # private final 객체 변수 선업   

    def average(self):                                  # 평균값 계산 Method 생성
        average = ((self.__mid + self.__final)/2)       # average 객체 변수에 평균값 계산 및 저장
        print(f'중간고사와 기말고사 평균값은 {average}입니다.') # 평균값 도출

def trace(func):                                    # 호출할 함수를 매개변수로 받음
        print(func.__name__, '점수를 입력해주세요.')    # __name__으로 함수 이름 출력
        func()                                      # 매개변수로 받은 함수를 호출

@trace
def 중간고사():                   # 중간고사 데코레이터
    global mid                  # mid 전역변수 지정
    mid = float(input())        # 중간고사 값 입력 및 저장
    return mid                  # mid 값 반환
@trace
def 기말고사():                   # 기말고사 데코레이터
    global final                # final 전역변수 지정
    final = float(input())      # 기말고사 값 입력 및 저장
    return final                # final 값 반환

score = Score(mid,final)
score.average()
"""

# Q2 - Case 1
"""
class car:
    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels

class bike (car):
    def __init__(self, fuel, wheels, size):
        super().__init__(fuel, wheels)
        self.size = size

BMW_m3 = car("gas", 4)
print("BMW_m3 :", BMW_m3.fuel, BMW_m3.wheels)

BMW_motorrad = bike("gas", 2, "small")
print("BMW_motorrad :", BMW_motorrad.fuel, BMW_motorrad.wheels, BMW_motorrad.size)
"""

# Q2 - Case 2
"""
class car():                                        # 상위클래스 생성
    def __init__(self, fuel, wheels):               # __init__ Method를 통해 Constructor 생성
        self.fuel = fuel                            # fuel 객체함수 선언
        self.wheels = wheels                        # wheels 객체함수 선언

class Bike(car):                                    # 하위클래스 생성
    def __init__(self, fuel, wheels, size):         # 기존 상위클래스 속성에 Size Constructor 생성
        car.__init__(self, fuel, wheels)            # 상위클래스 속성 가져옴
        self.size = size                            # Size 객체함수 선언

bike = Bike("gas", 2 , "small")                
print(bike.fuel, bike.wheels, bike.size)
"""

# Q3 - Case 1
"""
import pprint
dict_contents = {}
file_path = "./data-01-test-score.csv"
def file_read(file_path):
    with open(file_path, "r") as Origin:
        copy_list = Origin.readlines()
    for num in range(0, len(copy_list)):
        dict_contents[num+1] = copy_list[num].rstrip('\n')
    return dict_contents
read_csv = file_read(file_path)
pprint.pp(read_csv)
"""

# Q3 - Case 2
"""
file_path = "./data-01-test-score.csv"

class ReadCSV():                                        # ReadCSV Class 함수 선언
    def __init__(self, path):                           # __init__ Method를 통해 Constructor 생성
        self.path = path

    def read_file(self):                                # read_file 함수 선언
        with open(self.path, "r") as Test_result:       # open 함수를 통해 해당 CSV 파일 읽기
            line_counter = 0                            # 몇줄인지 Count 하기 위한 변수 생성
            data_list = []                              # Data 저장할 수 있는 List 생성
            while True:                                 # While 문 생성
                data = Test_result.readline()           # readline을 통해 Data를 변수에 값 저장
                if not data:                            # 만약 Data가 없는 경우 중지
                    break
                else:
                    data = data.rstrip('\n')            # 줄바꿈으로 생기는 \n 제거
                    data_list.append(data.split(","))   # ","를 기준으로 str 나눈 후, List 함수에 append
                    line_counter += 1                   # 한줄끝날때마다 Count
        for i in range(0, int(line_counter)):           # Data 저장한 List 도출
            print(data_list[i])

read_csv = ReadCSV(file_path)
read_csv.read_file()
"""

# Q4
"""
import csv
import pprint
file_path = "./data-01-test-score.csv"

class ReadCsv:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_read(self, file_path):
        with open(file_path, "r") as Origin_read:
            copy = csv.reader(Origin_read, delimiter=',',
                              lineterminator='\n', quotechar="'")
            read_list = []
            for line in copy:
                read_list.append(line)
        return read_list

    def file_merge(self, file_path):
        with open(file_path, "r") as Origin_merge:
            copy = csv.reader(Origin_merge, delimiter=',',
                              lineterminator='\n', quotechar="'")
            merge_list = []
            merge_sum = []
            for line in copy:
                merge_list.append(line)
            for i in range(len(merge_list)):
                merge_sum.append(float(
                    merge_list[i][0])+float(merge_list[i][1])+float(merge_list[i][2])+float(merge_list[i][3]))
        return merge_sum

read_csv = ReadCsv(file_path)
pprint.pp(read_csv.file_read(file_path))
pprint.pp(read_csv.file_merge(file_path))
""" 

# Q5
"""
import csv
import pprint
file_path = "./data-01-test-score.csv"

class ReadCsv:
    def __init__(self, file_path):
        self.file_path = file_path
    def file_read(self, file_path):
        with open(file_path, "r") as Origin_read:
            copy = csv.reader(Origin_read, delimiter=',', lineterminator='\n', quotechar="'")
            read_list = []
            for line in copy:
                read_list.append(line)
        return read_list
    def file_merge(self, file_path):
        with open(file_path, "r") as Origin_merge:
            copy = csv.reader(Origin_merge, delimiter=',', lineterminator='\n', quotechar="'")
            merge_list = []
            merge_mean = []
            for line in copy:
                merge_list.append(line)
            for i in range(len(merge_list)):
                merge_mean.append((float(merge_list[i][0])+float(merge_list[i][1])+float(merge_list[i][2])+float(merge_list[i][3]))/4)
            merge_mean.sort()
        return merge_mean
read_csv = ReadCsv(file_path)
pprint.pp(read_csv.file_merge(file_path)) 
""" 
