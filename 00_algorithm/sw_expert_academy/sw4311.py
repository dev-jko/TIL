# 4311. [연습문제] 오래된 스마트폰


class Queue:
    def __init__(self):
        self.q = [0] * 1000
        self.head = 0
        self.tail = -1
        self.size = 0

    def push(self, value):
        if self.tail + 1 >= len(self.q):
            self.q += [0] * 500
        self.tail += 1
        self.q[self.tail] = value
        self.size += 1

    def pop(self):
        value = self.q[self.head]
        self.head += 1
        self.size -= 1
        return value

    def is_empty(self):
        return True if self.size == 0 else False


for T in range(1, int(input()) + 1):
    N, O, M = map(int, input().split())
    number_str = input().split()
    number = list(map(int, number_str))
    operators = list(map(int, input().split()))
    W = int(input())
    q = Queue()
    result = [-1] * 1000
    for i in number:
        result[i] = 1
        q.push(i)
    for i in range(10, 1000):
        string = str(i)
        for s in string:
            if s not in number_str:
                break
        else:
            result[i] = len(string)
            number.append(i)
            q.push(i)
    while not q.is_empty():
        n = q.pop()
        if n == W:
            break
        for nn in number:
            cnt = result[n] + result[nn] + 1
            if cnt > M:
                continue
            for op in operators:
                if op == 1:
                    t = n + nn
                    if t <= 999 and (result[t] == -1 or cnt < result[t]):
                        result[t] = cnt
                        q.push(t)
                elif op == 2:
                    t = n - nn
                    if t >= 0 and (result[t] == -1 or cnt < result[t]):
                        result[t] = cnt
                        q.push(t)
                elif op == 3:
                    t = n * nn
                    if t <= 999 and (result[t] == -1 or cnt < result[t]):
                        result[t] = cnt
                        q.push(t)
                else:
                    if nn == 0:
                        continue
                    t = n // nn
                    if t >= 0 and (result[t] == -1 or cnt < result[t]):
                        result[t] = cnt
                        q.push(t)
    if W in number:
        print('#%d %d' % (T, result[W]))
    elif result[W] != -1 and result[W] + 1 <= M:
        print('#%d %d' % (T, result[W] + 1))
    else:
        print('#%d -1' % T)
