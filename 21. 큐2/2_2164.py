import sys
N = int(sys.stdin.readline())
K = 2
queue = list(range(1, N+1))

while True:
    if N == 1 or N == 2:
        print(N)
        break
    K *= 2
    if K >= N:
        print((N - (K//2)) * 2)
        break