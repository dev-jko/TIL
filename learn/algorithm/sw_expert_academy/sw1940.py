for T in range(1, int(input()) + 1):
    N = int(input())
    result = 0
    s = 0
    for i in range(N):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            s += cmd[1]
        elif cmd[0] == 2:
            s -= cmd[1]
            s = 0 if s < 0 else s
        result += s
    print(f'#{T} {result}')
