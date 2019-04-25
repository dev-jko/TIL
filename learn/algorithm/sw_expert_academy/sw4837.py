arr = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
for T in range(1, int(input()) + 1):
    result = 0
    N, K = map(int, input().split())
    for i in range(1 << len(arr)):
        Sum = 0
        cnt = 0
        for j in range(len(arr)):
            if i & 1 << j:
                Sum += arr[j]
                cnt += 1
        if cnt == N and Sum == K:
            result += 1
    print(f'#{T} {result}')
