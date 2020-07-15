# 11.1 출력 포매팅
# reprlib 모듈은 크거나 깊게 중첩된 컨테이너의 축약 된 디스플레이를 위해
# pprint 모듈은 인터프리터가 읽을 수 있는 방식으로
# 내장 객체나 사용자 정의 객체를 인쇄하는 것을 보다 정교하게 제어할 수 있게 합니다
import reprlib

reprlib.repr(set('supercalifragilisticexpialidocious'))

# "{'a', 'c', 'd', 'e', 'f', 'g', ...}"

# pprint 모듈은 인터프리터가 읽을 수 있는 방식으로 내장 객체나 사용자 정의 객체를 인쇄하는 것을 보다 정교하게 제어할 수 있게 합니다
import pprint

t = [[['black, syan'], 'white', ['green', 'red'], ['magenta', 'yellow'], 'blue']]
pprint.pprint(t, width=30)
# [[['black, syan'],
#   'white',
#   ['green', 'red'],
#   ['magenta', 'yellow'],
#   'blue']]

# textwrap 모듈은 텍스트의 문단을 주어진 화면 너비에 맞게 포맷합니다:
import textwrap

doc = """The wrap() method is just like fill() except that it returns
 a list of strings instead of one big string with newlines to separate
 the wrapped lines."""

# The wrap() method is just like fill() except that it returns  a list
# of strings instead of one big string with newlines to separate  the
# wrapped lines.

print(textwrap.fill(doc, width=70))

# locale 모듈은 문화권 특정 데이터 포맷의 데이터베이스에 액세스

# 11.2.템플릿
# string 모듈은 다재다능한 Template 클래스를 포함하고 있는데,
# 최종 사용자가 편집하기에 적절한 단순한 문법을 갖고 있습니다.
# 따라서 사용자는 응용 프로그램을 변경하지 않고도 응용 프로그램을 커스터마이즈할 수 있습니다.
#
# 형식은 $ 와 유효한 파이썬 식별자 (영숫자와 밑줄)로 만들어진 자리표시자 이름을 사용합니다

# 11.3.바이너리 데이터 레코드 배치작업
# struct 모듈은 가변 길이 바이너리 레코드 형식으로 작업하기 위한 pack() 과 unpack() 함수를 제공
# 팩 코드 "H" 와 "I" 는 각각 2바이트와 4바이트의 부호 없는 숫자를 나타냅니다.
# "<" 는 표준 크기이면서 리틀 엔디안 바이트 순서를 가짐을 나타냅니다

# 11.4.다중 스레딩
# 스레딩은 차례로 종속되지 않는 작업을 분리하는 기술
# 스레드는 다른 작업이 백그라운드에서 실행되는 동안 사용자 입력을 받는 응용 프로그램의 응답을 향상하는 데 사용할 수 있습니다

# 11.5.로깅
# logging 모듈은 완전한 기능을 갖춘 유연한 로깅 시스템을 제공합니다.
# 가장 단순한 경우, 로그 메시지는 파일이나 sys.stderr 로 보내집니다:

# 11.6.약한 참조
# 파이썬은 자동 메모리 관리를 수행합니다.
# 사용되는 동안에만 객체를 추적해야 할 필요가 있습니다
# weakref 모듈은 참조를 만들지 않고 객체를 추적할 수 있는 도구를 제공
import weakref, gc


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])  # 10

del a

gc.collect()
print(d['primary'])  # Traceback (most recent call last):


# 11.7.리스트 작업 도구
# from array import array
# collections 에서 deque사용


# 11.8.10진 부동 소수점 산술
# decimal 모듈은 10진 부동 소수점 산술을 위한 Decimal 데이터형을 제공
# 정확한 10진수 표현이 필요한 금융 응용 및 기타 용도,
#
# 정밀도 제어,
#
# 법적 또는 규제 요구 사항을 충족하는 반올림 제어,
#
# 유효숫자 추적, 또는
#
# 사용자가 결과가 손으로 계산한 것과 일치 할 것으로 기대하는 응용.
