N = int(input())
inputs = "".join(input().strip().split(' '))
t = max(map(len, inputs.split("1")))
answer = t // 2
if t % 2:
    answer += 1
print(answer)
