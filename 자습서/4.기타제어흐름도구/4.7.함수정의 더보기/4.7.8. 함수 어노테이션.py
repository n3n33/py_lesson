# 4.7.8. 함수 어노테이션
# 함수 어노테이션 은 사용자 정의 함수가 사용하는 형들에 대한 완전히 선택적인 메타데이터 정보입니다
# (자세한 내용은 PEP 3107 과 PEP 484 를 보세요).
#
# 어노테이션은 함수의 __annotations__ 어트리뷰트에 딕셔너리로 저장되고
# 함수의 다른 부분에는 아무런 영향을 미치지 않습니다.
# 매개변수 어노테이션은 매개변수 이름 뒤에 오는 콜론으로 정의되는데,
# 값을 구할 때 어노테이션의 값을 주는 표현식이 뒤따릅니다.
# 반환 값 어노테이션은 리터럴 -> 와 그 뒤를 따르는 표현식으로 정의되는데,
# 매개변수 목록과 def 문의 끝을 나타내는 콜론 사이에 놓입니다.
# 다음 예에서 위치 인자, 키워드 인자, 반환 값이 어노테이트 됩니다:

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + 'and' + eggs


f('spam')
# ham + 'and' + eggs가 출력안됨
