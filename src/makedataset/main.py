import re
import os
import csv

from select_files import select_files

max_files = 200
path = './log/trace_log'

selected_files = select_files(path, max_files)

print(selected_files)
print(len(selected_files))

last_n_syscalls = 5
last_syscalls = []
file_dataset_name = 'syscalls_dataset.csv'

with open(file_dataset_name, 'w', newline='') as csvfile:
    fieldnames = ['last syscalls', 'syscall']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()


files = selected_files

for f in files:
    print(f)
    data = []
    with open(f'{path}/{f}', 'r') as file:
        data = file.read().split('\n')

    dataset = []
    # reg_exp = r'(.+?) (.+?)(\(.+\))(\s*=\s*)(.*)'
    # reg_exp = r'(.*?)[ \t]([^\s]+)(\(.*\))(\s+=\s+)([-?0-9a-z]+)([ ]?)(.*)'
    reg_exp = r'([^\s]+)(\(.*\))(\s+=\s+)([-?0-9a-z]+)([ ]?)(.*)'

    for i in range(len(data) - 2):
        str = re.search(reg_exp, data[i])
        if (bool(str)):
            dataset.append(f'{f.split(".")[0]}syscall{str[1]}syscall{str[2]}syscall{str[4]}')

    if (len(dataset) > 0):
        for i in range(len(dataset) - last_n_syscalls):
            with open(file_dataset_name, 'a', newline='') as csvfile:
                fieldnames = ['last syscalls', 'syscall']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
                writer.writerow({'syscall': dataset[i + last_n_syscalls], 'last syscalls': 'last_n_syscalls'.join(dataset[i:i + last_n_syscalls])})
    else:
        os.remove(f'{path}/{f}')