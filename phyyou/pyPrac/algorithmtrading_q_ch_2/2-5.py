# 문제 2-5 월요일에 네이버의 주가가 100만 원으로 시작해 3일 연속으로 하한가(-30%)를 기록했을 때 수요일의 종가를 계산해 보세요.

mon_start_stkPriceNaver = 1000000
mon_end_stkPriceNaver = mon_start_stkPriceNaver * 0.7

tues_start_stkPriceNaver = mon_end_stkPriceNaver
tues_end_stkPriceNaver = tues_start_stkPriceNaver * 0.7

wed_start_stkPriceNaver = tues_end_stkPriceNaver
wed_end_stkPriceNaver =wed_start_stkPriceNaver * 0.7

print(wed_end_stkPriceNaver)                                            