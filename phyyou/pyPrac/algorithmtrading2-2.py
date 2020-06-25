# 문제 2-2 문제 2-1에서 구한 주식 총액에서 다음과 네이버의 주가가 각각 5%, 10% 하락한 경우에 손실액을 구하는 프로그램을 작성하세요.

stockpriceDaum = 89000
stockpriceNaver = 751000
posStockDaum = 100
posStockNaver = 20

stockpriceDaum = stockpriceDaum * 0.95
stockpriceNaver = stockpriceNaver * 0.9

stockpriceSum = (stockpriceDaum * posStockDaum) + (stockpriceNaver * posStockNaver)
print(stockpriceSum)
