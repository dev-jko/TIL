a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])
if a > b:
    result = a
else:
    result = b
print(result)
