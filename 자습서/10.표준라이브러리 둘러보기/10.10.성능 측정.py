# 일부 파이썬 사용자들은 같은 문제에 대한
# 다른 접근법들의 상대적인 성능을 파악하는데 깊은 관심을 두고 있습니다.
# 파이썬은 이런 질문들에 즉시 답을 주는 측정 도구를 제공합니다.
#
# 예를 들어, 인자들을 맞교환하는 전통적인 방식 대신에,
# 튜플 패킹과 언 패킹을 사용하고자 하는 유혹을 느낄 수 있습니다.
# timeit 모듈은 적당한 성능 이점을 신속하게 보여줍니다:

from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
# 0.57535828626024577
Timer('a,b = b,a', 'a=1; b=2').timeit()
# 0.54962537085770791