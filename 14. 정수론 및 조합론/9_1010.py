import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    top = 1
    bot_0 = 1
    bot_1 = 1
    for i in range(1, M+1):
        top *= i

    for i in range(1, N+1):
        bot_0 *= i

    for i in range(1, M-N+1):
        bot_1 *= i

    rst = top // (bot_0 * bot_1)
    
    print(rst)
