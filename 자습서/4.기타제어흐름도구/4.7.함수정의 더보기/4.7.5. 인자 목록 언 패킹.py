# 4.7.5. 인자 목록 언 패킹
# 인자들이 이미 리스트나 튜플에 있지만, 분리된 위치 인자들을 요구하는 함수 호출을 위해 언 패킹 해야 하는 경우 반대 상황이 벌어집니다.
# 예를 들어, 내장 range() 함수는 별도의 start와 stop 인자를 기대합니다.
# 그것들이 따로 있지 않으면, 리스트와 튜플로부터 인자를 언 패킹하기 위해 *-연산자를 사용해서 함수를 호출하면 됩니다:

list(range(1, 9))
# Out[2]: [1, 2, 3, 4, 5, 6, 7, 8]
args = [1, 9]
list(range(*args))