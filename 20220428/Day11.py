from pickle import TRUE
import numpy as np
a = [[1,2,3,], [4,5,6]]
b = np.array(a)
print(a)

# 배열의 차원, 모양, 접근
print(b.ndim)
print(b.shape)
print(b[0,0])
print(b[0,1])

# 행렬 만들기
print(np.zeros((2,2)))
print(np.ones((2,3)))
print(np.full((2,3), 5))
print(np.eye(3))

# 행렬의 차원변화
a = np.arange(20)
print(a)
print(a.reshape(4,5))

# 행렬 슬라이싱, 인덱싱
lst = [ [1,2,3],
        [4,5,6],
        [7,8,9]]
arr = np.array(lst)
a = arr[0:2, 0:2]
print(a)
a = arr[1:, 1:]
print(a)
a = arr[1:2, 1:2]
print(a)

# 행렬의 연산
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a + b
print(c)
c = np.add(a,b)
print(c)
c = a * b
print(c)
c = np.multiply(a, b)
print(c)
c = a/b
print(c)
c = np.divide(a,b)
print(c)

arr1 = [[1,2],[3,4]]
arr2 = [[5,6], [7,8]]
a = np.array(arr1)
b = np.array(arr2)
c = np.dot(a,b)
print(c)

a = np.array([[-1,2,3],[3,4,8]])
s = np.sum(a)
print('sum=',a.sum())
print('sum by row=', a.sum(axis=0))
print('mean=', a.mean())
print('sd',a.std())
print('product', a.prod())



# 중복원소 제거
a = [1,2,3]
b = [4,5,6]
c = [1,2,3,1,2]
d = [3,3,4,5,6,6,6,7,8,8,9]
print(a)
print(b)
print(c)

new_c=[]
for i in c:
    if i not in new_c:
        new_c.append(i)
print(new_c)

new_d=[]
for i in d:
    if i not in new_d:
        new_d.append(i)
print(new_d)

# 합집학 구현
# 1.겹치는 원소X
a = [1,2,3]
b = [4,5,6]
c + a + b
print(c)
# 2. 겹치는 원소 O
e = [1,2,3]
f = [2,3,4,5,6]
k= []
for i in e:
    if i not in f:
        k.append(i)
print(k)
k = k+f
print(k)

# 연습문제 1) 두 집합 A={apple, melon, oreange}, 
#             B={chicken, pig, cow}의 합집합을 구하여라.
A=['apple', 'melon', 'oreange']
B=['chicken', 'pig', 'cow']
c = A + B
print(c)

# 교집합 구현
a = [1,2,3]
b = [2,3,4,5,6]
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)

# 차집합 구현
a = [1,2,3]
b = [2,3,4,5,6]
c = []
for i in a:
    if i not in b:
        c.append(i)
print(c)

# remove사용
a = [1,2,3]
b = [2,3,4,5,6]
c = a+[]
for i in b:
    if i in a:
        c.remove(i)
print(c)

# 여집합 사용
u = [1,2,3,4,5]
a =[1,2,3]
a_com = []
for i in u:
    if i not in a:
        a_com.append(i)
print(a_com)

u = [1,2,3,4,5]
a = [1,2,3]
rest = u + []
for i in u:
    if i in u:
        rest.remove(i)
print(rest)

# 소수
a = 17
a_prime = True
for i in range(2,a):
    if a % i == 0:
        a_prime == False
if a_prime == True:
    print('%d 는 소수이다' %a)
else:
    print('%d 는 소수가 아니다' %a)

# 약수찾기
a = 24
b = range(1,a)
factors = []
for i in b:
    if a % i == 0:
        factors.append(i)
factors.append(a)
print(factors)

# 최대공약수, 최소공배수 찾기
# 1. 최대공약수: 두 수의 약수를 구하고 오름차순 정렬 후 나오는 마지막 숫자 
a = 24
aa = range(1,a)
a_factors = []
for i in aa:
    if a % i == 0:
        a_factors.append(i)
a_factors.append(a)

b = 36
bb = range(1,b)
b_factors = []
for i in bb:
    if b % i == 0:
        b_factors.append(i)
b_factors.append(b)

common = []
for i in a_factors:
    if i in b_factors:
        common.append(i)
common.sort()
result = common[-1]
print(result)

# 2. 두 수의 곱 / 최대공약수
a = 24
b = 36
M = a*b
GCD = common[-1]
LCM = M/GCD
print('%d 와 %d의 최소공배수는 %d이다.' %(a, b, LCM))






