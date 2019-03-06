# https://www.acmicpc.net/problem/1244
# 스위치 켜고 끄기


N = int(input())
switch = [-1]
switch += list(map(int, input().split()))
N_s = int(input())
students = []
for _ in range(N_s):
    students.append(list(map(int, input().split())))
idx = 0
while idx < len(students) - 1:
    if students[idx] == students[idx + 1]:
        students[idx][0] = students[idx + 1][0] = 0
    idx += 1
for student in students:
    if student[0] == 1:  # 남자일때
        idx = student[1]
        while idx < len(switch):
            switch[idx] = 0 if switch[idx] else 1
            idx += student[1]
    elif student[0] == 2:  # 여자일때
        switch[student[1]] = 0 if switch[student[1]] else 1
        start = student[1] - 1
        end = student[1] + 1
        while start > 0 and end < len(switch):
            if switch[start] == switch[end]:
                switch[start] = 0 if switch[start] else 1
                switch[end] = 0 if switch[end] else 1
            else:
                break
            start -= 1
            end += 1
result = ''
for i in range(1, len(switch), 20):
    result += ' '.join(map(str, switch[i:i + 20])) + '\n'
print(result)
