'''
Напишите программу, которая принимает две 
строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions
'''
import fractions
string_1 = input("Введите дробь вида a/b: ")
string_2 = input("Введите дробь вида a/b: ")


f1 = fractions.Fraction(string_1)
f2 = fractions.Fraction(string_2)
sum = f1 + f2
multipl = f1 * f2
print (f' сумма дробей = {sum}, произведение дробей = {multipl}')

"""
def Count_fractions(string_1, string_2):
    f1 = fractions.Fraction(string_1)
    f2 = fractions.Fraction(string_2)
    sum = f1 + f2
    multipl = f1 * f2
    return sum, multipl

result = Count_fractions(string_1, string_2)
print (result)

Не понимаю, почему эта функция не работает
"""

