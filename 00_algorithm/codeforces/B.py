n = int(input())
data = list(map(int, input().split()))
data += data
result = 0
temp = 0
for i in range(len(data) - 1):
    if data[i] == 1:
        temp += 1
    else:
        result = max(result, temp)
        temp = 0
print(result)
