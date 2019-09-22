from heapq import heappop, heappush

N = int(input())
inputs = []
for _ in range(N):
    inputs.append(list(map(int, input().strip().split(' '))))
inputs.sort(reverse=True)
answer = 1
heap = []
heappush(heap, inputs[-1][1])
time = inputs.pop()[0]
while inputs or heap:
    if heap and inputs:
        if heap[0] <= inputs[-1][0]:
            time = heappop(heap)
        else:
            time = inputs[-1][0]
    elif heap:
        time = heappop(heap)
    else:
        time = inputs[-1][0]

    while inputs and inputs[-1][0] <= time:
        heappush(heap, inputs.pop()[1])

    while heap and heap[0] <= time:
        heappop(heap)

    answer = max(answer, len(heap))

print(answer)