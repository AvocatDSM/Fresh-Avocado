# ## 문제 5-6

#  * 삼각형의 밑변과 높이를 입력받은 후 삼각형의 면적을 계산하는 함수를 작성하세요.

# ```
# def get_triangle_area(width, height):
#     # 함수 구현
# ```

def get_triangle_area(width, height):
    return (width * height) / 2

in_width = int(input('width : '))
in_height = int(input('height : '))

print(get_triangle_area(in_width, in_height))