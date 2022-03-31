#문제1
price_list = [32100, 32150, 32000, 32500]
for i in range(4):
    print(i, price_list[i])

#문제2
for i in range(1,4):
    print(90+10*i, price_list[i])

#문제3
for i in range(2002, 2050, 4):
    print(i)

#문제4
for i in range(10):
    print(i/10)

#문제5
ticker = "btc_krw"
print(ticker.upper())

#문제6
file_name = '보고서.xlsx'
print(file_name.endswith('xlsx'))

#문제7
a = "hello world"
a.split()

#문제8
date = "2020-05-01"
a.split('-')


#문제9
상장주식수 = "5,969,782,550"
print(int(상장주식수.replace(',', '')))

#문제10
a = "hello world"
a.split()

#문제11
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:7])

#문제12
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])

#문제13
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i %3 ==0:
        print(i)
