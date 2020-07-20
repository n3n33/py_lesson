# NumPy ( Numerical Python )는 거의 모든 과학 및 공학 분야에서 사용되는 오픈 소스 Python 라이브러리

# Numpy 를 가져오는 방법

import numpy as np

# 배열은 음이 아닌 정수의 튜플, 부울, 다른 배열 또는 정수로 색인을 생성 할 수 있습니다.
# rank 배열의 차원 수이다. 의 shape 배열은 각 차원을 따라 배열의 크기를 제공하는 정수의 튜플

# 배열에 대한 자세한 정보

# NumPy 에서 치수는 axis

# 기본 배열을 만드는 방법

a = np.array([1, 2, 3])

# array([1, 2, 3])

np.zeros(2)
# array([0., 0.])
# zeeros 의 기본값은 float 으로 설정되어 있어서
# 원소 값이 0. 으로 표기됨

np.ones(4)
# array([1., 1., 1., 1.])
# ones 의 경우 원소 값 float 으로 설정되어있어 1. 으로 표기됨

np.empty(3)
# array([4.34339178e-311, 4.08931890e-316, 2.41910791e-312])
# empty 는 초기내용이 무작위

np.arange(4)
# array([0, 1, 2, 3])

np.arange(2, 9, 2)
# array([2, 4, 6, 8])
# 2 ~ (9 - 1) 까지 씩 증가하는 배열 >> 2, 4, 6, 8

np.arange(2, 10, 2) == np.arange(2, 9, 2)
# array([ True,  True,  True,  True])


np.linspace(0, 10, num=5)
# array([ 0. ,  2.5,  5. ,  7.5, 10. ])
# 기본 원소 값은 float 으로 표현
# num = 5 는 기준 값으로
# 0~ 10 까지 원소 5개를 균일한 간격을 둔 값으로 구성함
# num 은 배열의 원소 갯수
# 원소갯수만 정하면 알아서 수열 생성됨

## 요소 추가, 제거 및 정렬
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)  # 오름차순으로 정렬됨
# 내림차순은?

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a, b))
# array([1, 2, 3, 4, 5, 6, 7, 8])

c = np.array([2, 3])
d = np.array([1, 0])
np.concatenate((c, d))
# array([2, 3, 1, 0])

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
np.concatenate((x, y), axis=0)
# axis int, optional
# The axis along which the arrays will be joined.
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
np.concatenate((x, y), axis=1)
# array([[1, 2, 5, 6],
#        [3, 4, 7, 8]])

# axis 는 열을 나타냄
# 0 일땐 a 행렬의 0번쨰 열에 b 행혈 join
e1 = np.array([[1, 2], [3, 4], [5, 9]])
e2 = np.array([[5, 6], [7, 8], [9, 3]])
np.concatenate((e1, e2), axis=0)
# array([[1, 2],
#        [3, 4],
#        [5, 9],
#        [5, 6],
#        [7, 8],
#        [9, 3]])
np.concatenate((e1, e2), axis=1)
# array([[1, 2, 5, 6],
#       [3, 4, 7, 8],
#       [5, 9, 9, 3]])


## 배열의 모양과 크기를 어떻게 알 수 있습니까?

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]]])

array_example.ndim  # 3 자원 수
array_example.size  # 24 요소 수
array_example.shape  # (3, 2, 4) 배열의 모양

## 배열을 재구성 할 수 있습니까?
# arr.reshape()
# 원소를 바꾸지않고 재배열 하여 새로운 배열 생성
l = np.arange(6)
print(l)
# [0 1 2 3 4 5]
r = l.reshape(3, 2)
print(r)
# [[0 1]
#  [2 3]
#  [4 5]]
# 3행 2열
# 출력할때 array가 출력될때랑 안될떄가 있는데 그차이?
a = np.arange(6)
np.reshape(a, newshape=(1, 6), order='C')
# newshape당신이 원하는 새로운 모양입니다.
# 정수 또는 튜플 정수를 지정할 수 있습니다.
# 정수를 지정하면 결과는 해당 길이의 배열이됩니다. 모양은 원래 모양과 호환되어야함
np.reshape(a, newshape=(2, 3), order='F')
# array([[0, 2, 4],
#        [1, 3, 5]])
# C , Fortran의 차이는 ?
# https://numpy.org/doc/stable/reference/internals.html#numpy-internals
# 참고하기


## 1D 배열을 2D 배열로 변환하는 방법 (배열에 새 축을 추가하는 방법)
a = np.array([1, 2, 3, 4, 5, 6])
a.shape
# (6,)
a2 = a[np.newaxis, :]  # 새 축 추가
a2.shape
# (1, 6)
col_vector = a[:, np.newaxis]
col_vector.shape
# (6, 1)
b = np.expand_dims(a, axis=1)  # 인덱스 위치에 새축 추가
# array([[1],
#        [2],
#        [3],
#        [4],
#        [5],
#        [6]])
# (6, 1)
c = np.expand_dims(a, axis=0)
# (1, 6)

## 인덱싱과 슬라이싱

data = np.array([1,2,3])
data
# array([1, 2, 3])
data[1]
# 2
data[0:2]
# array([1,2])

p = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(p[p<5])
# [1,2,3,4]
five_up = (p >= 5)
print(p[five_up])
# [ 5  6  7  8  9 10 11 12]
divisible_by_2 = p [p%2 == 0]
divisible_by_2
# array([ 2,  4,  6,  8, 10, 12])
five_up = (p > 5) | (p == 5)
print(five_up)
five_up
# [[False False False False]
#  [ True  True  True  True]
#  [ True  True  True True]]

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)
print(b)
# (array([0, 0, 0, 0], dtype=int64), array([0, 1, 2, 3], dtype=int64))

list_of_coordinates= list(zip(b[0], b[1]))

for coord in list_of_coordinates:
    print(coord)
# (0, 0)
# (0, 1)
# (0, 2)
# (0, 3)


