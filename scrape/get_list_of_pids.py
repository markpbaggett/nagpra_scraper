restricted = []
all_pids = []
open_pids = []

with open('temp/all_dsids_in_wpa_tva.txt', 'r') as all_files:
    for line in all_files:
        if 'POLICY' in line:
            restricted.append(line.split('/')[1])
        pid = line.split('/')[1]
        if pid not in all_pids:
            all_pids.append(pid)
for pid in all_pids:
    if pid not in restricted:
        open_pids.append(pid)
with open('open.txt', 'w') as open_things:
    for pid in open_pids:
        open_things.write(f'{pid}\n')