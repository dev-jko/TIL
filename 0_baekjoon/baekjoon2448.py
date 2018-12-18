import math
N = int(math.log2(int(input())/3))
star = ['  *  ', ' * * ', '*****']
for i in range(N):
    temp = [None]*2*len(star)
    for j in range(len(star)):
        temp[j] = ' '*int((len(star[-1])+1)/2) + star[j] + ' '*int((len(star[-1])+1)/2)
        temp[j+len(star)] = star[j] + ' ' + star[j]
    star = temp
for i in star:
    print(i)