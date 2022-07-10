# 합병정렬 실패
import sys

N = int(sys.stdin.readline().rstrip())
check = [0] * 10001

for i in range(N):
    inp = int(sys.stdin.readline().rstrip())
    check[inp] = check[inp] + 1

for i in range(10001):
    if check[i] != 0:
        for j in range(check[i]):
            print(i)