# 딕셔너리로 루핑할 때, items() 메서드를 사용하면 키와 거기에 대응하는 값을 동시에 얻을 수 있습니다.
#

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
     print(k, v)

# 시퀀스를 루핑할 때, enumerate() 함수를 사용하면 위치 인덱스와 대응하는 값을 동시에 얻을 수 있습니다.


for i, v in enumerate(['tic', 'tac', 'toe']):
     print(i, v)


# 둘이나 그 이상의 시퀀스를 동시에 루핑하려면,
# zip() 함수로 엔트리들의 쌍을 만들 수 있습니다.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))

# 시퀀스를 거꾸로 루핑하려면,
# 먼저 정방향으로 시퀀스를 지정한 다음에 reversed() 함수를 호출하세요.

for i in reversed(range(1, 10, 2)):
    print(i)

# 정렬된 순서로 시퀀스를 루핑하려면,
    # sorted() 함수를 사용해서 소스를 변경하지 않고도 정렬된 새 리스트를 받을 수 있습니다

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
     print(f)

# 때로 루프를 돌고 있는 리스트를 변경하고픈 유혹을 느낍니다;
# 하지만, 종종, 대신 새 리스트를 만드는 것이 더 간단하고 더 안전합니다.