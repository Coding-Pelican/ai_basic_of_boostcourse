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
