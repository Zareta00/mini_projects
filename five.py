nameher = str(input('Как тебя зовут? '))
name = 'Привет, ' + nameher.capitalize() + '.'
print(name)


def oneage(): # создание функции
    age = int(input('Сколько тебе лет? '))
    if (age >= 23):
        print('Я твоя лягушка-квакушка.')
    elif (age >= 18) and (age <= 22):
        print('Тебе сюда еще рано.')
    else:
        print('Тебе сюда еще рано!')


oneage()