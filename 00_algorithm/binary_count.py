arr = [1, 2, 3, 4, 5]

for i in range(1 << len(arr)):
    for j in range(len(arr)):
        if i & (1 << j):
            print(arr[j], end=' ')
        else:
            print(0, end=' ')
    print()