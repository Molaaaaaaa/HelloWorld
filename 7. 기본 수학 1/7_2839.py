import sys
N = int(sys.stdin.readline().rstrip())
cnt = 0
if N == 4 or N == 7:
    print(-1)
    exit()

t = N//3
f = N//5

for i in range(0, t+1):
    for j in range(0, f+1):
        r = (3 * i) + (5 * j)
        if N == r:
            print(i + j)
            exit()
        