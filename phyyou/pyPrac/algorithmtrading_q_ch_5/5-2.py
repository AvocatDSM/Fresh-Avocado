# ## 문제 5-2

#  * 함수의 인자로 리스트를 받은 후 리스트 내에 있는 모든 정수 값에 대한 최댓값과 최솟값을 반환하는 함수를 작성하세요.

# ```
# def get_max_min(data_list):
#     # 함수 구현
# ```

def get_max_min(data_list):
    retn_max = max(data_list)
    retn_min = min(data_list)
    return (retn_max, retn_min)

ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
(ex_list_max, ex_list_min) = get_max_min(ex_list)
print(ex_list_max, ex_list_min)