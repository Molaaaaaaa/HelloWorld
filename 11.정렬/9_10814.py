import sys

N = int(sys.stdin.readline().rstrip())
ls = [input().rstrip() for i in range(N)]
for i in range(N):
    a, b = ls[i].split(" ")
    ls[i] = [a, b]

age = []
for i in range(N):
    age.append([ls[i][0], i])

age.sort()

for i in range(N):
    idx = age[i][1]
    print(ls[idx][0], ls[idx][1])