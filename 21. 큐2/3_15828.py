import sys
from collections import deque

N = int(sys.stdin.readline())
buffer = deque()

while True:
    K = int(sys.stdin.readline())
    if K == -1:
        if len(buffer) == 0:
            print("empty")
            break
        else:
            print(*buffer)
    elif K == 0 and len(buffer) != 0:
        buffer.popleft()
    elif K != 0 and len(buffer) != N:
        buffer.append(K)
