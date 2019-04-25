N = int(input())
result = k = 1
while N > k:
    k += 6 * result
    result += 1
print(result)
