n = int(input())
data = list(map(int, input().split()))
temp = [0 for _ in range(n)]
for k in range(1, n + 1):
    is_ok = True
    temp[0] = k
    for i in range(1, n):
        t = temp[i - 1] + data[i - 1]
        if t < 1 or t > n:
            is_ok = False
            break
        temp[i] = t
    if not is_ok:
        continue
    check = [0 for _ in range(n + 1)]
    for i in range(n):
        check[temp[i]] += 1
    for i in range(1, n + 1):
        if check[i] != 1:
            is_ok = False
            break
    if is_ok:
        break
else:
    print(-1)
    exit(0)
print(*temp)
