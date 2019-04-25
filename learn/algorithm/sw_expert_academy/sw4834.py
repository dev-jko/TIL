for T in range(1, int(input()) + 1):
    input()
    arr = list(map(int, input()))
    cnt = [0 for _ in range(10)]
    for i in arr:
        cnt[i] += 1
    max_n = 0
    idx = 0
    for i in range(len(cnt)):
        if cnt[i] >= max_n:
            max_n = cnt[i]
            idx = i
    print(f'#{T} {idx} {max_n}')
