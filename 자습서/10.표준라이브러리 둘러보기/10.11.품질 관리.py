# 고품질의 소프트웨어를 개발하는 한 가지 접근법은 개발되는 각 함수에 대한 테스트를 작성하고,
# 그것들을 개발 프로세스 중에 자주 실행하는 것입니다.
#
# doctest 모듈은 모듈을 훑어보고 프로그램의 독스트링들에 내장된 테스트들을 검사하는 도구를 제공합니다.
# 테스트 만들기는 평범한 호출을 그 결과와 함께 독스트링으로 복사해서 붙여넣기를 하는 수준으로 간단해집니다.
# 사용자에게 예제를 함께 제공해서 설명서를 개선하고, doctest 모듈이 설명서에서 코드가 여전히 사실인지 확인하도록 합니다.

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


import doctest

doctest.testmod()

import unittest


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)


unittest.main()
