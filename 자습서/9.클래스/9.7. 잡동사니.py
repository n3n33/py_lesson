# 때로 몇몇 이름 붙은 데이터 항목들을 함께 묶어주는
# 파스칼의 《record》 나 C의 《struct》 와 유사한 데이터형을 갖는 것이 쓸모 있습니다.
# 빈 클래스 정의가 훌륭히 할 수 있는 일입니다

class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000