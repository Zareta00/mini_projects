text = 'КупИ молоко'
print(text)
print('')

print(text.upper()) # верхний регистр
print('')

print(text.lower()) # нижний регистр
print('')
print(text.capitalize()) # исправляет написание и первую буку переводит в верхний регистр
print('')

print(text.split(' ')) # превращает строку в список
print('')

print('. '.join(text)) # превращает из списка в строку
print('')

text1 = '  Купи молоко!   '
print(text1.strip()) # удаляет проблы в начале и в конце
print('')

print(text1.lstrip()) # удаляет пробелы только в начале
print('')

print(text1.rstrip()) # удаляет пробелы в конце строки
print('')

print(text1.replace('молоко', 'хлеб')) # заменяет элементы, первое то что мы заменяем второе на что мы заменяем