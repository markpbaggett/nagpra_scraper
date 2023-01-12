l = []
with open('open.txt', 'r') as file_to_split:
    for line in file_to_split:
        l.append(line.strip())

n = 500
x = [l[i:i + n] for i in range(0, len(l), n)]
i = 0
for thing in x:
    with open(f'batches/batch_{i}.txt', 'w') as current_batch:
        for pid in thing:
            current_batch.write(f'{pid}\n')
    i += 1
