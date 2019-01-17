f = open('./new_file.txt', 'w')
for i in range(1, 11):
    f.write(f'{i}th line\n')
f.close()

f = open('./new_file.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
f.close()

f = open('./new_file.txt', 'a')
f.write('end')
f.close()

f = open('./new_file.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
f.close()