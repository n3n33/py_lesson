# datetime 모듈은 날짜와 시간을 조작하는 클래스들을 제공하는데,
# 간단한 방법과 복잡한 방법 모두 제공

from datetime import date
now = date.today()
# datetime.date(2020, 7, 14)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# '07-14-20. 14 Jul 2020 is a Tuesday on the 14 day of July.'

birthday = date(1995, 3, 31)
age = now - birthday
age.days
# 9237
