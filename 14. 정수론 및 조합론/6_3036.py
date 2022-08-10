import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

N = int(input())
ls = list(map(int, input().split()))

for i in range(1, N):
    g = gcd(ls[0], ls[i])
    print("{0}/{1}".format(ls[0]//g, ls[i]//g))