#Q1. 
#파이썬에서는 리스트 형태의 데이터를 자주 사용합니다. 그래서 리스트 를 잘 다루는 것이 중요한데, 다음으로 주어진 리스트 데이터를 다뤄봅시다.😎
#다양한 데이터를 수집해서 아래와 같은 num_list를 얻었습니다.
#하지만 우리에게 필요한 데이터는 홀수 데이터입니다.
#그렇다면 num_list 가 홀수인 데이터만 출력하도록 하는 함수를 작성해보세요.

is_odd = lambda num : num if(num % 2 is not 0) else 0
get_odd_num = lambda num_list : list(filter(lambda val: val is not value_to_be_removed, list(map(is_odd, num_list))))
value_to_be_removed = 0
num_list = [1, 5, 7, 15, 16, 22, 28, 29]
print(get_odd_num(num_list))
