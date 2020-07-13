# 대부분의 컨테이너 객체들을 for 문으로 루핑할 수 있음

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')



class Reverse:
        """Iterator for looping over a sequence backwards."""

        def __init__(self, data):
            self.data = data
            self.index = len(data)

        def __iter__(self):
            return self

        def __next__(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1
            return self.data[self.index]