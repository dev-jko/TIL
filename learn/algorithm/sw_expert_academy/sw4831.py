for T in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    lines = list(map(int, input().split()))
    result = 0
    now = 0
    check = True
    while check:
        if now + K >= N:
            break
        for line in lines[::-1]:
            if now + K >= line and now != line:
                result += 1
                now = line
                break
            if now >= line:
                check = False
                result = 0
                break
        else:
            check = False
            result = 0
            break
    print(f'#{T} {result}')
