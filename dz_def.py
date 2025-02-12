'''
1. Написать функцию, которая возвращает факториал числа 
2. Написать функцию, которая принимает строку и возвращает количество символов в ней
3. Написать функцию, которая принимает имя, фамилию, возраст
   и возвращает словарь с этими данными
4. Написать функцию, которая принимает 3 числа и возвращает словарь,
   в котором содержится информация о сумме этих чисел, максимальном числе, минимальном числе
'''

def factorial_num (num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

print(factorial_num(5))

def count_of_letters(your_string):
    return len(your_string)
print(count_of_letters('dddddddd33'))

def inf_of_person(name, lastname, age):
    info = {
        'name': name,
        'surname': lastname,
        'age': age
    }
    return info
print(inf_of_person('masha', 'ivanova', 56))

def inf_about_num(num1, num2, num3):
    summ = num1+num2+num3
    a = [num1, num2, num3]
    max_num = num1
    for i in a:
        if max_num<i:
            max_num=i

    min_num = num1
    for i in a:
        if min_num>i:
            min_num=i

    info = {
        'min_num': min_num,
        'max_num': max_num,
        'summ': summ,

    }
    return info



print(inf_about_num(10,2,3))