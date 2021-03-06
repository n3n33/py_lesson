# 4.7.6. 람다 표현식
# lambda 키워드들 사용해서 작고 이름 없는 함수를 만들 수 있습니다.
# 이 함수는 두 인자의 합을 돌려줍니다: lambda a, b: a+b.
# 함수 객체가 있어야 하는 곳이면 어디나 람다 함수가 사용될 수 있습니다.
# 문법적으로는 하나의 표현식으로 제한됩니다.
# 의미적으로는, 일반적인 함수 정의의 편의 문법일 뿐입니다.
# 중첩된 함수 정의처럼, 람다 함수는 둘러싸는 스코프에 있는 변수들을 참조할 수 있습니다:

def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)  # f 의 x 정의
print(f(0))  # x : x + n n = 0
print(f(1))  # x : x + n n = 1 42 + 1
print(f(2))  # x : x + n n = 2 42 + 2
