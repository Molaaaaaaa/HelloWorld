import sys
import math
input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    ds = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if ds == 0 and r1 == r2:
        print(-1)
    elif abs(r2 -r1) == ds or r1 + r2 == ds: # 내접 외접
        print(1)
    elif abs(r2 - r1) < ds < (r1 + r2): # 다른 두 점
        print(2)
    else:
        print(0)
