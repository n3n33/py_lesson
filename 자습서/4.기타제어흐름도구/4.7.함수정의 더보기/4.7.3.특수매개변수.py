# 4.3.7.특수매개변수
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
# pos1, pos 2 >> positional only
# pos_or_kw >> positional or keyword
# kwd1, kwd2 >> keyword only

# 4.7.3.1. 위치-키워드(Positional-or-Keyword) 인자
# 함수 정의에 /와 *가 없으면, 인자를 위치나 키워드로 함수에 전달할 수 있습니다.

# 4.7.3.2. 위치 전용 매개 변수
# 좀 더 자세하게 살펴보면, 특정 매개 변수를 위치 전용으로 표시할 수 있습니다.
# 위치 전용이면, 매개 변수의 순서가 중요하며, 키워드로 매개 변수를 전달할 수 없습니다.
# 위치 전용 매개 변수는 / (슬래시) 앞에 놓입니다.
# /는 위치 전용 매개 변수를 나머지 매개 변수들로부터 논리적으로 분리하는 데 사용됩니다.
# 함수 정의에 /가 없으면, 위치 전용 매개 변수는 없습니다.

# / 다음의 매개 변수는 위치-키워드나 키워드 전용일 수 있습니다.

# 4.7.3.3. 키워드 전용 인자
# 매개 변수를 키워드 인자로 전달해야 함을 나타내도록, 매개 변수를 키워드 전용으로 표시하려면,
# 첫 번째 키워드 전용 매개 변수 바로 전에 인자 목록에 *를 넣으십시오.


def standard_arg(arg):
    print(arg)


# def position_only(arg, /):
#    print(arg)

# def pos_or_kw(/, args):
#    print(args)

def kw_only(*, arg):
    print(arg)


standard_arg(2)
standard_arg(arg=4)


# def foo(name, /,**kwds):
#    return 'name' in kwds

