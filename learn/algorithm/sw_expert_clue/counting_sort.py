arr = [0, 4, 1, 3, 1, 2, 4, 1]
cnt = [0 for x in range(5)]
for i in arr:
    cnt[i] += 1
result = []
for index, value in enumerate(cnt):
    for _ in range(value):
        result.append(index)
print(arr)
print(cnt)
print(result)
