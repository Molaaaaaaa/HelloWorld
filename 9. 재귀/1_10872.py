# N = int(map(int, input())) 오류
# TypeError: 'map' object cannot be interpreted as an integer

import sys
N = int(sys.stdin.readline())
mul = 1

for i in range(N):
    if N == 0:
        break
    mul *= (i + 1)

print(mul)