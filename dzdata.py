'''
1. Написать функцию, которая возвращает, сколько дней осталось до нового года
2. Написать функцию, которая принимает дату рождения и возвращает количество полных лет
3. Написать функцию check_date(), которая принимает дату в формате строки "дд.мм.гггг"
и возвращает количество дней, которые прошли с этой даты или сколько дней осталось)

4.
4.1 Написать функцию, которая принимает информацию о книге из консоли (автор, название, год, жанр)
4.2 Написать функцию, которая сохраняет в словарь информацию о книге с валидацией года
    (1500 < год < текущий)
4.3 Сохранить в новый словарь информацию о 5 книгах
    {
	"1": {
		"author": "Pushkin",
		"title": "Ruslan & Ludmila",
		....
	},
	"2": ...

    }
4.5 Записать информацию о 5 книгах в books.json
4.6 Считать инф-ю из books.json в консоли
'''

from datetime import datetime
from dateutil.relativedelta import relativedelta
from time import strptime
import json


def new_year_coming():
    tod=datetime.today()
    new_year_date = '01.01.2026'
    new_year_date = datetime.strptime(new_year_date, '%d.%m.%Y')
    diff = new_year_date - tod
    return 'до нового года осталось -', diff.days

print(new_year_coming())

def your_age(date_of_birth):
    date_of_birth = datetime.strptime(date_of_birth, '%d.%m.%Y')
    tod = datetime.today()
    diff = relativedelta(tod, date_of_birth)
    return f'вам полных {diff.years} лет'

print(your_age('20.12.2007'))


def check_date(your_date):
    try:
        your_date = datetime.strptime(your_date, '%d.%m.%Y')
        your_date = your_date.date()
        tod = datetime.today().date()
        diff = tod - your_date
        if tod > your_date:
            return f'эта дата была {diff.days} дней'
        elif tod < your_date:
            return f'эта дата будет через {-diff.days} дней'
        elif tod == your_date:
            return f'эта дата сегодня'
    except ValueError as error:
        error = 'неверный формат даты'
        return error

print(check_date('02.022025'))


'''
4.
4.1 Написать функцию, которая принимает информацию о книге из консоли (автор, название, год, жанр)
4.2 Написать функцию, которая сохраняет в словарь информацию о книге с валидацией года
    (1500 < год < текущий)
4.3 Сохранить в новый словарь информацию о 5 книгах
    {
	"1": {
		"author": "Pushkin",
		"title": "Ruslan & Ludmila",
		....
	},
	"2": ...

    }
4.5 Записать информацию о 5 книгах в books.json
4.6 Считать инф-ю из books.json в консоли
'''

def validate_year(year):
    try:
        year = datetime.strptime(year, '%Y').date()
        year_1500 = datetime.strptime( '01.01.1500', '%d.%m.%Y').date()
        tod = datetime.today().date()
        if year_1500 <= year <= tod:
            return year.year
    except ValueError:
        return f'неверно введен год'

print(validate_year('2024'))


'''
        info = {
            'автор': author,
            'название': name,
            'год': year,
            'жанр' jenre:
        }
'''
def get_info():
    info={}
    books=[]
    for i in range(1,6):
        author = input(f'Автор {i}: ')
        name = input(f'Название {i}: ')
        year = input(f'Год {i}: ')
        year = validate_year(year)
        jenre = input(f'Жанр {i}: ')
        info[i] = {
            'автор': author,
            'название': name,
            'год': year,
            'жанр': jenre
        }

        books.append(info)

    return books

info = get_info()


def save_info_to_json(info):
    with open('books.json', 'w', encoding='utf-8') as file:
        json.dump(info, file, indent=2, ensure_ascii=False)
    print('Данные занесены в json')

def read_info_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        file_info = json.load(file)
    return file_info


save_info_to_json(info)
print(read_info_from_json('books.json'))