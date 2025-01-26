names = []
names.append('alex')
names.append('Lora')
names.append('Lora')
names.append('Lora')

print(names)

ind = names.index('Lora',3,4)
print(ind)

names.insert(2, 2)
names.remove('Lora')


print(names)
print(len(names))

print(names[-1])
print(names)
#добавление списка
names.extend(['Vlonz', 2, 'Alex'])
print(names)


print(names[::-1])

for i in names:
    print(i)



for i in range(len(names)):
    print(f'{i+1}. {names[i]}')

a=10
while a>0:
    print('hello')
    a -= 4
    if a <= 4:
        break

'''
while True:
    print('jjjj')
    print('jjj')
    print('jjjj')
    print('jjjj')
    action = input('>>> ')
    if action == '1':
        print('yes')
    if action == '0':
        break
'''

print(names)
names += ['nastya']
print(names)

for i in range(9):
    print(i+1)



action = (
    ('kkkk', 'jjjj'),
    ('kkkk', ';;;')
)
print(action)
print(len("jjj"))




a = {'k': 3, 'hh': 'jj', 'ss': 'll'}

print(a['k'])
a['info'] = 'hhhh'
print(a)

print(len(a))

b = a.pop('hh')

print(a)

print(a.get('ss'))

a = b
print(id(b))

a =
