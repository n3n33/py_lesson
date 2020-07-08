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


x = MyClass()  # 인스턴스


def __init__(self):    #self는 자바의 this
    self.data = []
