import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

Sum = 0
ls = []
cards.sort()

for i in cards:
    for j in cards:
        for k in cards:
            if i< j and j < k:
                if i+j+k <= M:
                    ls.append(i+j+k)

print(max(ls))