n, m = map(int, input().split())
num = m // n
result = m % n
if result != 0:
    print(-1)
else:
    while num > 1:
        if num % 6 == 0:
            num //= 6
            result += 2
        else:
            break
    while num > 1:
        if num % 3 == 0:
            num //= 3
            result += 1
        else:
            break
    while num > 1:
        if num % 2 == 0:
            num //= 2
            result += 1
        else:
            break
    print(result if num == 1 else -1)
