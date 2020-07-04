# ## 문제 3-4
#  * 문제 3-1에서 만든 naver_closing_price를 이용해 해당 주에서 가장 종가가 높았던 요일과 가장 종가가 낮았던 요일의 가격 차를 화면에 출력하세요.

naver_closing_price = [474500, 461500, 501000, 500500, 488500]
min_NCP = min(naver_closing_price)
max_NCP = max(naver_closing_price)
print(max_NCP - min_NCP)