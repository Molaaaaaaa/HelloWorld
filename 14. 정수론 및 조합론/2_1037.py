import sys
input = sys.stdin.readline

N = int(input())
ls = list(map(int, input().split()))
ls.sort()

if len(ls) == 1:
    print(ls[0] * ls[0])
else:
    print(ls[0] * ls[-1])