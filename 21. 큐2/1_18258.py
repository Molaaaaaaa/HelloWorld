import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque()

for i in range(N):
    input = sys.stdin.readline().split()

    if input[0] == "push":
        queue.append(input[1])
    elif input[0] == "pop":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.popleft())
    elif input[0] == "size":
        print(len(queue))
    elif input[0] == "empty":
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    elif input[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif input[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
