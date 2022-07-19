import sys
N, M = map(int, sys.stdin.readline().split())

S=[sys.stdin.readline().split() for i in range(N)]

cnt = 0

for i in range(M):
  inp = sys.stdin.readline().split()
  if inp in S:
    cnt += 1

print(cnt)