import math
print ('Список операций: +, -, *, /, **, log(первое число = число, второе = основание), ceil(окр. в большую сторону), '
       'floor(окр. в меньшую сторону)')
cul = input('Введите операцию из списка:  ')
x1 = float(input('Введите первое число:  '))
x2 = float(input('Введите второе число:  '))
if cul == '+':
    print (x1 + x2)
elif cul == '-':
    print (x1 - x2)
elif cul == '*':
    print (x1 * x2)
elif cul == '/':
    print (x1 / x2)
elif cul == '**':
    print (x1 ** x2)
elif cul == 'log':
    print (math.log(x1,x2))
elif cul == 'ceil':
    print (math.ceil(x1))
    print (math.ceil(x2))
elif func == 'floor':
    print (math.floor(x1))
    print (math.floor(x2))
else:
    print ('Ошибка, неправильная функция')