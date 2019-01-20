currency_unit = (50000, 10000, 5000, 1000, 500, 100, 50, 10)
for T in range(1, int(input()) + 1):
    N = int(input())//10*10
    result = []
    for i in currency_unit:
        count = N//i
        N -= i * count
        result.append(count)
    print(f'#{T}')
    print(*result)
