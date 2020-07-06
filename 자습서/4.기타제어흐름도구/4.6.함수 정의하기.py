# 함수 만들기
# 피보나치 함수 만들기

# def fib(n):
#    a, b = 0, 1

# 값
def add(a,b):
    return a+b

def one_count(*iterable):
    one_count = 0
    for i in iterable:
        if i==1:
            one_count += 1
    return one_count

#7/6 기본 인자 값까지 진행함
