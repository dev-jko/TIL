for T in range(1, int(input()) + 1):
    N = int(input())
    result = 0
    check = True
    for i in range(1, N + 1):
        result += i if check else -i
        check = not check
    print(f'#{T} {result}')