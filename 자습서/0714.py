# global 과 nonlocal 차이

a = 1


def d():
    a = 5

    def f():
        global a  # d()의 출력 값은 2 이다. global 사용해 사용자 정의 함수 밖에 있는 a의 값 가져옴
        a = a + 1
        return a

    return f()


print(d())


def e():
    a = 5

    def g():
        nonlocal a  # e()의 출력 값은 6 이다. nonlocal 사용해 사용자 정의 함수 안에 있는 a의 값 가져옴
        a = a + 1
        return a

    return g()


print(e())


#closure

def x(m):
    def y(n):
        return m+n
    return y


print(x(3)(4))  # 7
l = x(4)  # l 은 x함수 m에 4 대입한 값
print(l(5))  # 5는 y함수 n에 대입되어 l = 4 + n >> 4 + 5가 됨
