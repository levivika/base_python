'''
Задание
1. Написать программу, которая выводит на экран список четных чисел от 10 до 30.

2. Написать программу, которая принимает от пользователя ввод трех имен и добавляет их в список names
Выведите список на экран
Выведите количество элементов списка
Выведите отдельно первый элемент списка
Выведите отдельно последний элемент списка

3. в получившийся во 2 задании список names добавьте имя Igor во 2 позицию
выведите на экран индекс этого элемента
удалите имя Igor из списка
'''


for i in range (10, 31):
    if i%2==0:
        print(i)


names = []
'''
a = input('First name: ')
b = input('Second name: ')
c = input('Third name: ')
'''
z=0
for i in range (0, 3):
    name = input('Name: ')
    names.append(name)


print(names)
print(len(names))
print(names[0])
print(names[-1])



names.insert(2, "Alex")
print(names)
ind = names.index("Alex")
print(ind)

if 'igor' in names:
    names.remove('igor')
print(names)