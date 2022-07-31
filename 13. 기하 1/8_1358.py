import sys
input = sys.stdin.readline
W, H, X, Y, P = map(int, input().split())
r = H // 2
cnt = 0
for i in range(P):
    X1, Y1 = map(int, input().split())
    if ((X1 - X) ** 2 + (Y1 - (Y+r)) ** 2) ** 0.5 <= r or\
       ((X1 - (X + W)) ** 2 + (Y1 - (Y+r)) ** 2) ** 0.5 <= r or\
       ((X <= X1 <= X + W) and (Y <= Y1 <= Y+H)):
       cnt += 1
print(cnt)