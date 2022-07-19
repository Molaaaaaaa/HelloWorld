import sys
N = int(sys.stdin.readline().rstrip())
ls_1 = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
ls_2 = list(map(int, sys.stdin.readline().split()))

for i in ls_2:
    cnt = 0
    while i in ls_1:
        cnt += 1
        ls_1.remove(i)
    print(cnt, end=" ")
