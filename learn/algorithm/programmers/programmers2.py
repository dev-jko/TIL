from collections import deque

element = deque()
cnt = deque()
for c in list(input()):
    if c.isdigit():
        if c == '0':
            cnt.pop()
            cnt.append(10)
        else:
            cnt.append(int(c))
    else:
        if c.islower():
            element.append(element.pop() + c)
        else:
            element.append(c)

result = []
is_error = False
while len(element):
    result.append(element.popleft())
    if len(cnt):
        temp = cnt.popleft()
        if temp != 1:
            result.append(temp)
    else:
        is_error = True
        break

if len(cnt) or len(element) or is_error:
    print('error')
else:
    print(*result, sep='')
