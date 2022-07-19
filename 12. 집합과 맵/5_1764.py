import sys
N, M = map(int, sys.stdin.readline().split())

no_hear = set()
for i in range(N):
    no_hear.add(sys.stdin.readline().rstrip())

no_look = set()
for i in range(M):
    no_look.add(sys.stdin.readline().rstrip())

print(len(no_hear & no_look))
answer = list(no_hear & no_look)
answer.sort()
for i in answer:
  print(i)