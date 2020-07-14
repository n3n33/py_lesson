# math 모듈은 부동 소수점 연산을 위한 하부 C 라이브러리 함수들에 대한 액세스를 제공합니다.
import math

math.cos(math.pi / 4)
math.log(1024, 2)

import random

random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)
random.random()  # random float

import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

statistics.mean(data)
statistics.median(data)
statistics.variance(data)
