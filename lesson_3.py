# тип данных множество - set() - {}
'''
set_num = {1,2,23,0}
print(type(set_num))
print(set_num)

b = ['x','x','e']
b=set(b)
b.add('v')
b.remove('x')
print(set(b))

'''


a={'dina','va', 'vova', 'arina'}
b={'dina', 'va', 'na'}

c = a | b
print(c)

v = a.intersection(b)
print(v)

l = a & b
print(l)



d =a.difference(b) #что есть в А но нет в Б
print(d)

o = a.symmetric_difference(b) #все кроме совпадения
print(o)

















#строки стринг


a='xxxxxxd'
print(a[:3])




if a.find('1') != -1:
    print(a.find('d'))
else:
    print('error')
print('jjjjjbbxb'.count('b'))
print('jjjjjbbxb'.index('x'))

print('ss'.upper())
print('ss'.title())
print('ss'.lower())



print('Ss'[0].upper())
t = 'werr'
print(t[0].title() + t[1:].lower())


tyb= ['ff',
      'jf',
      'ft']
for ty in tyb:
    if ty.endswith('f'):
        print(ty + ' xaends with f')

u='8'
print(u.isalpha())
print(u.isdigit())

r = ('999x@1xfx9xfx199999@')
print(r.strip('x9'))

oo = []
for r in r.split('1'):
    oo.append(r.strip('@'))
print(oo)


q = ['E', 'R', 'O' ,'G']
print('  '.join(q))
a='  '.join(q)
print(a.split())


myfile = open('myfile.txt')