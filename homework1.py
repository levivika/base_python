'''
Задание
Написать программу, которая запрашивает у пользователя номер месяца и выводит название этого месяца
Если введено число 0 или число, большее 12, то написать, что номер месяца должен быть от 1 до 12
'''


month = int(input("Введите число месяца: "))

if month == 1:
    print('January')
elif month == 2:
    print('February')
elif month == 3:
    print('March')
elif month == 4:
    print('April')
elif month == 5:
    print('May')
elif month == 6:
    print('June')
elif month == 7:
    print('July')
elif month == 8:
    print('August')
elif month == 9:
    print('September')
elif month == 10:
    print('October')
elif month == 11:
    print('November')
elif month == 12:
    print('December')
elif (month <= 0 or month>12):
    print('Not a month')
else:
    print('Error')


'''
Написать программу, которая запрашивает у пользователя его имя, фамилию, возраст
Вывести полученные данные на экран
Если возраст, меньше 18, дополнительно вывести сообщение об этом
'''


name = input('Your name: ')
surname = input('Your surname: ')
age = int(input('Your age: '))
message = 'You are under 18'

if (age < 18 and age >= 0):
    age = "under 18"
elif (age < 0 or age > 130):
    age = 'not age'
else:
    age = age


print(f"your name - {name}, your surname - {surname}, your age - {age}")