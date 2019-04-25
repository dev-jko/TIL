clap = ('3', '6', '9')
for i in range(1, int(input()) + 1):
    i = str(i)
    count = 0
    for j in clap:
        count += i.count(j)
    print(i if count == 0 else '-' * count, end=' ')
print()
