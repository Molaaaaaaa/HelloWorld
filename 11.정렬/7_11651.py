import sys

N = int(sys.stdin.readline().rstrip())
ls = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    ls.append((b, a))

ls.sort()
for i in range(N):
    print(ls[i][1], ls[i][0])