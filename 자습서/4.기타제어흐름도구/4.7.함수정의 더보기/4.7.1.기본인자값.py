# 정해지지 않은 개수의 인자들로 함수를 정의하는 것도 가능
# 세 가지 방식이 있음

# 4.7.1. 기본 인자 값
# 정의 된 것 보다 더 적은 개수의 인자들로 호출될 수 있는 함수 만들기

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


ask_ok('정말 끝나길 원하세요?', 2)

# 함수에 정의된 ok값이 없을 경우 reminder 출력됨
# retires 는 반복 횟수.
# retries 가 4일 경우, 0,1,2,3,4 총 5번 반복
# retries 가 2일경우 0,1,2 총 3번 반복
# if retries < 0 의 문장 떄문에 0까지 포함하여 반복


# ask_ok('y,n만 입력해주세요')
# retries int 값 새로 정의?안하면 기본값 4로

i = 5  # i의 값은 5


def f(arg=i):  # 험수 f의 인수는 arg. arg = i와 같으므로 arg의 값은 5
    print(arg)  # 함수 f를 실행할 시 i 값 출력함


i = 6  # 함수 밖에서 i값 다시 6으로 대입
f()  # 기본 값은 함수가 정의되고 있는 스코프에서 구해짐 f() = 5
print(i)  # 6
f(i)  # f(i) = 6 출력


# 기본값은 오직 한 번만 값이 구해집니다.
# 이것은 기본값이 리스트나 딕셔너리나 대부분 클래스의 인스턴스와 같은 가변 객체일 때 차이를 만듭니다.
# 예를 들어, 다음 함수는 계속되는 호출로 전달된 인자들을 누적합니다

def f1(a, L=[]):
    L.append(a)
    return L


print(f1(1))  # [1]
print(f1(2))  # [1, 2]


# 기본값 공유되지않음
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f2(1))  # [1]
print(f2(2))  # [2]