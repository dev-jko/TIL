T = int(input())
result = ''
for i in range(T):
    x, y = map(int, input().split())
    d = y - x
    s = 0
    count = 0
    while d > 0:
        if d <= s + 1:
            count += 1
            break
        elif d <= s * 2:
            count += 2
            break
        s += 1
        d -= s * 2
        count += 2
    result += str(count) + '\n'
print(result)
