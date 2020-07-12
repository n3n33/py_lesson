class Puppy:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def delete(self, x):
        self.data.delete(x)

class Dog(Puppy):
