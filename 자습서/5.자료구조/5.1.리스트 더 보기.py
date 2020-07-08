# 5.1. 리스트 더 보기
list = [1, 2, 3, 4]
print(list)

list.append(9)
print(list)

# list.extend(__iterable=)

list.insert(2, 13)
print(list)

list.remove(1)  # 1과 같은 항목 삭제함. 1번째에 들어있는 값이 아닌
print(list)

list.pop(0)  # 0은 index값으로 0번째에 들어있는 항목 지움
print(list)

# print(list.index(3, 0, 1))

print(list.count(3))

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.sort()
print(fruits)  # ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']
fruits.reverse()
print(fruits)  # ['pear', 'orange', 'kiwi', 'banana', 'banana', 'apple', 'apple']


# clear(list) #리스트 항목 전체 삭제

# 5.1.1.리스트를 스택으로 사용하기
# 스택은 First in Last Out
# append, pop 사용

# 5.1.2.리스트를 큐로 사용하기
# first in first out
# deque 사용해 머리,꼬리에서 삽입 삭제 자유롭게
# collections.deque 사용

# 5.1.3.리스트 컴프리헨션
squares = []
for x in range(10):
    squares.append(x**2)  #  x의 제곱급 삽입

print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# squares1 = list(map(lambda x: x**2, range(10)))

squares2 = [x**2 for x in range(10)]
print(squares2)