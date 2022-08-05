import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    x, y = A, B

    while y != 0:
        x = x % y
        x, y = y, x

    print(A*B // x)