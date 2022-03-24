# 문제1
letters = 'python'
print(letters[0], letters[3])

#문제2
string = 'PYTHON'
re_name = ''
for i in string:
    re_name = i + re_name

print(f'name    : {string}')
print(f'reverse : {re_name}')

#문제3
url = input("url을 입력하시오: ")
url_split = url.split('.')
domain = url_split[-1]
print(domain)

#문제4
file_name = '보고서.xlsx'
x = file_name.endswith('.xlsx')
print(x)

#문제5
file_name = "2020_보고서.xlsx"
x = file_name.startswith('2020')
print(x)

#문제6
score = int(input('점수를 입력하시오: '))
if (score <= 100 and score >80):
    print('학점: A')
elif (score <= 80 and score >60):
    print('학점:B')
elif (score <= 60 and score >40):
    print('학점:C')
elif (score <= 40 and score >20):
    print('학점:D')
elif (score <= 20 and score >=0):
    print('학점:E')
else:
    print('다시입력하시오')
    score = input('점수를 입력하시오: ')

#문제7
cook = ["피자", "김밥", "양념치킨", "족발", "김치만두", "쫄면", "소시지", "라면", "핕빙수", "김치전"]
x = len(cook)
print(x)

#문제8
x = input("종목명을 입력하시오: ")
warn_investment_lisk = ["Microsoft", "Google", "Naver", "SAMSUNG", "LG"]
if x in warn_investment_lisk:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

#문제9
리스트 = [100, 200, 300]
for 원가 in 리스트:
    정가 = 원가 + 10
    print(정가)

#문제10
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for 종목 in 리스트:
    length = len(종목)
    print(length)

