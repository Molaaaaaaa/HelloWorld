import sys

N = int(sys.stdin.readline())
ls = [sys.stdin.readline().split() for i in range(N)]

for i in ls:
    i[0] = int(i[0])
    i[1] = int(i[1])

print(ls)