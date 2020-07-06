# break 문은, C처럼, 가장 가까이서 둘러싸는 for 나 while 루프로부터 빠져나가게 만듭니다.
# 루프 문은 else 절을 가질 수 있습니다

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
        elif n % 2 == 0:
            print("Found an even number", n)
            continue
        print("Found a number", n)
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
