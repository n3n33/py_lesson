
class Puppy:
    def __init__(self):
        self.data = []

    def addname(self, x):
        self.data.append(x)

    def delete(self, x):
        self.data.delete(x)


class Dog(Puppy):
    pass


dog = Dog()
dog.addname('tofu')
print(dog.data)

# 상속해서 부모 클래스?의 정의 함수 사용가능. 덮어쓰기도 가능할듯