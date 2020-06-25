# ## 문제 3-7
#  * 문제 3-6에서 만든 naver_closing_price2 딕셔너리를 이용해 09/09일의 종가를 출력하세요.

# | 날짜 | 요일 | 종가 |
# | 09/11 | 금 | 488,500 |
# | 09/10 | 목 | 500,500 |
# | 09/09 | 수 | 501,000 |
# | 09/08 | 화 | 461,500 |
# | 09/07 | 월 | 474,500 |

naver_closing_price = [474500, 461500, 501000, 500500, 488500]
naver_closing_price2 = {'09/07': naver_closing_price[0], '09/08': naver_closing_price[1], '09/09': naver_closing_price[2], '09/10': naver_closing_price[3], '09/11': naver_closing_price[4]}

print(naver_closing_price2['09/09'])