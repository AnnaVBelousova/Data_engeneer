
"""
Дан список повторяющихся элементов. 
Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
"""
my_list = [2, 78, 9, 'a', 'a', 'b', 2, 9]
list_dublicates = []


for item in my_list:
    count = my_list.count(item)
    print(count)
    if count > 1:
        list_dublicates.append(item)
        
print(list(set(list_dublicates)))
