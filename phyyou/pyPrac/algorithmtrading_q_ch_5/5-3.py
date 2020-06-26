# ## 문제 5-3

#  * 절대 경로를 입력받은 후 해당 경로에 있는 *.txt 파일의 목록을 파이썬 리스트로 반환하는 함수를 작성하세요.
# 응 싫어 py 파일 리스트 반환할꺼야
# ```
# def get_txt_list(path):
#     # 함수 구현
# ```

import os

def get_py_list(path):
    all_path_file_li = os.listdir(path)
    retu_li = []
    for x in all_path_file_li:
        if x.endswith('py'):
            retu_li.append(x)
    return retu_li 

print(get_py_list('C:\\Users\\user\\Documents\\Programming\\Avocat\\phyyou\\pyPrac\\algorithmtrading_q_ch_5'))