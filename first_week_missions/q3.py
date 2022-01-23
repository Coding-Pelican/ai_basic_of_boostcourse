"""
Q3. 
이번 학기의 중간고사, 기말고사 점수가 발표되었습니다. 각 학생들의 점 수가 튜플 형태로 저장되어 있고, 이를 포함한 리스트가 있습니다. 이를 이용 해 각 학생들의 평균 점수를 출력하는 함수를 제작하세요. 😎
리스트와 반복문을 사용해 데이터를 불러오세요.
이를 이용해 각 학생별 평균을 구해보세요
"""

get_avg_of_list = lambda list : sum(list) / len(list)
get_avg_of_elements_of_2D_list = lambda target_list : list(map(lambda index: get_avg_of_list(target_list[index]), range(0, len(target_list))))
def get_avg(score):
    avg_of_list = list(enumerate(get_avg_of_elements_of_2D_list(score)))
    for element in avg_of_list:
        print("{} 번, 평균 : {}".format(element[0] + 1, element[1]))
    return None

score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]
get_avg(score)
# Q1 Case - 1

class Score:
    def __init__(self, mid, final):
        self.mid = mid
        self.final = final

def print_avg_of_score():
    score = Score(50,75)
    print((score.mid + score.final)/2)

print_avg_of_score()


# Q1 Case - 2
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

# Q1 Case - 3 
"""
