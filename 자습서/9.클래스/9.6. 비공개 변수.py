# 객체 내부에서만 액세스할 수 있는 《비공개》 인스턴스 변수는 파이썬에 존재하지 않습니다.
# 하지만, 대부분의 파이썬 코드에서 따르고 있는 규약이 있습니다:
# 밑줄로 시작하는 이름은 (예를 들어, _spam) API의 공개적이지 않은 부분으로 취급되어야 합니다
# (그것이 함수, 메서드, 데이터 멤버중 무엇이건 간에). 구현 상세이고 통보 없이 변경되는 대상으로 취급되어야 합니다.
#
# 클래스-비공개 멤버들의 올바른 사례가 있으므로 (즉 서브 클래스에서 정의된 이름들과의 충돌을 피하고자),
# 이름 뒤섞기 (name mangling) 라고 불리는 메커니즘에 대한 제한된 지원이 있습니다.
# __spam 형태의 (최소 두 개의 밑줄로 시작하고, 최대 한 개의 밑줄로 끝납니다)
# 모든 식별자는 _classname__spam 로 텍스트 적으로 치환되는데,
# classname 은 현재 클래스 이름에서 앞에 오는 밑줄을 제거한 것입니다.
# 이 뒤섞기는 클래스 정의에 등장하는 이상, 식별자의 문법적 위치와 무관하게 수행됩니다.
#
# 이름 뒤섞기는 클래스 내부의 메서드 호출을 방해하지 않고
# 서브 클래스들이 메서드를 재정의할 수 있도록 하는 데 도움을 줍니다

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
