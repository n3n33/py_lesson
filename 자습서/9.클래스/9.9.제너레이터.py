# 제너레이터 는 이터레이터를 만드는 간단하고 강력한 도구입니다.
# 일반적인 함수처럼 작성되지만 값을 돌려주고 싶을 때마다 yield 문을 사용합니다.
# 제너레이터에 next() 가 호출될 때마다,
# 제너레이터는 떠난 곳에서 실행을 재개합니다 (모든 데이터 값들과 어떤 문장이 마지막으로 실행되었는지 기억합니다).
# 예는 제너레이터를 사소할 정도로 쉽게 만들 수 있음을 보여줍니다:
# 제너레이터로 할 수 있는 모든 것은 앞 절에서 설명했듯이 클래스 기반 이터레이터로도 할 수 있습니다.
# 제너레이터가 간단한 이유는 __iter__() 와 __next__() 메서드가 저절로 만들어지기 때문입니다.
#
# 또 하나의 주요 기능은 지역 변수들과 실행 상태가 호출 간에 자동으로 보관된다는 것입니다.
# 이것은 self.index 나 self.data 와 같은 인스턴스 변수를 사용하는 접근법에 비교해 함수를 쓰기 쉽고 명료하게 만듭니다.
#
# 자동 메서드 생성과 프로그램 상태의 저장에 더해,
# 제너레이터가 종료할 때 자동으로 StopIteration 을 일으킵니다.
# 조합하면, 이 기능들이 일반 함수를 작성하는 것만큼 이터레이터를 만들기 쉽게 만듭니다.

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
