# if 문

# x = int(input('Please  enter an  Integer: '))
# if x < 0 :
#     x = 0
#     print('Negative change to Zero')
# elif x == 0 :
#     print('Zero')
# elif x == 1 :
#     print('Single')
# else :
#     print('More')



x = input('생년월일8자리를 입력해주세요')
if len(x) == 8:
    print('태어난 년도는', x[:4], '생일은', x[4:], '입니다.')
else :
    print('8자리를 입력해주세요')