# 4.7.2. 키워드 인자
# 함수는 kwarg=value 형식의 키워드 인자를 사용해서 호출될 수 있다

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# 어떤 인자도 두 개 이상의 값을 받을 수 없다.
# 함수 호출에서, 키워드 인자는 위치 인자 뒤에 나와야 합니다. <<중요>>

parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# parrot(volatage 인자 값은 필수, 나머지 세개는 선택)


# **name 형식의 마지막 형식 매개변수가 존재하면, 형식 매개변수들에 대응하지 않는 모든 키워드 인자들을 담은 딕셔너리를 받습니다.
# 이것은 *name형식의 형식 매개변수와 조합될 수 있는데, 형식 매개변수 목록 밖의 위치 인자들을 담은 튜플을 받습니다.
# (*name은 **name 앞에 나와야 합니다.)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)  # *arguments 출력
    print("-" * 40)
    for kw in keywords:  # dictionary 형태
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# Limburger 는 kind
# It's very runny, sir 는 *arguments
# It's really very, VERY runny, sir.  *arguments
# 인쇄되는 키워드 인자들의 순서 함수 호출로 전달된 순서와 일치함이 보장됨에 주목