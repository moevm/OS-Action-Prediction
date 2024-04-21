import os

def get_pid_max_size(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

def select_files(path, max_files):
    files = os.listdir(path)
    filesname_dict = {'.'.join(file.split('.')[:-1]): {file2.split('.')[-1]: os.path.getsize(f'{path}/{file2}')
                      for file2 in files if '.'.join(file2.split('.')[:-1]) == '.'.join(file.split('.')[:-1])}
                      for file in files}

    selected_files = []

    while (True):
        for file in filesname_dict:
            if filesname_dict[file]:
                pid = get_pid_max_size(filesname_dict[file])
                mem_size = filesname_dict[file][pid]

                selected_files.append(f'{file}.{pid}')
                filesname_dict[file].pop(pid)
                max_files -= 1
                if max_files == 0:
                    return selected_files


# max_files = 500
# path = './log/trace_log_copy'
#
# selected_files = select_files(path, max_files)
#
# print(selected_files)
# print(len(selected_files))
