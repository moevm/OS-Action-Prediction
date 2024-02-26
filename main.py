import re
import numpy as np
import os

s = os.listdir()
dirs = [f for f in list(filter(os.path.isdir, os.listdir())) if f not in ['venv', '.idea']]


last_n_syscalls = 10
last_syscalls = []

# print(dirs)
# dirs = ['firefox']
for dir in dirs:
    files = os.listdir(dir)

    for f in files:
        print(f)
        data = []
        with open(f'{dir}/{f}', 'r') as file:
            data = file.read().split('\n')

        dataset = []
        reg_exp = r'(.*) (.*)(\(.*\))(\s*=\s)(.*)'

        for i in range(len(data) - 2):
            if (bool(re.search(reg_exp, data[i]))):
                str = re.sub(reg_exp, r'\1;\2;\3;\5', data[i]).split(';')
                dataset.append({'system call': str[1], 'var': str[2], 'result': str[3], 'time': str[0]})

        for i in range(len(dataset) - last_n_syscalls):
            last_syscalls.append(
                {'syscall': dataset[i + last_n_syscalls], 'last syscalls': dataset[i:i + last_n_syscalls]})

for i in range(len(last_syscalls)):
    print(i + 1, last_syscalls[i])