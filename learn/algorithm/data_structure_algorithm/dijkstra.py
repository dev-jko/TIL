from heapq import heappush, heappop


def find_path(start, end):
    heap = []
    for i in range(6):
        if G[start][i] > 0:
            heappush(heap, (G[start][i], start, i))
    result = [[i, 0xffffffff] for i in range(6)]
    result[start][1] = 0
    while heap:
        w, s, e = heappop(heap)
        if result[e][1] > result[s][1] + w:
            result[e][1] = w
            result[e][0] = s
            for i in range(6):
                if G[e][i] > 0 and result[i][1] == 0xffffffff:
                    heappush(heap, (result[e][1] + G[e][i], e, i))
    path = [end]
    cur = end
    while cur != result[cur][0]:
        cur = result[cur][0]
        path.append(cur)
    path.reverse()
    string = '{}->{}, 거리 : {}, 경로 : {}'.format(start, end, result[end][1], '->'.join(map(str, path)))
    print(string)


G = [
    [0, 7, 9, -1, -1, 14],
    [7, 0, 10, 15, -1, -1],
    [9, 10, 0, 11, -1, 2],
    [-1, 15, 11, 0, 6, -1],
    [-1, -1, -1, 6, 0, 9],
    [14, -1, 2, -1, 9, 0],
]

start = 0
end = 4
for i in range(6):
    for j in range(6):
        find_path(i, j)
