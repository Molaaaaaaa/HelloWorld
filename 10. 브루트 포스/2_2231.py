import sys
N = int(sys.stdin.readline().rstrip())

for i in range(N):
    ls = list(map(int, str(i))) # 분해합
    result = i + sum(ls)
    if result == N:
        print(i)
        exit()

print(0)