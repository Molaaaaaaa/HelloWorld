import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque()
rst = []

for i in range(1, N +1):
    queue.append(i)

while queue:
    for i in range(K-1):
        queue.append(queue.popleft()) # 맨 왼 -> 맨 뒤
    rst.append(queue.popleft())

print("<", end='')
print(", ".join(map(str, rst)), end=' ')
print(">")