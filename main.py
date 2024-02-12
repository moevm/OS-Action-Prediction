import re

with open('strace.log', 'r') as file:
    data = file.read().split('\n')

dataset = []

for i in range(len(data)-2):
    str = re.sub(r'(.*)(\(.*\))(\s*=\s)(.*)', r'\1;\2;\4', data[i]).split(';')
    dataset.append({'system call': str[0], 'var': str[1], 'result': str[2]})

# print(dataset[0])
# print(dataset[1])

# for i in range(len(dataset)):
#     print(dataset[i])

last_n_syscalls = 10
last_syscalls = []

for i in range(len(dataset) - last_n_syscalls - 1):
    last_syscalls.append({'syscall': dataset[i + last_n_syscalls], 'last syscalls': [dataset[i:i + last_n_syscalls]]})

print(last_syscalls[0])
print(last_syscalls[1])