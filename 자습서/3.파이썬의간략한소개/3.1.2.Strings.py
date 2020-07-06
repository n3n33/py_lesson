# Python can also manipulate strings, which can be expressed in several ways.

print('spam eggs', type('spam eggs'))    # str

print('doesn\'t', type('doesn\'t'))    # use \' to escape the single quote...

print("doesn't", type("doesn't"))

print('"yes," they said')

print("\"Yes,\" they said.")

print('"Isn\'t," they said.')

print('"Isn\'t," they said.')

print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'
print(s)

a = 'First line.\'Second line.'
print(a)

print('c:\some\name')

print(r'C:\some\name')    # 특수문자 취급 안받으면 r 붙이기

# 여러줄로 작성하고 싶으면 """ ~~ """ 또는 ''' ~~ '''로 작성
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 문자열은 + 연산자로 이어붙이고, * 연산자로 반복시킬 수 있다

print(3 * 'Na' + 'Ya')

print('Py' 'thon')    # 문자열이 연속해서 나타나면 자동으로 이어붙임

text = ('Put several strings within parentheses'
        ' to have htem joined together')
print(text)

prefix = 'Py'

print(prefix + 'thon')

word = 'Python'

print(word[0], 'word type',type(word),'word[0] type', type(word[0]))

print(word[-6])

# print(word[-7])

print(word[5])

print(word[0:2])

print(word[:2] + word[2:])    # Python

print(word[4:50])

print(len(word))