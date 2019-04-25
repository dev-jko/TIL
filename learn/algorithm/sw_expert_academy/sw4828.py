for T in range(1, int(input()) + 1):
    input()
    arr = list(map(int, input().split()))
    min, max = 1000001, 0
    for i in arr:
        max = i if i > max else max
        min = i if i < min else min
    print(f'#{T} {max - min}')
