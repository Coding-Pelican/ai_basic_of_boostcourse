# Q1 Case - 1
"""
class Score:
    def __init__(self, mid, final):
        self.mid = mid
        self.final = final

def print_avg_of_score():
    score = Score(50,75)
    print((score.mid + score.final)/2)

print_avg_of_score()
"""

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
"""

# Q1 Case - 3 
