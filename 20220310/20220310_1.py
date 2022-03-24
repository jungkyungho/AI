#day1 프로그램
a=[10, 20, 30]
print(a)

a=10
b=2000
a,b= b,a

a=[10, 20, 30]
b= a
a[0]=200
print(b)

print("a="+str(a))
print("a=",a)
print("a={}".format(a))

c=2
print("a={}, b={}, c={}".format(a,b,c))

print('hello', end='!!!')

a=123   
b='hello'
print(a, 456, b, 'world')

item1='사과'
price1= 1000
item2= '바나나'
price2= 500
str1= '{0}는 {1}원 입니다.'
str2= '%s는 %d원 입니다'

print(item, pricwe, sep=',', end='/')
print

print(str1.format(item1, price1))
print(str1.format(item2, price2))

print(str2%(item1, price1))
print(str2%(item2, price2))