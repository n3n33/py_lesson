# 8.1. 문법 에러

# 문법에러 == 파싱에러

# while True print('Hello World!')
# SyntaxError: invalid syntax
    # 콜론 붙이면 해결

# 8.2. 예외

# 실행 중에 감지되는 에러들을 "예외"라고 부름
# 치명적이지는 않음
# 예외는 프로그램이 처리하지않음

# print(10*(1/0))
# ZeroDivisionError: division by zero

# 8.3. 예외 처리하기

while True:
    try:
        x = int(input('Plaese Enter A  Number: '))
        break
    except ValueError:
        print('Oops!  That was no valid number.  Try again...')

# 8.4. 예외 일으키기
# raise 문은 프로그래머가 지정한 예외가 발생하도록 강제할 수 있게함
# raise NameError('HiThere')
#     raise NameError('HiThere')
# NameError: HiThere

# 8.5. 사용자 정의 예외
# 새 예외 클래스를 만듦으로써 프로그램은 자신의 예외에 이름을 붙일 수 있습니다
# (파이썬 클래스에 대한 자세한 내용은 클래스 를 보세요).
# 예외는 보통 직접적으로나 간접적으로 Exception 클래스를 계승합니다.

    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


# 8.6. 뒷정리 동작 정의하기
# finally 절이 있으면, try 문이 완료되기 전에 finally 절이 마지막 작업으로 실행됩니다.
# finally 절은 try 문이 예외를 생성하는지와 관계없이 실행됩니다.
# 다음은 예외가 발생할 때 더 복잡한 경우를 설명합니다:

def bool_return():
     try:
         return True
     finally:
         return False


bool_return()

# 8.7. 미리 정의된 뒷정리 동작들
# 어떤 객체들은 객체가 더 필요 없을 때 개입하는 표준 뒷정리 동작을 정의합니다.
for line in open("myfile.txt"):
    print(line, end="")

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
