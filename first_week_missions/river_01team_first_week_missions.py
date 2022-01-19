# Q1 - Case 1
""" 
num_list = [1, 5, 7, 17, 16, 22, 28, 29]
def Get_Odd_Num(num_list):              # 함수 선언
    num_odd = []                        # Empty List 선언 (결과값 저장할)
    for num in num_list:
        if num % 2 != 0:                # 짝수 검사
            num_odd.append(num)         # 짝수가 아니면 Empty List(num_odd)에 추가
            print(num, " is odd.")      # Loop 검사를 위한 출력
        else:
            print(num, " is even.")
    print("EOP")
    return num_odd
# Get_Odd_Num(num_list)
print(Get_Odd_Num(num_list))
"""

# Q1 - Case 2
"""
is_odd = lambda num : num if(num % 2 is not 0) else 0
get_odd_num = lambda num_list : list(filter(lambda val: val is not value_to_be_removed, list(map(is_odd, num_list))))
value_to_be_removed = 0
num_list = [1, 5, 7, 15, 16, 22, 28, 29]
print(get_odd_num(num_list))
"""

# Q2 - Case 1
"""
sentence = "way a is there will a is there where"
def Reverse_Sentence1(sentence):                    # 함수 선언
    Before_Reverse = sentence.split()               # list로 받음
    After_Reverse = []                              # 재배치할 list 선언
    for item in Before_Reverse[::-1]:               # for문을 통한 list 역순배치
        After_Reverse.append(item)
        print(After_Reverse)                        # 디버깅을 위한 중간값 출력
    R_Sentence = " ".join(After_Reverse)
    return (R_Sentence)
print('"', Reverse_Sentence1(sentence), '"')
"""

# Q2 - Case 2
"""
sentence = "way a is there will a is there where"
def reverse_sentence(sentence):
  answer = sentence.split()
  answer.reverse()
  answer = " ".join(answer)
  answer = answer.capitalize()
  return answer
print(reverse_sentence(sentence))
"""

# Q2 - Case 3
"""
sentence = "way a is there will a is there where"
split_string = lambda string : string.split()
reverse_list = lambda original_list : list(reversed(original_list))
list_to_string = lambda original_list : " ".join(original_list)
reverse_sentence = lambda sentence : (list_to_string(reverse_list(split_string(sentence))))
print(reverse_sentence(sentence))
"""

# Q3 - Case 1
"""
score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]
def get_avg(score):
    Copy_Score = score
    AVG_Of_Score = []
    for i in range(len(Copy_Score)):
        AVG_Of_Score.append(0.5*(int(Copy_Score[i][0])+int(Copy_Score[i][1])))
        print(i+1, "번 평균 :", AVG_Of_Score[i])
        print("집계", AVG_Of_Score)
    return(AVG_Of_Score)
get_avg(score)
"""

# Q3 - Case 2
"""
score = [(100,100), (95,90), (55,60), (75,80), (70,70)]
def get_avg(score):
    number = 0
    for i in score:
        sum = i[0] + i[1]
        avg = sum / 2
        number += 1
        print(f"{number}번, 평균 : {avg}")
    return
get_avg(score)
"""

# Q3 - Case 3
"""
get_avg_of_list = lambda target_list : sum(target_list) / len(target_list)
get_avg_of_elements_of_2D_list = lambda target_list : list(map(lambda index: get_avg_of_list(target_list[index]), range(0, len(target_list))))
def get_avg(score):
    avg_of_list = list(enumerate(get_avg_of_elements_of_2D_list(score)))
    for element in avg_of_list:
        print("{} 번, 평균 : {}".format(element[0] + 1, element[1]))
    return None

score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]
get_avg(score)
"""

# Q4 - Case 1
"""
dict_1st = {'사과': 30, '배': 15, "감": 10, '포도': 10}
dict_2nd = {'사과': 5, '감': 25, "배": 15, "귤": 25}
def merge_dict(dict_1st, dict_2nd):
    Fruit_Stack = []
    Fruit_New = []
    dict_merge = dict_1st
    for key in dict_2nd:
        if key in dict_1st:
            print(key, "is stacked")
            Fruit_Stack.append(key)
            dict_merge[key] = dict_1st[key] + dict_2nd[key]
        else:
            print(key, "is new")
            Fruit_New.append(key)
            dict_merge[key] = dict_2nd[key]
    print("중복", Fruit_Stack)
    print("신규", Fruit_New)
    print("총계", dict_merge)
    return(Fruit_Stack, Fruit_New)
merge_dict(dict_1st, dict_2nd)
"""

# Q4 - Case 2
"""
dict_1st = {'사과': 30, '배': 15, "감": 10, '포도': 10}
dict_2nd = {'사과': 5, '감': 25, "배": 15, "귤": 25}
def merge_dict1(dict_1st, dict_2nd):
    dict_merge = {**dict_1st, **dict_2nd}
    dict_1st_re = {**dict_1st, **dict_2nd}
    dict_2nd_re = {**dict_1st, **dict_2nd}
    for key in dict_1st_re.keys():       # key 누락 없게 만들고, 0으로 초기화 후 dict_1st로 update
        dict_1st_re[key] = 0
        dict_1st_re.update(dict_1st)
    for key in dict_2nd_re.keys():    # key 누락 없게 만들고, 0으로 초기화 후 dict_2nd로 update
        dict_2nd_re[key] = 0
        dict_2nd_re.update(dict_2nd)
    for key in dict_merge.keys():    #  합 계산
        dict_merge[key] = dict_1st_re[key] + dict_2nd_re[key]
    return(dict_merge)
print(merge_dict1(dict_1st, dict_2nd)) 
"""

# Q4 - Case 3
"""
from collections import Counter
dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}
def merge_dict(dict_first, dict_second):
    counter1 = Counter(dict_first)
    counter2 = Counter(dict_second)
    dic_sum = dict(counter1 + counter2)
    result = sorted(dic_sum.items())
    result2 = dict(result)
    print(result2)
merge_dict(dict_first, dict_second)
"""

# Q5 - Case 1
"""
inputs = "cat32dog16cow5"
def find_strings(inputs):
    num = "0123456789"
    for i in range(len(num)):
        inputs = inputs.replace(num[i], " ")
    outputs = inputs.split()
    return (outputs)
string_list = find_strings(inputs)
print(string_list)
"""
