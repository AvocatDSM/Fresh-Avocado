# ## 문제 4-5
#
#  * 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.
#
#     *
#    **
#   ***
#  ****
# *****

for i in range(0, 5):
    for j in range(0, 4 - i):
        print(" ", end = '')
    for j in range(0, i + 1):
        print("*", end = '')
    print("")