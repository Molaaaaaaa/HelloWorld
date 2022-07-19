# 시간초과
import sys
N, M = map(int, sys.stdin.readline().split())

ls_1 = [sys.stdin.readline().split() for i in range(N)]
ls_2 = [sys.stdin.readline().split() for i in range(M)]
ls_1 = sum(ls_1, [])
ls_2 = sum(ls_2, [])

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in ls_2:
  if i[0] in alpha:
    print(ls_1.index(i) + 1)
  else:
    print(ls_1[int(i) - 1])