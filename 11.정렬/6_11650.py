import sys

# 왜 틀린지 아직 모름
# N = int(sys.stdin.readline().rstrip())
# ls = [input() for i in range(N)]

# ls.sort()
# for i in ls:
#     print(i)

N = int(sys.stdin.readline().rstrip())
ls = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    ls.append((a, b))

ls.sort()
for i in range(N):
    print(ls[i][0], ls[i][1])
