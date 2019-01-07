T = int(input())
while T > 0:
    T -= 1
    T_n = int(input())
    scores = map(int, input().split())
    counts = [0] * 101
    for i in scores:
        counts[i] += 1
    big = max(counts)
    result = -1
    for i, v in enumerate(counts):
        if v == big:
            result = i
    print(f'#{T_n} {result}')
