for T in range(1, int(input()) + 1):
    inputs = sorted(list(map(int, input().split())))[1:-1]
    result = int(round(sum(inputs) / len(inputs), 0))
    print(f'#{T} {result}')
