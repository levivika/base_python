list_1 = [1,30,30,25,24,30,1,27,25,40]
print(set(list_1))

list_2 =[]
for i in list_1:
    if i>=24:
        list_2.append(i)

print(list_2)

dict={}
count = 1
for i in list_1:
    if i>=24:
        dict.update({count:i})
        count+=1
print(dict)