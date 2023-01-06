people = {'Даша': 23, 'Зарета': 22, 'Аня': 21, 'Алина': 26} # кортеж с левой стороны ключ, с правой стороны значени
print(people)
print('')

print(people['Даша']) # выдает значение ключа
print('')

people['Даша'] = 24 # изменяет значение ключа
print(people)
print('')

for k in people.keys(): # выводит только ключи
  print(k)
print('')

for m in people.values(): # выыодит только значение
  print(m)
print('')

for i in people.items(): # выводит все содержимое в качестве списка
  print(i)
print('')

del(people['Даша']) # удаляет элемент кортежа
print(people) 