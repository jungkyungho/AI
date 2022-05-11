# 1. NumPy 사용법

import numpy as np

# 1) 리스트에서 행렬/배열 생성

# 행렬생성
a = [[1,2,3], [4,5,6]]
b = np.array(a)

# 열수
print(b.ndim)

# 차원
print(b.shape)

# 원소접근
print(b[0,0])


# 2) 특수한 배열의 생성

# 1씩 증가하는 1차원 배열(5부터 시작)
print(np.arange(5,10))

# 영행렬
print(np.zeros((2,2)))

# 유닛행렬(1로 채워진행렬)
print(np.ones((2,3)))

# 단위행렬(3x3)
print(np.eye(3))

# 3) 배열의 차원 변환
a = np.arange(20)
b = a.reshape((4,5))

# 3) NumPy 슬라이싱/ 인덱싱
list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
array = np.array(list)
a = array[0:2, 0:2]
a = array[1:, 1:]

# 4) NumPy 사칙연산( +, -, *, / )
a = np.array([1,2,3])
b = np.array([4,5,6])

# 더하기
c = a + b
c = np.add(a,b)

# 곱하기
c = a * b
c = np.multiply(a, b)

# 나누기
c = a / b
c = np.divide(a, b)

# 행렬의 곱
array1 = [[1,2], [3,4]]
array2 = [[5,6], [7,8]]
a = np.array(array1)
b = np.array(array2)

c = np.dot(a, b)

# 모든원소 합/곱
a = np.array([[-1,2,3], [3,4,8]])
s = np.sum(a)
s = np.prod(a)

# 평균
array3 = [
    [10, 20, 30],
    [3, 50, 5],
    [100, 110, 120]
]
print(np.mean(array3))
print(np.mean(array3, axis=0))
print(np.mean(array3, axis=1))

# 표준편차
print(np.std(array3))
print(np.std(array3, axis=0))
print(np.std(array3, axis=1))



# 5) 백터의 연산
# 내적
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])


#print(x.T.dot(y))# x'y

print(x.dot(y)) # xy
print(y.dot(x)) # yx

# 역행렬
arr = np.array([
                [[1, 3],
                 [5, 7]],
                [[2, 5],
                 [4, 6]]])
arr_inv = np.linalg.inv(arr)
print(arr_inv)

# 6) random number 생성

# 균등분포에서
x = np.random.uniform(size=100) # 최소, 최대, 개수
x.reshape(20,5)

# 정규분포에서
s = np.random.normal(0, 1, 1000) # 평균, 표준편차, 개수


# 2. matplotlib 사용법
import matplotlib.pyplot as plt

# 1) sine 그리기
x = np.linspace(-2*np.pi, 2*np.pi, 100) # -2pi과 2pi사이를 100개의 점으로 나타냄
y = np.sin(x) 

plt.plot(x,y) # 기본 플롯
plt.plot(x, 0.5*y, color='blue', marker='o', linestyle=':',label='legend2 표시') # 다추가한 플롯

plt.title('Sine graph') # 제목, X와 Y축 제목
plt.xlabel(r'$x$')
plt.ylabel(r'$sin(4 \pi x)$')

plt.grid(True) # 그리드 표시
plt.legend(loc='upper left')

# subplot(여러개의 그래프를 행렬처럼 배치)
x = np.linspace(0,1,50)
y1 = np.cos(4*np.pi*x)
y2 = np.cos(4*np.pi*x)*np.exp(-2*x)

plt.subplot(2,1,1) # 2행 1열, idnum
plt.plot(x,y1,'r-*',lw=1)
plt.grid(True)
plt.ylabel(r'$sin(4 \pi x)$')


plt.subplot(2,1,2)
plt.plot(x,y2,'bo',lw=1)
plt.grid(True)
plt.xlabel('x')
plt.ylabel(r'$ e^{-2x} sin(4\pi x) $')


# 3. 파이썬과 수학
import numpy as np

# 중복원소 제거
a = [1,2,3]
b = [4,5,6]
c = [1,2,3,1,2]
d = [3,3,4,5,6,6,6,7,8,8,9]

new_c = []
for i in c:
    if i not in new_c:
        new_c.append(i)
print(new_c)             #새로운 값을 담을 객체를 만들고 for문을 돌려 c의 객체를 new_c에 듬으면서 if문으로 중복을 확인.(c에서 중복원소를 찾는 것!!)

# 합집합 구현
a = [1,2,3]
b = [4,5,6]
c = a + b

c = []
for i in a:
    if i not in b:
        c.append(i)
c = c + b
print(c)


A = ['apple', 'melon', 'oreange']
B = ['chicken', 'pig', 'cow']
C = []
for i in A:
    if i not in B:
        C.append(i)
C = B + C

# 교집합 구현
a = [1,2,3]
b = [2,3,4,5,6]
c = []
for i in a:
    if i in b:
        c.append(i)

# 차칩합 구현
a = [1,2,3]
b = [2,3,4,5,6]
c = []
for i in a:
    if i not in b:
        c.append(i)

a = [1,2,3]
b = [2,3,4,5,6]
c = a + []
for i in b:
    if i in a:
        c.remove(i)

#여집합 구하기
u = [1,2,3,4,5]
a = [1,2,3]
a_com = []
for i in u:
    if i not in a:
        a_com.append(i)

u = [1,2,3,4,5]
a = [1,2,3]
rest = u + []
for i in a:
    if i in a:
        a_com.append(i)

# 소수: 자기자신과 1로 밖에 나누어지지 않는 숫자.(1은 제외)
a = 17
a_prime = True
for i in range(2, a):
    if a % i ==0:
        a_prime = False
if a_prime == True:
    print('%d 는 소수이다.' %a)
else:
    print("%d는 소수가 아니다." %a)










