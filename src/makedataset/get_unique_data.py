import pandas as pd

max_size = 500000
dataset = pd.read_csv("syscalls_dataset.csv", delimiter=";").sample(n=max_size)

dataset2 = pd.DataFrame(columns=['last syscalls', 'syscall'])

for i in range(len(dataset)):
    print(i)
    if dataset.iloc[i]['syscall'] not in dataset2['syscall'].tolist() or dataset.iloc[i]['last syscalls'] not in dataset2['last syscalls'].tolist():
        dataset2.loc[len(dataset2.index)] = [dataset.iloc[i]['last syscalls'], dataset.iloc[i]['syscall']]

dataset2.to_csv("syscalls_dataset_2.csv", index=False)