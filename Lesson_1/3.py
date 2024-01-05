'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
''' 
LOWER_LIMIT = 0
UPPER_LIMIT = 1000

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)
number = int(input('Введите число:'))
count = 0
TRY = 2


while count > TRY:
    print('Не угадали')
else:
    
    if number > num:
        count = count + 1
        print("Больше")
        number = int(input('Введите число:'))
    
    elif number < num:
        count = count + 1        
        print("Меньше")
        number = int(input('Введите число:'))
    
    else: 
         print("Верно")
         



   
    
        
        

