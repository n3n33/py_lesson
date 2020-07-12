# 9.3.1. 클래스 정의 문법
# 정의 또는 선언
# 함수선언과 클래스 선언
# 선언은 재사용하기 위해서

# class 클래스이름
# ~~~~~~~~

# 타입__클래스__

# 9.3.2. 클래스 객체

# 어트리뷰트와 메서드
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


# 9.3.3. 인스턴스 객체

x = MyClass()  # 인스턴스화


def __init__(self):  # self는 자바의 this
    self.data = []


x = MyClass()

# 9.3.4. 메세드 객체

x.f()
xf = x.f
# while True:
#    print(xf())  # 끊임없이 출력


# 9.3.5. 클래스와 인스턴스 변수

class Dog:

    kind = 'canine'     # kind 객체, 모든 인스턴스에 공유가능

    def __init__(self, name):
        self.name = name  # 각각의 인스턴스


d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
