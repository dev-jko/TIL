a = int(input())
b = int(input())
c = int(input())
s = str(a*b*c)
counts = [0]*10
for i in s:
    counts[int(i)] += 1
for i in counts:
    print(i)