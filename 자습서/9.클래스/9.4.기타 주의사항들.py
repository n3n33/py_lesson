# 인스턴스와 클래스 모두에서 같은 어트리뷰트 이름이 등장하면,
# 어트리뷰트 조회는 인스턴스를 우선합니다

class Warehouse:
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()
print(w1.purpose, w1.region)  # storage west
w2 = Warehouse()
w2.region = 'north'
print(w2.purpose, w2.region)
w3 = Warehouse()
w3.purpose = 'keep'
print(w3.purpose, w3.region)


def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


bag = Bag()  # 인스턴스화
bag.add('backpack')  # Bag 클래스의 add 정의함수로 backpack 삽입
print(bag.data)  # self.data로 리스트 출력



