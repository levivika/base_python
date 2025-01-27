
age = int(input('Your age: '))
name = input('Your name: ')
if age >= 18:
    print(f'Hello, {name}, welcome!')
    print(f'You are {age}')

elif age < 18 and age >= 0:
    print(f'Your age {age}, access denied!')

