from collections import deque
from heapq import heappop, heappush

msg, consumer_n = map(int, input().strip().split(' '))
d = deque()
consumer = []
for _ in range(msg):
    d.append(int(input()))

answer = 0
while len(d) > 0 or len(consumer) > 0:
    while len(d) > 0 and len(consumer) < consumer_n:
        heappush(consumer, d.popleft())

    min_n = heappop(consumer)
    answer += min_n
    for i in range(len(consumer)):
        consumer[i] -= min_n

print(answer)

