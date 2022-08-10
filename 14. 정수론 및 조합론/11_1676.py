import sys
input = sys.stdin.readline

N = int(input())
m = 1
for i in range(1, N+1):
    m *= i

m = str(m)
ls = []

for i in m:
    ls.append(i)

cnt = 0

for i in reversed(ls):
    if "0" == i:
        cnt += 1
    else:
        break

print(cnt)