import math

N = int(input().strip())

result = 99999
for i in range(int(math.sqrt(N)), 0, -1):
    if N % i == 0:
        t = abs(i - N // i)
        result = min(result, t)
        break
print(result)
