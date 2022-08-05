import sys

a, b = map(int, sys.stdin.readline().split())

y = b
divisor_ls = []
i = 0

while i != 10000:
    i += 1
    if a % i == 0 and b % i == 0:
        a = a // i
        b = b // i
        divisor_ls.append(i)
        if i > 1:
            i -= 1
    

min_mul = 1
for i in divisor_ls:
    min_mul *= i

print(min_mul)
print(a * y)