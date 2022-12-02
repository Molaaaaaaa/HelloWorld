import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque()

for i in range(N):
    input = sys.stdin.readline().split()

    if input[0] == "push_front":
        queue.appendleft(input[1])

    elif input[0] == "push_back":
        queue.append(input[1])

    elif input[0] == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            tmp = queue.popleft()
            print(tmp)

    elif input[0] == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            tmp = queue.pop()
            print(tmp)

    elif input[0] == "size":
        print(len(queue))

    elif input[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

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