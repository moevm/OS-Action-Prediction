import re
import numpy as np
import os
import csv

path = 'dataset'

dirs = os.listdir(path)

print(dirs)

last_n_syscalls = 5
last_syscalls = []

# print(dirs)
dirs = ['uname']
for dir in dirs:
    newpath = f'{path}/{dir}'
    files = os.listdir(newpath)

    for f in files:
        data = []
        with open(f'{newpath}/{f}', 'r') as file:
            data = file.read().split('\n')

        dataset = []
        reg_exp = r'(.+?) (.+?)(\(.+\))(\s*=\s*)(.*)'

        for i in range(len(data) - 2):
            if (bool(re.search(reg_exp, data[i]))):
                str = re.sub(reg_exp, r'\1;\2;\3;\5', data[i]).split(';')
                # with dictionary
                # dataset.append({'system call': str[1], 'var': str[2], 'result': str[3]})

                # with str
                print(80*'-')
                print(f'{str[1]} ; {str[2]} ; {str[3].split()[0]}')
                print(80*'-')

                dataset.append(f'{str[1]}syscall{str[2]}syscall{str[3].split()[0]}')

                # with time
                # dataset.append({'system call': str[1], 'var': str[2], 'result': str[3], 'time': str[0]})

        for i in range(len(dataset) - last_n_syscalls):
            last_syscalls.append(
                {'syscall': dataset[i + last_n_syscalls], 'last syscalls': 'last_n_syscalls'.join(dataset[i:i + last_n_syscalls])})



with open('syscalls_dataset.csv', 'w', newline='') as csvfile:
    fieldnames = ['last syscalls', 'syscall']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for el in last_syscalls:
        writer.writerow(el)


# print(last_syscalls[0])
# print(last_syscalls[0]['syscall'])
# print(last_syscalls[0]['last syscalls'])

# for i in last_syscalls[0]['last syscalls']:
#     print(i)

# for i in range(len(last_syscalls)):
#     print(i + 1, last_syscalls[i])
