N = int(input().strip())
data = [int(input().strip()) for _ in range(N)]
result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if data[i] <= data[j]:
            result = max(result, j - i)
            break
for i in range(N - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        if data[i] < data[j]:
            result = max(result, i - j)
            break
print(result)
