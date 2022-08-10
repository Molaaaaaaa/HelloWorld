import sys
input = sys.stdin.readline

N, K = map(int, input().split())

top = 1
bot_0 = 1
bot_1 = 1

for i in range(1, N+1):
    top *= i

for i in range(1, K+1):
    bot_0 *= i

for i in range(1, N-K+1):
    bot_1 *= i

rst = (top // (bot_0 * bot_1)) % 10007

if K == 0:
    print("1")
else:
    print(rst)