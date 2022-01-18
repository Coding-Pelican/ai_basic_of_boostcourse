# Q3.
get_avg_of_list = lambda list : sum(list) / len(list)
get_avg_of_elements_of_2D_list = lambda target_list : list(map(lambda index: get_avg_of_list(target_list[index]), range(0, len(target_list))))
def get_avg(score):
    avg_of_list = list(enumerate(get_avg_of_elements_of_2D_list(score)))
    for element in avg_of_list:
        print("{} 번, 평균 : {}".format(element[0] + 1, element[1]))
    return None

score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]
get_avg(score)
