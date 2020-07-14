# re모듈은 고급 문자열 처리를 위한 정규식 도구들을 제공합니다.
import re

re.findall(r'\b[a-z]*]', 'which foot or hand fell fastest')
# Out[10]: ['foot', 'fell', 'fastest']
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
# Out[9]: 'cat in the hat'