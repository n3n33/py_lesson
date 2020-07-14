# 일반적인 유틸리티 스크립트는 종종 명령행 인자를 처리해야 할 필요가 있음
import sys

print(sys.argv)
# ['C:/Users/F190028/Desktop/py_lesson/py_lesson/자습서/10.표준라이브러리 둘러보기/10.3.명령행 인자.py']

import argparse

parser = argparse.ArgumentParser(
    prog='top', description='show top lines form each file'
)
parser.add_argument('filename', nargs='+')
parser.add_argument('-|', '--lines', default=10)
args = parser.parse_args()
print(args)

# usage: top [-h] [-| LINES] filename [filename ...]
# top: error: the following arguments are required: filename