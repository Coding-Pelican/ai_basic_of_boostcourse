"""
Q2. 
데이터 처리를 위해서 문자열을 입력받았습니다. 그런데, 문자열을 받았 더니 단어 단위로 거꾸로 입력되었습니다. 이를 다시 원래대로 출력하는 함수 를 작성해보세요.😎
string 문장을 받아 단어를 역순으로 출력하는 함수를 작성하세요.
string 연산을 이용해보세요.
"""

sentence = "way a is there will a is there where"
split_string = lambda string : string.split()
reverse_list = lambda original_list : list(reversed(original_list))
list_to_string = lambda original_list : " ".join(original_list)
reverse_sentence = lambda sentence : (list_to_string(reverse_list(split_string(sentence))))
print(reverse_sentence(sentence))
