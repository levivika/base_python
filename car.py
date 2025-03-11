import re

def is_car_number(num):
    exm = r'^[А-Я]\d{3}[А-Я]{2}\d{3}$'
    match = re.match(exm, num.upper())
    return bool(match)

print(is_car_number('A233AAA555'))