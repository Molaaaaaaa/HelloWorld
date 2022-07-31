import sys
input = sys.stdin.readline()

N = int(input.rstrip())
ls = []
i = 2

while N != 1:
    if N % i == 0:
        N = N / i
        print(i)
    else:
        i += 1