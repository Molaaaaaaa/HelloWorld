import sys
from collections import deque

I = int(sys.stdin.readline())

for i in range(I):
    N, M = map(int, sys.stdin.readline().split())
    case = list(map(int, sys.stdin.readline().split()))
    sol = list(range(len(case)))
    sol[M] = 10
    
    cnt = 0

    while True:
        if case[0] == max(case):
            cnt += 1
            if sol[0] == 10:
                print(cnt)
                break
            else:
                case.pop(0)
                sol.pop(0)

        else:
            case.append(case.pop(0))
            sol.append(sol.pop(0))

# deque는 max함수 안되나?