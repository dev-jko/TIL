class Heap:
    def __init__(self):
        self.heap = [None] * 200
        self.size = 0

    def push(self, value):
        if self.size == 0:
            self.heap[1] = value
            self.size += 1
        else:
            self.size += 1
            self.heap[self.size] = value
            cur = self.size
            p = self.size // 2
            while cur > 1 and self.heap[cur] < self.heap[p]:
                self.heap[cur], self.heap[p] = self.heap[p], self.heap[cur]
                cur = p
                p = p // 2

    def pop(self):
        result = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        cur = 1
        while (cur * 2 <= self.size and self.heap[cur] > self.heap[cur * 2]) or (
                cur * 2 + 1 <= self.size and self.heap[cur] > self.heap[cur * 2 + 1]):
            child = (cur * 2) if self.heap[cur * 2] < self.heap[cur * 2 + 1] else (cur * 2 + 1)
            self.heap[cur], self.heap[child] = self.heap[child], self.heap[cur]
            cur = child
        return result

    def print(self):
        print(self.heap[1:self.size + 1])


inputs = '1 8492 29 3729 93 3892 829 83 9 28 39 823 28 398 2383 8848 42'
data = list(map(int, inputs.split()))
heap = Heap()
for n in data:
    heap.push(n)
    heap.print()
print(sorted(data))
string = '['
for i in range(heap.size):
    string += str(heap.pop()) + ', '
print(string[:-2] + ']')
