# ## 문제 5-7

#  * 함수의 인자로 시작과 끝을 나타내는 숫자를 받아 시작부터 끝까지의 모든 정수값의 합을 반환하는 함수를 작성하세요(시작값과 끝값을 포함).

# ```
# def add_start_to_end(start, end):
#     # 함수 구현

def add_start_to_end(start, end):
    sum = 0
    for i in range(start, end):
        sum += i
    return sum

in_value_start = int(input('start : '))
in_value_end = int(input('end : '))

print(add_start_to_end(in_value_start, in_value_end))