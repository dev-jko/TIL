for T in range(1, int(input()) + 1):
    N = int(input())
    result = 0
    s = 0
    for i in range(N):
        used = list(map(int, input().split()))
        if used[0] == 1:
            s += used[1]
        elif used[0] == 2:
            s -= used[1]
            s = 0 if s < 0 else s
        result += s
    print(f'#{T} {result}')
