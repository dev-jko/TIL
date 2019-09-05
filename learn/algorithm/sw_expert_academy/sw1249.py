import heapq

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for case in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for i in range(N):
        temp = list(map(int, input()))
        arr.append(temp)
    result = [[-1] * N for _ in range(N)]
    result[0][0] = 0
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    while len(heap) > 0:
        w, x, y = heapq.heappop(heap)
        if x == N - 1 and y == N - 1:
            break
        for dx, dy in dxy:
            xx, yy = x + dx, y + dy
            if xx < 0 or yy < 0 or xx >= N or yy >= N:
                continue
            if result[xx][yy] == -1 or w + arr[xx][yy] < result[xx][yy]:
                result[xx][yy] = w + arr[xx][yy]
                heapq.heappush(heap, (result[xx][yy], xx, yy))
    print("#", case, " ", result[-1][-1], sep="")
