# ## 문제 3-6
#  * 문제 3-1의 표 3.2를 이용해 날짜를 딕셔너리의 키 값으로, 종가를 딕셔너리의 값으로 사용해 naver_closing_price2라는 딕셔너리를 만드세요.

# | 날짜 | 요일 | 종가 |
# | 09/11 | 금 | 488,500 |
# | 09/10 | 목 | 500,500 |
# | 09/09 | 수 | 501,000 |
# | 09/08 | 화 | 461,500 |
# | 09/07 | 월 | 474,500 |

naver_closing_price = [474500, 461500, 501000, 500500, 488500]
naver_closing_price2 = {'Mon': None, 'Tue': None, 'Wed': None, 'Thu': None, 'Fri': None}

naver_closing_price2.update(Mon = naver_closing_price[0])
naver_closing_price2.update(Tue = naver_closing_price[1])
naver_closing_price2.update(Wed = naver_closing_price[2])
naver_closing_price2.update(Thu = naver_closing_price[3])
naver_closing_price2.update(Fri = naver_closing_price[4])

print(naver_closing_price2)