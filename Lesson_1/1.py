#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. 
#Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
#то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input("введите число"))
b = int(input("введите число"))
c = int(input("введите число"))

if a + b > c and b + c > a and a + c > b:
    if a == b  and a !=c or b == c and b!= a or a == c and a != b:
        print("Треугольник равнобедренный")
    elif a == b and b == c:
        print("Треугольник равносторонний")
    else: 
        print("Треугольник разносторонний")
else: 
    print("Треугольник не существует")
