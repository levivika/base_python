'''
results = set()
for n in range(100, 3001):
    bin_n = bin(n)[2:]
    bin_n_list = list(bin_n)
    if bin_n_list and bin_n_list[0] == '1':
        bin_n_list.pop(0)
        while bin_n_list and bin_n_list[0]=='0':
            bin_n_list.pop(0)
    if len(bin_n_list)==0:
            results.add(n)

    else:
            new_bin = ''.join(bin_n_list)
            new_n = int(new_bin, 2)
            results.add(n-new_n)
print(len(results))

'''



















