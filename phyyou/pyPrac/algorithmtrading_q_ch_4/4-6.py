# ## 문제 4-6
#
#  * 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
# ```python
# *****
#  ****
#   ***
#    **
#     *
# ```


for i in range(0, 5):
    for j in range(0, i):
        print(" ", end = '')
    for j in range(0, 5 - i):
        print("*", end = '')
    print("")