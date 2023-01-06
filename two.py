name = ['Салли', 'Элли', 'Мегги', 2, 24]  # один из видов списка
print(name)
print('') # отступ

for names in name:
    print(
        names
    )  # цикл For дает возможность выводит все элементы списка по отдельности.
print('') 

name.append(26)  # добавление числового типа данных
print(name)  # Выводит сам список
print('')

name.append('Эшли')  # добавление строкового типа данных
print(name)
n = name.index(2) # Выводит индекс элемента. 
print(n)
print('')

print(name[4])  # вывод элемент списка через индекс.
print('')

name.pop() # удаляет последний элемент списка pop() удаляет по индексу
print(name)
print('')

name.remove('Элли') # Метод remove удаляет заданное значения в списке.
print(name)
print('')

print(len(name)) # показывает кол-во элементов в списке
print('')


number = [3,166,1,679,23,15,37,93,1]
print(number)
print('')

number.sort() # метод sort() сортирует по возврастанию только один тип данных.
print(number)
print('')

number.sort(reverse=True) # сортирует в обратном порядке
print(number)
print('')

number[5] = 'Bill' # замена элемента списка через индекс
print(number)
print('')

print(number.count(1)) # считает количество раз, когда значение появляется в списке
print('')

number.extend([4,5]) # Метод extend расширяет список, добавляя элементы. Преимущество над append в том, что вы можете добавлять списки.
print(number)
print('')

print([1,2] + [3,4]) # альтератива соединению списков


# Метод insert вставляет элемент перед указанным индексом.  .insert(индекс, список)