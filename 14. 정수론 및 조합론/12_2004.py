import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def two_cnt(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_cnt(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

t = two_cnt(n) - two_cnt(n-m) - two_cnt (m)
f = five_cnt(n) - five_cnt(n-m) - five_cnt (m)

if t > f:
    print(f)
else:
    print(t)