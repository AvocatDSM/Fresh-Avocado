# ## 문제 5-8

#  * 함수의 인자로 문자열을 포함하는 리스트가 입력될 때 각 문자열의 첫 세 글자로만 구성된 리스트를 반환하는 함수를 작성하세요. 
#  예를 들어, 함수의 입력으로 ['Seoul', 'Daegu', 'Kwangju', 'Jeju']가 입력될 때 함수의 반환값은 ['Seo', 'Dae', 'Kwa', 'Jej']입니다.

def __3_letter_list(temp_list):
    ret_list = []
    for i in temp_list:
        ret_list.append(i[0:3])
    return ret_list

in_list = ['Seoul', 'Daegu', 'Kwangju', 'Jeju']

for list_data in __3_letter_list(in_list):
    print(list_data)
