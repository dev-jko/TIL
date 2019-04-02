# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금


for T in range(1, int(input()) + 1):
    data, n = input().split()
    n = int(n)
    data = list(map(int, data))
    temp = sorted(data, reverse=True)
    idx = 0
    changes = []
    for i in range(len(data)):
        if n <= 0:
            break
        if data[i] != temp[idx]:
            n -= 1
            t = len(data) - 1
            while data[t] != temp[idx]:
                t -= 1
            data[i], data[t] = data[t], data[i]
            changes.append((i, t))
        idx += 1
    for i in range(len(changes)):
        for j in range(len(changes)):
            if i == j:
                continue
            a, b = changes[i], changes[j]
            if data[a[0]] == data[b[0]]:
                if a[1] > b[1] and data[a[1]] > data[b[1]]:
                    data[a[1]], data[b[1]] = data[b[1]], data[a[1]]
                elif a[1] < b[1] and data[a[1]] < data[b[1]]:
                    data[a[1]], data[b[1]] = data[b[1]], data[a[1]]
    if n % 2:  # 홀수
        check = False
        for i in range(1, len(data)):
            if data[i - 1] == data[i]:
                check = True
                break
        if not check:
            data[-1], data[-2] = data[-2], data[-1]
    print('#{} {}'.format(T, ''.join(map(str, data))))
