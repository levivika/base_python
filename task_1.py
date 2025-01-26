name = input('Name: ')
lastname= input('lastname: ')
fathername = input('fathername: ')
date = input('date: ')
city = input('city: ')

data = {'name': name,'lastname': lastname,'fathername': fathername,'city': city,'date': date}
print(data)

for key in data:
    print(f'{key}:{data[key]}')