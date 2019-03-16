NULL = 'NULL'
N = int(input().strip())
table1 = {}
header1 = input().strip().split()
for i in range(N - 1):
    inputs = input().strip().split()
    table1[int(inputs[0])] = inputs[1:]

N = int(input().strip())
table2 = {}
header2 = input().strip().split()
for i in range(N - 1):
    inputs = input().strip().split()
    table2[int(inputs[0])] = inputs[1:]

header = header1 + header2[1:]
result = []
null_cnt = len(header) - len(header1)
for key, val in table1.items():
    row = [key] + val
    if key in table2:
        row += table2[key]
    else:
        for i in range(null_cnt):
            row.append(NULL)
    result.append(row)

result.sort()
print(*header)
for row in result:
    print(*row)

