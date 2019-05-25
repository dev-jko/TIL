qs = ['123', '456', '789']
a = [s2 for s1 in qs for s2 in s1]
print(a)

aa = [s2 for s1 in qs for s2 in s1]
print(aa)


aaa = []
for s1 in qs:
    for s2 in s1:
        aaa.append(s2)
print(aaa)

# aaaa = [s2 for s2 in s1 for s1 in qs]
# print(aaaa)
