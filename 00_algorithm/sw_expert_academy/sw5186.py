for T in range(1, int(input()) + 1):
    N = float(input())
    result = ''
    for i in range(1, 13):
        if N - 2**(-1*i) >= 0:
            result += '1'
            N -= 2**(-1*i)
        else:
            result += '0'
        if N == 0:
            break
    else:
        result = 'overflow'
    print(f'#{T} {result}')
