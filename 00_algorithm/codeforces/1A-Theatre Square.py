# https://codeforces.com/problemset/problem/1/A
# A. Theatre Square

n, m, a = map(int, input().split())
x = n // a + (1 if n % a else 0)
y = m // a + (1 if m % a else 0)
print(x * y)
