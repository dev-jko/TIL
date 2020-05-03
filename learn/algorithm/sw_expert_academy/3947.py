class Node:
    def __init__(self, start, end, dist):
        self.start = start
        self.end = end
        self.dist = dist

    def __repr__(self):
        return str(self.dist)


class Heap:
    def __init__(self):
        self.heap = [None]

    def clear(self):
        self.heap = [None]

    def push(self, node):
        self.heap.append(node)
        current = len(self.heap) - 1
        parent = current // 2
        while current > 1 and self.heap[current].dist < self.heap[parent].dist:
            self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
            current = parent
            parent = current // 2

    def pop(self):
        h = self.heap
        if self.is_empty():
            return -1
        elif len(h) == 2:
            return h.pop()
        result = h[1]
        h[1] = h.pop()
        current = 1
        c1 = h[current].dist > h[current * 2].dist if current * 2 < len(h) else False
        c2 = h[current].dist > h[current * 2 + 1].dist if current * 2 + 1 < len(h) else False
        while c1 or c2:
            if c1 and c2:
                if h[current * 2].dist < h[current * 2 + 1].dist:
                    h[current], h[current * 2] = h[current * 2], h[current]
                    current += current
                else:
                    h[current], h[current * 2 + 1] = h[current * 2 + 1], h[current]
                    current += current + 1
            elif c1:
                h[current], h[current * 2] = h[current * 2], h[current]
                current += current
            else:
                h[current], h[current * 2 + 1] = h[current * 2 + 1], h[current]
                current += current + 1
            c1 = h[current].dist > h[current * 2].dist if current * 2 < len(h) else False
            c2 = h[current].dist > h[current * 2 + 1].dist if current * 2 + 1 < len(h) else False
        return result

    def is_empty(self):
        return len(self.heap) <= 1


# h = Heap()
# from random import choice
# for i in range(500000):
#     h.push(Node(i, i, choice(range(10000))))
#     # print(h.heap)
# print()
# while not h.is_empty():
#     print(h.pop())

def get_dist(start):
    global graph
    result = [0xffffffffffff] * len(graph)
    used = [[] for _ in range(len(graph))]
    visited = [False] * len(graph)
    result[0] = 0
    h = Heap()
    h.push(Node(start, start, 0))
    while not h.is_empty():
        node = h.pop()
        d, s = node.dist, node.end
        if node.start != node.end:
            dd = list(filter(lambda x: x[0] == node.end, graph[node.start]))[0][1]
            used[node.end].append(dd)
        visited[s] = True
        for next, dd in graph[s]:
            if visited[next]:
                continue
            if d + dd <= result[next]:
                result[next] = d + dd
                h.push(Node(s, next, d + dd))
    return used


for TC in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        s, e, d = list(map(int, input().split()))
        graph[s - 1].append([e - 1, d])
        graph[e - 1].append([s - 1, d])

    used = get_dist(0)
    answer = 0
    for arr in used:
        if len(arr) == 0:
            continue
        answer += min(arr)
    print(f'#{TC} {answer}')

# 2
# 5 5
# 1 2 1
# 4 3 2
# 1 3 1
# 2 4 2
# 5 4 3
# 4 4
# 1 2 1000
# 2 3 100
# 3 4 500
# 1 4 600

# 1
# 1 0

# 1
# 200000 5
# 1 2 1
# 4 3 2
# 1 3 1
# 2 4 2
# 5 4 3


# print()
# for i in range(5, 499995):
#     print(f"{i} {i + 1} {100000000}")
#
