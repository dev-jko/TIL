for x in range(1, int(input()) + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    result = 0
    big = prices[-1]
    for i in range(N-1, -1, -1):
        if prices[i] > big:
            big = prices[i]
        else:
            result += big - prices[i]
    print(f'#{x} {result}')
