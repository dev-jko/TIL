# https://codeforces.com/problemset/problem/1141/D
# D. Colored Boots


# TODO 실패 타임오버

n = int(input())
a = input()
b = input()
data1 = [[] for _ in range(27)]
data2 = [[] for _ in range(27)]
for i in range(n):
    if a[i] == '?':
        data1[26].append(i + 1)
    else:
        data1[ord(a[i]) - 97].append(i + 1)
    if b[i] == '?':
        data2[26].append(i + 1)
    else:
        data2[ord(b[i]) - 97].append(i + 1)
idx = 0
cnt = 0
result = ''
while idx < 26:
    if data1[idx] and data2[idx]:
        result += str(data1[idx].pop()) + ' ' + str(data2[idx].pop()) + '\n'
        cnt += 1
    else:
        idx += 1
idx = 0
while data2[idx]:
    if data1[26] and data2[idx]:
        result += str(data1[26].pop()) + ' ' + str(data2[idx].pop()) + '\n'
        cnt += 1

for arr in data2:
    while arr and data1[26]:
        result += str(data1[26].pop()) + ' ' + str(arr.pop()) + '\n'
        cnt += 1
    if len(data1[26]) == 0:
        break
for arr in data1:
    while arr and data2[26]:
        result += str(arr.pop()) + ' ' + str(data2[26].pop()) + '\n'
        cnt += 1
    if len(data2[26]) == 0:
        break

print(cnt)
if cnt:
    print(result, end='')
