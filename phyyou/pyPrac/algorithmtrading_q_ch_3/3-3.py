# ## 문제 3-3
#  * 문제 3-1에서 만든 naver_closing_price를 이용해 해당 주에 종가를 기준으로 가장 낮았던 가격을 출력하세요. 
# (힌트: 리스트에서 최솟값을 찾는 함수는 min()이고, 화면에 출력하는 함수는 print()입니다.)

naver_closing_price = [474500, 461500, 501000, 500500, 488500]
min_NCP = min(naver_closing_price)
print(min_NCP)